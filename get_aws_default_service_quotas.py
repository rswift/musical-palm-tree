#
# Retrieve the list of AWS services to then individually retrieve default quota limits for...
#
import boto3
import json
import os
from time import sleep

all_services = False # setting to True will ignore the list below and gather data for every service, False will only retrieve services on the list
region = "eu-west-2" # set here for clarity in the script

try:
    identity = boto3.client('sts', region_name=region).get_caller_identity()
    gamut = "all" if all_services else "a subset of"
    print(f"Retrieving AWS default quotas for {gamut} services, from {identity['Account']} in {region}")
except Exception as e:
    print(f"It doesn't seem possible to authenticate to AWS: {e}")
    quit()

sq = boto3.client('service-quotas', region_name=region)

# purely for example...
services_of_interest = [
    "apigateway", "autoscaling", "appmesh",
    "cloudformation", "cloudtrail", "cognito-identity", "cognito-idp", "cognito-sync",
    "dynamodb",
    "ebs", "ec2", "ecr", "ecs", "eks", "elasticache", "elasticfilesystem", "elasticloadbalancing", "events",
    "fargate",
    "glacier",
    "kms",
    "lambda", "logs",
    "monitoring",
    "ram", "rds",
    "s3", "secretsmanager", "servicecatalog", "sns", "sqs",
    "vpc",
    "xray"
]

#
# specify a filename to write out JSON and/or Markdown, or None to swerve
#
output_json_file = None
output_markdown_file = "aws_default_quota_limits.md"
if not output_json_file and not output_markdown_file:
    print("No output files set, not much point in executing... 😏")
    quit()

paginator = sq.get_paginator('list_services')
all_aws_services = {}
response_iterator = paginator.paginate()
for response in response_iterator:
    for services in response['Services']:
        all_aws_services[services['ServiceCode']] = services['ServiceName']

all_aws_service_quotas = {}
for service, label in all_aws_services.items():
    if all_services or service in services_of_interest:
        print(f"Retrieving quota limits for {label} (AWS Service: {service})")
        all_aws_service_quotas[service] = {"description": label}
        paginator = sq.get_paginator('list_aws_default_service_quotas')
        sleep(0.2) # try and avoid 429's 🖖
        response_iterator = paginator.paginate(ServiceCode=service)
        for response in response_iterator:
            for quotas in response['Quotas']:
                all_aws_service_quotas[service][quotas['QuotaCode']] = {
                    "description": quotas['QuotaName'],
                    "value": quotas['Value'],
                    "unit": quotas['Unit'],
                    "adjustable": bool(quotas['Adjustable']),
                    "global": bool(quotas['GlobalQuota'])
                }

if output_json_file:
    with open(output_json_file, "w") as f:
        f.write(json.dumps(all_aws_service_quotas))
        print(f"Dump of JSON response written to {f.name}")

if output_markdown_file:
    import datetime
    today = datetime.date.today()
    day = today.day
    if 4 <= day <= 20 or 24 <= day <= 30:
        o = "th"
    else:
        o = ["st", "nd", "rd"][day % 10 - 1]
    retrieved = f"{day}{o} of {today.strftime('%B')} {today.year}" # because i'm a tart...

    with open(output_markdown_file, "w") as f:
        f.write(f"# Default AWS Service Quotas{os.linesep*2}")
        f.write(f"Retrieved for an account in `{region}` on the {retrieved}{os.linesep*2}")
        f.write(f"Full details can be found [in the AWS documentation](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html \"AWS Service Quotas Documentation\"), but AWS define Service Quotas as:{os.linesep}")
        f.write(f"> Quotas, also referred to as limits in AWS services, are the maximum values for the resources, actions, and items in your AWS account. Each AWS service defines its quotas and establishes default values for those quotas.{os.linesep*2}")

        for service in all_aws_service_quotas:
            f.write(f"## {all_aws_service_quotas[service]['description']} (AWS Service: {service}){os.linesep*2}")
            f.write(f"| Property | Limit | Unit | Adjustable | Global |{os.linesep}")
            f.write(f"|---|---|---|---|---|{os.linesep}")
            quote_code = None
            for entry in all_aws_service_quotas[service]:
                if entry != "description":
                    field = all_aws_service_quotas[service][entry]
                    f.write(f"| {field['description']} | {field['value']} | {field['unit']} | {field['adjustable']} | {field['global']} |{os.linesep}")
            f.write(f"{os.linesep}")
        print(f"Markdown rendering written to {f.name}")
