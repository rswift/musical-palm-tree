# Default AWS Service Quotas

Retrieved for an account in `eu-west-2` on the 19th of August 2022

Full details can be found [in the AWS documentation](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html "AWS Service Quotas Documentation"), but AWS define Service Quotas as:
> Quotas, also referred to as limits in AWS services, are the maximum values for the resources, actions, and items in your AWS account. Each AWS service defines its quotas and establishes default values for those quotas.

## AWS Cloud Map (AWS Service: AWSCloudMap)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Custom attributes per instance | 30.0 | None | False | False |
| DiscoverInstances operation per account burst rate | 2000.0 | None | True | False |
| DiscoverInstances operation per account steady rate | 1000.0 | None | True | False |
| Instances per namespace | 2000.0 | None | True | False |
| Instances per service | 1000.0 | None | False | False |
| Namespaces per Region | 50.0 | None | True | False |

## Access Analyzer (AWS Service: access-analyzer)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Access previews per analyzer per hour | 1000.0 | None | True | False |
| Analyzers with an account zone of trust | 1.0 | None | False | False |
| Analyzers with an organization zone of trust | 5.0 | None | True | False |
| Archive rules per analyzer | 100.0 | None | True | False |
| CloudTrail log files processed per policy generation | 100000.0 | None | False | False |
| Concurrent policy generations | 1.0 | None | False | False |
| Policy generation CloudTrail data size | 25.0 | Gigabytes | False | False |
| Policy generation CloudTrail time range | 90.0 | None | False | False |
| Policy generations per day | 50.0 | None | False | False |

## AWS Certificate Manager (ACM) (AWS Service: acm)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| ACM certificates | 2500.0 | None | True | False |
| ACM certificates created in last 365 days | 5000.0 | None | True | False |
| Domain names per ACM certificate | 10.0 | None | True | False |
| Imported certificates | 2500.0 | None | True | False |
| Imported certificates in last 365 days | 5000.0 | None | True | False |

## AWS Certificate Manager Private Certificate Authority (ACM PCA) (AWS Service: acm-pca)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Number of private certificate authorities (CAs) | 200.0 | None | True | False |
| Number of private certificates per CA | 1000000.0 | None | True | False |
| Number of revoked private certificates per CA | 1000000.0 | None | False | False |
| Rate of CreateCertificateAuthority requests | 1.0 | None | False | False |
| Rate of CreateCertificateAuthorityAuditReport requests | 1.0 | None | False | False |
| Rate of CreatePermission requests | 1.0 | None | False | False |
| Rate of DeleteCertificateAuthority requests | 10.0 | None | False | False |
| Rate of DeletePermission requests | 1.0 | None | False | False |
| Rate of DeletePolicy requests | 5.0 | None | False | False |
| Rate of DescribeCertificateAuthority requests | 20.0 | None | False | False |
| Rate of DescribeCertificateAuthorityAuditReport requests | 20.0 | None | False | False |
| Rate of GetCertificate requests | 75.0 | None | True | False |
| Rate of GetCertificateAuthorityCertificate requests | 20.0 | None | False | False |
| Rate of GetCertificateAuthorityCsr requests | 10.0 | None | False | False |
| Rate of GetPolicy requests | 5.0 | None | False | False |
| Rate of ImportCertificateAuthorityCertificate requests | 10.0 | None | False | False |
| Rate of IssueCertificate requests | 25.0 | None | True | False |
| Rate of ListCertificateAuthorities requests | 20.0 | None | False | False |
| Rate of ListPermissions requests | 5.0 | None | False | False |
| Rate of ListTags requests | 20.0 | None | False | False |
| Rate of PutPolicy requests | 5.0 | None | False | False |
| Rate of RestoreCertificateAuthority requests | 20.0 | None | False | False |
| Rate of RevokeCertificate requests | 20.0 | None | False | False |
| Rate of TagCertificateAuthority requests | 10.0 | None | False | False |
| Rate of UntagCertificateAuthority requests | 10.0 | None | False | False |
| Rate of UpdateCertificateAuthority requests | 10.0 | None | False | False |

## Amazon Managed Workflows for Apache Airflow (AWS Service: airflow)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Environments per account per Region | 10.0 | None | True | False |
| Workers per environment | 25.0 | None | True | False |

## AWS Amplify (AWS Service: amplify)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Apps | 25.0 | None | True | False |
| Branches per app | 50.0 | None | True | False |
| Build artifact size | 5.0 | Gigabytes | False | False |
| Cache artifact size | 5.0 | Gigabytes | False | False |
| Concurrent jobs | 5.0 | None | True | False |
| Domains per app | 5.0 | None | True | False |
| Environment cache artifact size | 5.0 | Gigabytes | False | False |
| Manual deploy ZIP file size | 5.0 | Gigabytes | False | False |
| Maximum app creations per hour | 25.0 | None | False | False |
| Subdomains per domain | 50.0 | None | True | False |
| Webhooks per app | 50.0 | None | True | False |

## Amplify UI Builder (AWS Service: amplifyuibuilder)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Component size | 350.0 | Kilobytes | False | False |
| Components per app | 1000.0 | None | False | False |
| Theme size | 350.0 | Kilobytes | False | False |
| Themes per app | 1000.0 | None | False | False |
| Themes per app | 1000.0 | None | False | False |

## Amazon API Gateway (AWS Service: apigateway)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| API Payload Size | 10.0 | Megabytes | False | False |
| API Stage throttles in a usage plan | 100.0 | None | False | False |
| API keys | 10000.0 | None | False | False |
| AWS Lambda authorizer result size | 8.0 | Kilobytes | False | False |
| Client certificates | 60.0 | None | True | False |
| Connection duration for WebSocket API | 7200.0 | Seconds | False | False |
| Custom Domain Names | 120.0 | None | True | False |
| Edge API URL Length | 8192.0 | None | False | False |
| Edge-optimized APIs | 120.0 | None | False | False |
| Maximum API caching TTL | 3600.0 | Seconds | False | False |
| Maximum Cached Response Size | 1048576.0 | Bytes | False | False |
| Maximum Combined Header Size | 10240.0 | Bytes | False | False |
| Maximum Iterations In Mapping Template | 1000.0 | None | False | False |
| Maximum integration timeout in milliseconds | 29000.0 | Milliseconds | False | False |
| Maximum resource policy size in bytes | 8192.0 | None | True | False |
| Method ARN Length | 1600.0 | Bytes | False | False |
| Private APIs | 600.0 | None | False | False |
| Regional API URL Length | 10240.0 | None | False | False |
| Regional APIs | 600.0 | None | False | False |
| Resources/Routes per REST/WebSocket API | 300.0 | None | True | False |
| Routes per HTTP API | 300.0 | None | True | False |
| Stage Variable Key Length | 64.0 | None | False | False |
| Stage Variable Value Length | 512.0 | None | False | False |
| Stage variables per stage | 100.0 | None | False | False |
| Stages per API | 10.0 | None | True | False |
| Subnets per VPC link(V2) | 10.0 | None | True | False |
| Tags Per Stage | 50.0 | None | False | False |
| Throttle burst rate | 5000.0 | None | False | False |
| Throttle rate | 10000.0 | None | True | False |
| Usage plans | 300.0 | None | True | False |
| Usage plans per API key | 10.0 | None | True | False |
| VPC links | 20.0 | None | True | False |
| VPC links(V2) | 10.0 | None | True | False |
| WebSocket Idle Connection Timeout | 600.0 | Seconds | False | False |
| WebSocket frame size | 32.0 | Kilobytes | False | False |
| WebSocket message payload size | 128.0 | Kilobytes | False | False |
| WebSocket new connections burst rate | 500.0 | None | False | False |
| WebSocket new connections rate | 500.0 | None | True | False |

## AWS AppConfig (AWS Service: appconfig)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Configuration size limit in AWS AppConfig hosted configuration store | 1024.0 | Kilobytes | True | False |
| Deployment size limit | 1024.0 | Kilobytes | True | False |
| Maximum number of applications | 100.0 | None | True | False |
| Maximum number of configuration profiles per application | 100.0 | None | True | False |
| Maximum number of deployment strategies | 20.0 | None | True | False |
| Maximum number of environments per application | 20.0 | None | True | False |

## Amazon AppFlow (AWS Service: appflow)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Amazon AppFlow flow run size | 100.0 | Gigabytes | False | False |
| Amazon EventBridge event size | 256.0 | Kilobytes | False | False |
| Amplitude flow run size | 25.0 | Megabytes | False | False |
| Concurrent flow runs | 1000.0 | None | True | False |
| Connector profiles | 100.0 | None | True | False |
| Google Analytics dimensions | 9.0 | None | False | False |
| Google Analytics metrics | 10.0 | None | False | False |
| Marketo flow run size | 20.0 | Megabytes | False | False |
| Monthly flow runs | 10000000.0 | None | True | False |
| Rate of Amazon AppFlow flow runs | 1.0 | None | False | False |
| Rate of Amazon S3 flow runs | 1.0 | None | False | False |
| Rate of Amplitude flow runs | 1.0 | None | False | False |
| Rate of Datadog flow runs | 1.0 | None | False | False |
| Rate of Dynatrace flow runs | 1.0 | None | False | False |
| Rate of Google Analytics flow runs | 1.0 | None | False | False |
| Rate of Infor Nexus flow runs | 1.0 | None | False | False |
| Rate of Marketo flow runs | 1.0 | None | False | False |
| Rate of Salesforce Pardot flow runs | 1.0 | None | False | False |
| Rate of Salesforce flow runs | 1.0 | None | False | False |
| Rate of ServiceNow flow runs | 1.0 | None | False | False |
| Rate of Singular flow runs | 1.0 | None | False | False |
| Rate of Slack flow runs | 1.0 | None | False | False |
| Rate of TrendMicro flow runs | 1.0 | None | False | False |
| Rate of Veeva flow runs | 1.0 | None | False | False |
| Rate of Zendesk flow runs | 1.0 | None | False | False |
| Salesforce event size | 1.0 | Megabytes | False | False |
| Salesforce flow run data export size | 500.0 | Megabytes | False | False |
| Salesforce flow run data import size | 15.0 | Gigabytes | False | False |
| ServiceNow records | 100000.0 | None | False | False |
| Total flows | 1000.0 | None | True | False |

## Application Auto Scaling (AWS Service: application-autoscaling)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Scalable targets for Amazon Keyspaces | 500.0 | None | True | False |
| Scalable targets for Amazon MSK | 500.0 | None | True | False |
| Scalable targets for Comprehend | 500.0 | None | True | False |
| Scalable targets for DynamoDB | 5000.0 | None | True | False |
| Scalable targets for EC2 | 500.0 | None | True | False |
| Scalable targets for ECS | 3000.0 | None | True | False |
| Scalable targets for EMR | 500.0 | None | True | False |
| Scalable targets for Lambda | 500.0 | None | True | False |
| Scalable targets for RDS | 500.0 | None | True | False |
| Scalable targets for SageMaker | 500.0 | None | True | False |
| Scalable targets for custom resources | 500.0 | None | True | False |
| Scaling policies per scalable target | 50.0 | None | False | False |
| Scheduled actions per scalable target | 200.0 | None | False | False |
| Step adjustments per step scaling policy | 20.0 | None | False | False |

## AWS App Mesh (AWS Service: appmesh)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Backends per virtual node | 50.0 | None | True | False |
| Connected Envoy processes per virtual gateway | 50.0 | None | True | False |
| Connected Envoy processes per virtual node | 50.0 | None | True | False |
| Gateway routes per virtual gateway | 10.0 | None | True | False |
| Meshes per account | 15.0 | None | True | False |
| Routes per virtual router | 50.0 | None | True | False |
| Virtual gateways per mesh | 3.0 | None | True | False |
| Virtual nodes per mesh | 200.0 | None | True | False |
| Virtual routers per mesh | 200.0 | None | True | False |
| Virtual services per mesh | 200.0 | None | True | False |
| Weighted targets per route | 10.0 | None | False | False |

## Amazon AppStream 2.0 (AWS Service: appstream2)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Active fleets | 10.0 | None | True | False |
| Compute-optimized 2xlarge streaming instances for fleets | 0.0 | None | True | False |
| Compute-optimized 2xlarge streaming instances for image builders | 0.0 | None | True | False |
| Compute-optimized 4xlarge streaming instances for fleets | 0.0 | None | True | False |
| Compute-optimized 4xlarge streaming instances for image builders | 0.0 | None | True | False |
| Compute-optimized 8xlarge streaming instances for fleets | 0.0 | None | True | False |
| Compute-optimized 8xlarge streaming instances for image builders | 0.0 | None | True | False |
| Compute-optimized large streaming instances for fleets | 10.0 | None | True | False |
| Compute-optimized large streaming instances for image builders | 3.0 | None | True | False |
| Compute-optimized xlarge streaming instances for fleets | 10.0 | None | True | False |
| Compute-optimized xlarge streaming instances for image builders | 3.0 | None | True | False |
| Concurrent image copies per destination Region | 2.0 | None | True | False |
| Concurrent image updates | 5.0 | None | True | False |
| Fleets | 10.0 | None | True | False |
| Graphics G4DN 12xlarge streaming instances for fleets | 0.0 | None | True | False |
| Graphics G4DN 12xlarge streaming instances for image builders | 0.0 | None | True | False |
| Graphics G4DN 16xlarge streaming instances for fleets | 0.0 | None | True | False |
| Graphics G4DN 16xlarge streaming instances for image builders | 0.0 | None | True | False |
| Graphics G4DN 2xlarge streaming instances for fleets | 0.0 | None | True | False |
| Graphics G4DN 2xlarge streaming instances for image builders | 0.0 | None | True | False |
| Graphics G4DN 4xlarge streaming instances for fleets | 0.0 | None | True | False |
| Graphics G4DN 4xlarge streaming instances for image builders | 0.0 | None | True | False |
| Graphics G4DN 8xlarge streaming instances for fleets | 0.0 | None | True | False |
| Graphics G4DN 8xlarge streaming instances for image builders | 0.0 | None | True | False |
| Graphics G4DN xlarge streaming instances for fleets | 0.0 | None | True | False |
| Graphics G4DN xlarge streaming instances for image builders | 0.0 | None | True | False |
| Graphics design 2xlarge streaming instances for fleets | 10.0 | None | True | False |
| Graphics design 2xlarge streaming instances for image builders | 3.0 | None | True | False |
| Graphics design 4xlarge streaming instances for fleets | 0.0 | None | True | False |
| Graphics design 4xlarge streaming instances for image builders | 0.0 | None | True | False |
| Graphics design large streaming instances for fleets | 10.0 | None | True | False |
| Graphics design large streaming instances for image builders | 3.0 | None | True | False |
| Graphics design xlarge streaming instances for fleets | 10.0 | None | True | False |
| Graphics design xlarge streaming instances for image builders | 3.0 | None | True | False |
| Graphics pro 16xlarge streaming instances for fleets | 0.0 | None | True | False |
| Graphics pro 16xlarge streaming instances for image builders | 0.0 | None | True | False |
| Graphics pro 4xlarge streaming instances for fleets | 0.0 | None | True | False |
| Graphics pro 4xlarge streaming instances for image builders | 0.0 | None | True | False |
| Graphics pro 8xlarge streaming instances for fleets | 0.0 | None | True | False |
| Graphics pro 8xlarge streaming instances for image builders | 0.0 | None | True | False |
| Image builders | 10.0 | None | True | False |
| Image sharing limit | 100.0 | None | True | False |
| Max concurrent sessions for Elastic fleets with Amazon Linux 2 platform and stream.standard.2xlarge instance type | 10.0 | None | True | False |
| Max concurrent sessions for Elastic fleets with Amazon Linux 2 platform and stream.standard.large instance type | 50.0 | None | True | False |
| Max concurrent sessions for Elastic fleets with Amazon Linux 2 platform and stream.standard.medium instance type | 50.0 | None | True | False |
| Max concurrent sessions for Elastic fleets with Amazon Linux 2 platform and stream.standard.small instance type | 50.0 | None | True | False |
| Max concurrent sessions for Elastic fleets with Amazon Linux 2 platform and stream.standard.xlarge instance type | 10.0 | None | True | False |
| Max concurrent sessions for Elastic fleets with Windows Server 2019 platform and stream.standard.2xlarge instance type | 10.0 | None | True | False |
| Max concurrent sessions for Elastic fleets with Windows Server 2019 platform and stream.standard.large instance type | 50.0 | None | True | False |
| Max concurrent sessions for Elastic fleets with Windows Server 2019 platform and stream.standard.medium instance type | 50.0 | None | True | False |
| Max concurrent sessions for Elastic fleets with Windows Server 2019 platform and stream.standard.small instance type | 50.0 | None | True | False |
| Max concurrent sessions for Elastic fleets with Windows Server 2019 platform and stream.standard.xlarge instance type | 10.0 | None | True | False |
| Memory-optimized large streaming instances for fleets | 10.0 | None | True | False |
| Memory-optimized large streaming instances for image builders | 3.0 | None | True | False |
| Memory-optimized xlarge streaming instances for fleets | 10.0 | None | True | False |
| Memory-optimized xlarge streaming instances for image builders | 3.0 | None | True | False |
| Memory-optimized z1d 12xlarge streaming instances for fleets | 0.0 | None | True | False |
| Memory-optimized z1d 12xlarge streaming instances for image builders | 0.0 | None | True | False |
| Memory-optimized z1d 2xlarge streaming instances for fleets | 0.0 | None | True | False |
| Memory-optimized z1d 2xlarge streaming instances for image builders | 0.0 | None | True | False |
| Memory-optimized z1d 3xlarge streaming instances for fleets | 0.0 | None | True | False |
| Memory-optimized z1d 3xlarge streaming instances for image builders | 0.0 | None | True | False |
| Memory-optimized z1d 6xlarge streaming instances for fleets | 0.0 | None | True | False |
| Memory-optimized z1d 6xlarge streaming instances for image builders | 0.0 | None | True | False |
| Memory-optimized z1d large streaming instances for fleets | 10.0 | None | True | False |
| Memory-optimized z1d large streaming instances for image builders | 3.0 | None | True | False |
| Memory-optimized z1d xlarge streaming instances for fleets | 10.0 | None | True | False |
| Memory-optimized z1d xlarge streaming instances for image builders | 3.0 | None | True | False |
| Private images | 10.0 | None | True | False |
| Stacks | 10.0 | None | True | False |
| Standard 2xlarge streaming instances for fleets | 10.0 | None | True | False |
| Standard large streaming instances for fleets | 50.0 | None | True | False |
| Standard large streaming instances for image builders | 5.0 | None | True | False |
| Standard medium streaming instances for fleets | 50.0 | None | True | False |
| Standard medium streaming instances for image builders | 5.0 | None | True | False |
| Standard small streaming instances for fleets | 50.0 | None | True | False |
| Standard small streaming instances for image builders | 5.0 | None | True | False |
| Standard xlarge streaming instances for fleets | 10.0 | None | True | False |
| Users in the user pool | 50.0 | None | True | False |

## AWS AppSync (AWS Service: appsync)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| API keys per API | 50.0 | None | False | False |
| APIs per region | 25.0 | None | True | False |
| Authentication providers per API | 50.0 | None | False | False |
| Evaluated resolver template size | 5.0 | Megabytes | False | False |
| Functions per pipeline resolver | 10.0 | None | False | False |
| Iterations in a foreach loop in mapping templates | 1000.0 | None | False | False |
| Max Batch Size | 2000.0 | None | False | False |
| Number of caching keys | 25.0 | None | False | False |
| Number of custom domain names | 25.0 | None | True | False |
| Rate of request tokens | 2000.0 | None | True | False |
| Rate of subscription invalidation requests | 100.0 | None | False | False |
| Request execution time for mutations, queries, and subscriptions | 30.0 | Seconds | False | False |
| Request mapping template size | 64.0 | Kilobytes | False | False |
| Resolvers executed in a single request | 10000.0 | None | False | False |
| Response mapping template size | 64.0 | Kilobytes | False | False |
| Schema document size | 1.0 | Megabytes | False | False |
| Subscription payload size | 240.0 | Kilobytes | False | False |
| Subscriptions per connection | 100.0 | None | True | False |

## Amazon Managed Prometheus (AWS Service: aps)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| API operations burst-rate quota in transactions per second | 10.0 | None | True | False |
| API operations rate quota in transactions per second | 10.0 | None | True | False |
| Active alerts per alert manager | 1000.0 | None | True | False |
| Active series per metric name | 200000.0 | None | True | False |
| Active series per workspace | 1000000.0 | None | True | False |
| Aggregation groups per alert manager definition | 1000.0 | None | True | False |
| Alert manager file size | 1.0 | Megabytes | False | False |
| Ingestion burst size per workspace | 1000000.0 | None | True | False |
| Ingestion rate per workspace | 70000.0 | None | True | False |
| Inhibition rules per alert manager definition | 100.0 | None | True | False |
| Labels per metric series | 70.0 | None | True | False |
| Nodes on routing tree per alert manager definition | 100.0 | None | True | False |
| Query bytes for instant queries | 750.0 | Megabytes | False | False |
| Query bytes for range queries | 750.0 | Megabytes | False | False |
| Query samples | 12000000.0 | None | False | False |
| Query time range in days | 32.0 | None | False | False |
| Retention time for ingested data in days | 150.0 | None | True | False |
| Rule group namespaces per workspace | 10.0 | None | True | False |
| Rule groups file size | 1.0 | Megabytes | False | False |
| Rule groups per workspace | 100.0 | None | True | False |
| Rules per rule group | 20.0 | None | True | False |
| Templates per alert manager definition | 100.0 | None | True | False |
| Total active alert payload size per alert manager | 20.0 | Megabytes | False | False |
| Workspaces per region | 10.0 | None | True | False |

## Amazon Athena (AWS Service: athena)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Active DDL queries | 20.0 | None | True | False |
| Active DML queries | 100.0 | None | True | False |
| DDL query timeout | 600.0 | None | True | False |
| DML query timeout | 30.0 | None | True | False |

## AWS Audit Manager (AWS Service: auditmanager)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Custom controls | 500.0 | None | True | False |
| Custom frameworks | 100.0 | None | True | False |
| Running assessments | 100.0 | None | True | False |

## Amazon EC2 Auto Scaling (AWS Service: autoscaling)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Auto Scaling groups per region | 500.0 | None | True | False |
| Classic Load Balancers per Auto Scaling group | 50.0 | None | False | False |
| Launch configurations per region | 200.0 | None | True | False |
| Lifecycle hooks per Auto Scaling group | 50.0 | None | False | False |
| SNS topics per Auto Scaling group | 10.0 | None | False | False |
| Scaling policies per Auto Scaling group | 50.0 | None | False | False |
| Scheduled actions per Auto Scaling group | 125.0 | None | False | False |
| Step adjustments per step scaling policy | 20.0 | None | False | False |
| Target groups per Auto Scaling group | 50.0 | None | False | False |

## AWS Auto Scaling Plans (AWS Service: autoscaling-plans)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Scaling instructions per scaling plan | 500.0 | None | False | False |
| Scaling plans | 100.0 | None | True | False |
| Target tracking configurations per scaling instruction | 10.0 | None | False | False |

## AWS Backup (AWS Service: backup)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Backup plans per Region per account | 100.0 | None | True | False |
| Backup vaults per Region per account | 100.0 | None | True | False |
| Concurrent backup copies per supported service per account | 5.0 | None | False | False |
| Concurrent backup jobs per resource | 1.0 | None | False | False |
| Framework controls per Region per account | 50.0 | None | True | False |
| Frameworks per Region per account | 10.0 | None | True | False |
| Frameworks per report plan | 1000.0 | None | False | False |
| Metadata tags per backup | 50.0 | None | False | False |
| Recovery points per backup vault | 1000000.0 | None | True | False |
| Report plans per Region per account | 20.0 | None | True | False |
| Versions per backup plan | 2000.0 | None | True | False |

## AWS Batch (AWS Service: batch)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Compute environment limit | 50.0 | None | False | False |
| Compute environments per job queue limit. | 3.0 | None | False | False |
| Job dependencies limit | 20.0 | None | False | False |
| Job payload size limit | 30.0 | None | False | False |
| Job queue limit | 50.0 | None | False | False |
| Maximum array size limit | 10000.0 | None | False | False |
| Share identifiers per job queue limit. | 500.0 | None | False | False |
| Submitted state jobs limit | 1000000.0 | None | False | False |

## Amazon Braket (AWS Service: braket)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Burst rate of API requests | 600.0 | None | False | False |
| Burst rate of CancelJob requests | 5.0 | None | False | False |
| Burst rate of CancelQuantumTask requests | 20.0 | None | False | False |
| Burst rate of CreateJob requests | 5.0 | None | False | False |
| Burst rate of CreateQuantumTask requests | 40.0 | None | False | False |
| Burst rate of GetDevice requests | 50.0 | None | False | False |
| Burst rate of GetJob requests | 25.0 | None | False | False |
| Burst rate of GetQuantumTask requests | 500.0 | None | False | False |
| Burst rate of SearchDevices requests | 50.0 | None | False | False |
| Burst rate of SearchJobs requests | 50.0 | None | False | False |
| Burst rate of SearchQuantumTasks requests | 50.0 | None | False | False |
| Maximum allowed compute instances for a job | 2.0 | None | True | False |
| Number of concurrent DM1 tasks | 50.0 | None | False | False |
| Number of concurrent SV1 tasks | 50.0 | None | False | False |
| Number of concurrent TN1 tasks | 5.0 | None | True | False |
| Number of concurrent jobs | 5.0 | None | True | False |
| Rate of API requests | 140.0 | None | True | False |
| Rate of CancelJob requests | 2.0 | None | True | False |
| Rate of CancelQuantumTask requests | 2.0 | None | True | False |
| Rate of CreateJob requests | 1.0 | None | True | False |
| Rate of CreateQuantumTask requests | 20.0 | None | True | False |
| Rate of GetDevice requests | 5.0 | None | True | False |
| Rate of GetJob requests | 5.0 | None | True | False |
| Rate of GetQuantumTask requests | 100.0 | None | True | False |
| Rate of SearchDevices requests | 5.0 | None | True | False |
| Rate of SearchJobs requests | 5.0 | None | True | False |
| Rate of SearchQuantumTasks requests | 5.0 | None | True | False |

## Amazon Keyspaces (for Apache Cassandra) (AWS Service: cassandra)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Account-level read throughput quota (Provisioned mode) | 80000.0 | None | True | False |
| Account-level write throughput quota (Provisioned mode) | 80000.0 | None | True | False |
| Concurrent DDL operations | 50.0 | None | False | False |
| Keyspaces per region | 256.0 | None | True | False |
| Max Schema size | 358400.0 | Bytes | False | False |
| Max amount of data restored using Point-in-time Recovery (PITR) | 5.0 | Terabytes | True | False |
| Max clustering key size | 850.0 | Bytes | False | False |
| Max concurrent table restores using Point-in-time Recovery (PITR) | 4.0 | None | True | False |
| Max partition key size | 2048.0 | Bytes | False | False |
| Max row size | 1.0 | Megabytes | False | False |
| Max static data per logical partition | 1.0 | Megabytes | False | False |
| Table-level read throughput quota | 40000.0 | None | True | False |
| Table-level write throughput quota | 40000.0 | None | True | False |
| Tables per region | 256.0 | None | True | False |

## AWS Cloud9 (AWS Service: cloud9)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| EC2 development environments | 100.0 | None | True | False |
| EC2 development environments | 200.0 | None | True | False |
| Members per development environment | 8.0 | None | False | False |
| SSH development environments | 200.0 | None | True | False |
| SSH development environments | 100.0 | None | True | False |

## AWS CloudFormation (AWS Service: cloudformation)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Attributes per mapping in CloudFormation template | 200.0 | None | False | False |
| Data in custom resource provider | 4096.0 | Bytes | False | False |
| Declared mappings in CloudFormation template. | 200.0 | None | False | False |
| Maximum size of a template description in a cloud formation template | 1024.0 | Bytes | False | False |
| Module limit per account | 100.0 | None | True | False |
| Nested modules | 3.0 | None | False | False |
| Output count in CloudFormation template | 200.0 | None | False | False |
| Parameters declared in CloudFormation template. | 200.0 | None | False | False |
| Resource limit per account | 50.0 | None | True | False |
| Resources declared in a CloudFormation template | 500.0 | None | False | False |
| Size of Mapping attribute name | 255.0 | None | False | False |
| Size of a parameter value in cloud formation template | 4096.0 | None | False | False |
| Size of a resource name in cloud formation template | 255.0 | None | False | False |
| Size of a template body in S3 object for a ValidateStack request | 1.0 | Megabytes | False | False |
| Size of output name in CloudFormation template | 255.0 | None | False | False |
| Size of parameter name in CloudFormation template | 255.0 | None | False | False |
| Size of template body in CreateStack request | 51200.0 | Bytes | False | False |
| Stack count | 2000.0 | None | True | False |
| Stack instance operations per administrator account | 3500.0 | None | True | False |
| Stack instances per stack set | 2000.0 | None | True | False |
| Stack sets per administrator account | 100.0 | None | True | False |
| Version limit per module | 100.0 | None | True | False |
| Version limit per resource | 50.0 | None | True | False |
| cfn-signal wait condition data | 4096.0 | Bytes | False | False |

## AWS CloudHSM (AWS Service: cloudhsm)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Clusters per AWS Region and AWS account | 4.0 | None | True | False |
| HSMs per AWS Region and AWS account | 6.0 | None | True | False |
| HSMs per CloudHSM cluster | 28.0 | None | False | False |
| Keys per CloudHSM cluster | 3300.0 | None | False | False |
| Length of a Username | 31.0 | None | False | False |
| Length of a password | 32.0 | None | False | False |
| Minimum length of a password | 7.0 | None | False | False |
| Number of concurrent clients | 900.0 | None | False | False |
| Users per CloudHSM cluster | 1024.0 | None | False | False |

## AWS CloudTrail (AWS Service: cloudtrail)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Conditions across all advanced event selectors | 500.0 | None | False | False |
| Data resources across all event selectors in a trail | 250.0 | None | False | False |
| Event data stores per region | 5.0 | None | False | False |
| Event selectors | 5.0 | None | False | False |
| Event size | 256.0 | Kilobytes | False | False |
| Trails per region | 5.0 | None | False | False |
| Transactions per second (TPS) for all other APIs | 1.0 | None | False | False |
| Transactions per second (TPS) for the LookupEvents API | 2.0 | None | False | False |
| Transactions per second (TPS) for the get, describe, and list APIs | 10.0 | None | False | False |

## AWS CodeArtifact (AWS Service: codeartifact)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Asset file size maximum | 5.0 | Gigabytes | True | False |
| Assets per package version maximum | 100.0 | None | False | False |
| CopyPackageVersions maximum requests per second | 5.0 | None | True | False |
| Direct upstream repository maximum | 10.0 | None | False | False |
| Domains per AWS account maximum | 10.0 | None | True | False |
| GetAuthorizationToken maximum requests per second | 40.0 | None | True | False |
| GetPackageVersionAsset maximum requests per second | 50.0 | None | True | False |
| ListPackageVersionAssets maximum requests per second | 20.0 | None | True | False |
| ListPackageVersions maximum requests per second | 200.0 | None | True | False |
| ListPackages maximum requests per second | 200.0 | None | True | False |
| Maximum read requests per second from a single AWS account | 800.0 | None | True | False |
| Maximum requests per second using a single authentication token. | 800.0 | None | False | False |
| Maximum write requests per second from a single AWS account | 100.0 | None | True | False |
| Repositories per domain maximum | 1000.0 | None | True | False |
| Requests without authentication token per IP address maximum | 600.0 | None | False | False |
| Upstream repository search maximum | 25.0 | None | False | False |

## AWS CodeBuild (AWS Service: codebuild)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Associated tags per project | 50.0 | None | False | False |
| Build projects | 5000.0 | None | True | False |
| Build timeout in minutes | 480.0 | None | False | False |
| Concurrent request for information about builds | 100.0 | None | False | False |
| Concurrent requests for information on build projects | 100.0 | None | False | False |
| Concurrently running builds | 60.0 | None | True | False |
| Minimum period for build timeout in minutes | 5.0 | None | False | False |
| Security groups under VPC configuration | 5.0 | None | False | False |
| Subnets under VPC configuration | 16.0 | None | False | False |

## AWS CodeCommit (AWS Service: codecommit)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Allowed repositories | 1000.0 | None | True | False |

## AWS CodeDeploy (AWS Service: codedeploy)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| AWS Lambda deployment run in hours | 50.0 | None | False | False |
| Applications associated per account per region | 1000.0 | None | True | False |
| Auto Scaling groups in a deployment group | 10.0 | None | False | False |
| Concurrent deployments per account | 1000.0 | None | True | False |
| Concurrent deployments per deployment group | 1.0 | None | False | False |
| Custom deployment configurations per account | 50.0 | None | False | False |
| Deployment groups associated with a single application | 1000.0 | None | True | False |
| EC2/On-Premises blue/green deployment run in hours | 109.0 | None | False | False |
| EC2/On-Premises in-place deployment run in hours | 8.0 | None | False | False |
| Event notification triggers in a deployment group | 10.0 | None | True | False |
| GitHub connection tokens per account | 25.0 | None | False | False |
| Hours between the completion of a deployment and the termination of the original instances during an EC2/On-Premises blue/green deployment | 48.0 | None | False | False |
| Hours between the deployment of a revision and when traffic shifts to the replacement instances during an EC2/On-Premises blue/green deployment | 48.0 | None | False | False |
| Instances count per deployment | 1000.0 | None | True | False |
| Minutes a blue/green deployment can wait after a successful deployment before terminating instances from the original deployment | 2800.0 | None | False | False |
| Minutes between the first and last traffic shift during an AWS Lambda canary or linear deployment | 2880.0 | None | False | False |
| Minutes until a deployment fails if a lifecycle event doesn't start | 5.0 | None | False | False |
| Number of deployment groups that can be associated with an Amazon ECS service | 1.0 | None | False | False |
| Number of instances that can be passed to the BatchGetOnPremisesInstances API action | 100.0 | None | False | False |
| Number of instances used by concurrent deployments that are in progress per account | 1000.0 | None | True | False |
| Number of listeners for a traffic route during an Amazon ECS deployment | 1.0 | None | False | False |
| Seconds until a deployment lifecycle event fails if not completed | 3600.0 | Seconds | False | False |
| Size of deployment group name | 100.0 | None | False | False |
| Size of tag key | 128.0 | None | False | False |
| Size of tag value | 256.0 | None | False | False |
| Tags in a deployment group | 10.0 | None | False | False |
| Traffic that can be shifted in one increment during an AWS Lambda deployment | 99.0 | None | False | False |

## Amazon CodeGuru Profiler (AWS Service: codeguru-profiler)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Number of profiling groups per account and region. | 50.0 | None | True | False |

## Amazon CodeGuru Reviewer (AWS Service: codeguru-reviewer)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Allowed Code Reviews | 5000.0 | None | True | False |

## AWS CodePipeline (AWS Service: codepipeline)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| AWS CloudFormation action timeout | 3.0 | None | True | False |
| AWS CodeBuild action timeout | 8.0 | None | False | False |
| AWS CodeDeploy ECS (Blue/Green) action timeout | 5.0 | None | True | False |
| AWS CodeDeploy action timeout | 5.0 | None | True | False |
| AWS Lambda action timeout | 1.0 | None | True | False |
| Action configuration key length | 50.0 | None | False | False |
| Action configuration value length | 1000.0 | None | False | False |
| Action timeout | 1.0 | None | True | False |
| Amazon S3 deployment action timeout | 20.0 | None | True | False |
| Approval action timeout | 7.0 | None | False | False |
| Minimum actions | 1.0 | None | False | False |
| Minimum stages per pipeline | 2.0 | None | False | False |
| Total AWS CodeCommit or GitHub source artifact size | 1.0 | Gigabytes | False | False |
| Total Amazon S3 source artifact size | 3.0 | Gigabytes | False | False |
| Total JSON object size for Parameter Overrides | 1.0 | Kilobytes | False | False |
| Total actions per pipeline | 500.0 | None | False | False |
| Total actions per stage | 50.0 | None | False | False |
| Total custom actions | 50.0 | None | True | False |
| Total image definitions JSON file size | 100.0 | Kilobytes | False | False |
| Total input artifact size for AWS CloudFormation deployments | 256.0 | Megabytes | False | False |
| Total parallel actions per stage | 50.0 | None | False | False |
| Total period for execution history | 12.0 | None | False | False |
| Total pipelines | 1000.0 | None | True | False |
| Total pipelines with change detection set to periodically checking for source changes | 300.0 | None | False | False |
| Total sequential actions per stage | 50.0 | None | False | False |
| Total source artifact size for Amazon EBS deployments | 512.0 | Megabytes | False | False |
| Total stages per pipeline | 50.0 | None | False | False |
| Total webhooks | 300.0 | None | True | False |

## Amazon Cognito Federated Identities (AWS Service: cognito-identity)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Identity pool name size | 128.0 | Bytes | False | False |
| Identity pools per account | 1000.0 | None | True | False |
| List API call results | 60.0 | None | False | False |
| Login provider name size | 2048.0 | Bytes | False | False |
| Role-based access control rules | 25.0 | None | False | False |
| User pool providers per identity pool | 50.0 | None | True | False |

## Amazon Cognito User Pools (AWS Service: cognito-idp)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Apps per user pool | 1000.0 | None | True | False |
| Custom domains per account | 4.0 | None | False | False |
| Groups per user | 100.0 | None | False | False |
| Groups per user pool | 10000.0 | None | False | False |
| Identity providers per user pool | 300.0 | None | True | False |
| Rate of ClientAuthentication requests per account | 150.0 | None | False | False |
| Rate of UserAccountRecovery requests | 30.0 | None | False | False |
| Rate of UserAuthentication requests | 120.0 | None | True | False |
| Rate of UserCreation requests | 50.0 | None | True | False |
| Rate of UserFederation requests | 25.0 | None | True | False |
| Rate of UserList requests | 30.0 | None | False | False |
| Rate of UserPoolClientRead requests per account | 15.0 | None | False | False |
| Rate of UserPoolClientRead requests per user pool | 5.0 | None | False | False |
| Rate of UserPoolClientUpdate requests per account | 15.0 | None | False | False |
| Rate of UserPoolClientUpdate requests per user pool | 5.0 | None | False | False |
| Rate of UserPoolRead requests | 15.0 | None | False | False |
| Rate of UserPoolResourceRead requests per account | 20.0 | None | False | False |
| Rate of UserPoolResourceRead requests per user pool | 5.0 | None | False | False |
| Rate of UserPoolResourceUpdate requests per account | 15.0 | None | False | False |
| Rate of UserPoolResourceUpdate requests per user pool | 5.0 | None | False | False |
| Rate of UserPoolUpdate requests | 15.0 | None | False | False |
| Rate of UserRead requests | 120.0 | None | True | False |
| Rate of UserResourceRead requests | 50.0 | None | True | False |
| Rate of UserResourceUpdate requests | 25.0 | None | False | False |
| Rate of UserToken requests | 120.0 | None | True | False |
| Rate of UserUpdate requests | 25.0 | None | False | False |
| Resource servers per user pool | 25.0 | None | True | False |
| Scopes per resource server | 100.0 | None | False | False |
| User import jobs per user pool | 1000.0 | None | True | False |
| User pools per account | 1000.0 | None | True | False |

## Amazon Cognito Sync (AWS Service: cognito-sync)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Bulk publish wait time | 24.0 | None | False | False |
| Dataset name size | 128.0 | Bytes | False | False |
| Dataset size | 1.0 | Megabytes | True | False |
| Datasets per identity | 20.0 | None | True | False |
| Records per dataset | 1024.0 | None | True | False |

## Amazon Comprehend (AWS Service: comprehend)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| BatchDetectDominantLanguage throttle limit in transactions per second | 10.0 | None | True | False |
| BatchDetectEntities throttle limit in transactions per second | 10.0 | None | True | False |
| BatchDetectKeyPhrases throttle limit in transactions per second | 10.0 | None | True | False |
| BatchDetectSentiment throttle limit in transactions per second | 10.0 | None | True | False |
| BatchDetectSyntax throttle limit in transactions per second | 10.0 | None | True | False |
| CreateDocumentClassifier throttle limit in transactions per second | 1.0 | None | False | False |
| CreateEntityRecognizer throttle limit in transactions per second | 1.0 | None | False | False |
| DeleteDocumentClassifier throttle limit in transactions per second | 1.0 | None | False | False |
| DeleteEntityRecognizer throttle limit in transactions per second | 1.0 | None | False | False |
| DescribeDocumentClassificationJob throttle limit in transactions per second | 10.0 | None | False | False |
| DescribeDocumentClassifier throttle limit in transactions per second | 10.0 | None | False | False |
| DescribeDominantLanguageDetectionJob throttle limit in transactions per second | 10.0 | None | False | False |
| DescribeEntitiesDetectionJob throttle limit in transactions per second | 10.0 | None | False | False |
| DescribeEntityRecognizer throttle limit in transactions per second | 10.0 | None | False | False |
| DescribeEventsDetectionJob throttle limit in transactions per second | 10.0 | None | False | False |
| DescribeKeyPhrasesDetectionJob throttle limit in transactions per second | 10.0 | None | False | False |
| DescribePiiEntitiesDetectionJob throttle limit in transactions per second | 10.0 | None | False | False |
| DescribeSentimentDetectionJob throttle limit in transactions per second | 10.0 | None | False | False |
| DescribeTargetedSentimentDetectionJob throttle limit in transactions per second | 10.0 | None | False | False |
| DescribeTopicsDetectionJob throttle limit in transactions per second | 10.0 | None | False | False |
| DetectDominantLanguage max active jobs | 10.0 | None | False | False |
| DetectDominantLanguage throttle limit in transactions per second | 40.0 | None | True | False |
| DetectEntities max active jobs | 10.0 | None | False | False |
| DetectEntities throttle limit in transactions per second | 20.0 | None | True | False |
| DetectEvents max active jobs | 10.0 | None | False | False |
| DetectKeyPhrases max active jobs | 10.0 | None | False | False |
| DetectKeyPhrases throttle limit in transactions per second | 20.0 | None | True | False |
| DetectPiiEntities max active jobs | 10.0 | None | False | False |
| DetectPiiEntities throttle limit in transactions per second | 20.0 | None | True | False |
| DetectSentiment max active jobs | 10.0 | None | False | False |
| DetectSentiment throttle limit in transactions per second | 20.0 | None | True | False |
| DetectSyntax throttle limit in transactions per second | 20.0 | None | True | False |
| DetectTargetedSentiment max active jobs | 10.0 | None | False | False |
| DocumentClassification max active jobs | 10.0 | None | False | False |
| DocumentClassifier max active jobs | 10.0 | None | False | False |
| Endpoints max active endpoints | 10.0 | None | True | False |
| Endpoints max inference units per account | 100.0 | None | True | False |
| Endpoints max inference units per endpoint | 10.0 | None | True | False |
| EntityRecognizer max active jobs | 10.0 | None | False | False |
| ListDocumentClassificationJobs throttle limit in transactions per second | 10.0 | None | False | False |
| ListDocumentClassifiers throttle limit in transactions per second | 10.0 | None | False | False |
| ListDominantLanguageDetectionJobs throttle limit in transactions per second | 10.0 | None | False | False |
| ListEntitiesDetectionJobs throttle limit in transactions per second | 10.0 | None | False | False |
| ListEntityRecognizers throttle limit in transactions per second | 10.0 | None | False | False |
| ListEventsDetectionJobs throttle limit in transactions per second | 10.0 | None | False | False |
| ListKeyPhrasesDetectionJobs throttle limit in transactions per second | 10.0 | None | False | False |
| ListPiiEntitiesDetectionJobs throttle limit in transactions per second | 10.0 | None | False | False |
| ListSentimentDetectionJobs throttle limit in transactions per second | 10.0 | None | False | False |
| ListTagsForResource throttle limit in transactions per second | 10.0 | None | False | False |
| ListTargetedSentimentDetectionJobs throttle limit in transactions per second | 10.0 | None | False | False |
| ListTopicsDetectionJobs throttle limit in transactions per second | 10.0 | None | False | False |
| StartDocumentClassificationJob throttle limit in transactions per second | 1.0 | None | False | False |
| StartDominantLanguageDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StartEntitiesDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StartEventsDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StartKeyPhrasesDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StartPiiEntitiesDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StartSentimentDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StartTargetedSentimentDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StartTopicsDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StopDominantLanguageDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StopEntitiesDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StopEventsDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StopKeyPhrasesDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StopPiiEntitiesDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StopSentimentDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StopTargetedSentimentDetectionJob throttle limit in transactions per second | 1.0 | None | False | False |
| StopTrainingDocumentClassifier throttle limit in transactions per second | 1.0 | None | False | False |
| StopTrainingEntityRecognizer throttle limit in transactions per second | 1.0 | None | False | False |
| TagResource throttle limit in transactions per second | 1.0 | None | False | False |
| TopicsDetection max active jobs | 10.0 | None | False | False |
| UntagResource throttle limit in transactions per second | 1.0 | None | False | False |

## Amazon Comprehend Medical (AWS Service: comprehendmedical)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Characters per second (CPS) for the DetectEntities operation | 40000.0 | None | True | False |
| Characters per second (CPS) for the DetectEntities-v2 operation | 40000.0 | None | True | False |
| Characters per second (CPS) for the DetectPHI operation | 40000.0 | None | True | False |
| Characters per second (CPS) for the InferICD10CM operation | 40000.0 | None | True | False |
| Characters per second (CPS) for the InferRxNorm operation | 40000.0 | None | True | False |
| Maximum document size (UTF-8 characters) for the DetectEntities operation | 20000.0 | Bytes | False | False |
| Maximum document size (UTF-8 characters) for the DetectEntities-v2 operation | 20000.0 | Bytes | False | False |
| Maximum document size (UTF-8 characters) for the DetectPHI operation | 20000.0 | Bytes | False | False |
| Maximum document size (UTF-8 characters) for the InferICD10CM operation | 10000.0 | Bytes | False | False |
| Maximum document size (UTF-8 characters) for the InferRxNorm operation | 10000.0 | Bytes | False | False |
| Maximum individual file size for batch jobs | 40.0 | Kilobytes | False | False |
| Maximum number of files for batch jobs | 5000000.0 | None | False | False |
| Maximum size (in GB) of text analysis batch jobs (all files) | 10.0 | Gigabytes | False | False |
| Maximum size of ontology linking batch analysis jobs (all files) | 5.0 | Gigabytes | False | False |
| Minimum size of batch jobs (all files) | 1.0 | Bytes | False | False |
| Transactions per second (TPS) for the DescribeEntitiesDetectionV2Job operation | 10.0 | None | True | False |
| Transactions per second (TPS) for the DescribeICD10CMInferenceJob operation | 10.0 | None | True | False |
| Transactions per second (TPS) for the DescribePHIDetectionJob operation | 10.0 | None | True | False |
| Transactions per second (TPS) for the DescribeRxNormInferenceJob operation | 10.0 | None | True | False |
| Transactions per second (TPS) for the DetectEntities operation | 100.0 | None | False | False |
| Transactions per second (TPS) for the DetectEntities-v2 operation | 100.0 | None | False | False |
| Transactions per second (TPS) for the DetectPHI operation | 100.0 | None | False | False |
| Transactions per second (TPS) for the InferICD10CM operation | 100.0 | None | False | False |
| Transactions per second (TPS) for the InferRxNorm operation | 100.0 | None | False | False |
| Transactions per second (TPS) for the ListEntitiesDetectionV2Jobs operation | 10.0 | None | True | False |
| Transactions per second (TPS) for the ListICD10CMInferenceJobs operation | 10.0 | None | True | False |
| Transactions per second (TPS) for the ListPHIDetectionJobs operation | 10.0 | None | True | False |
| Transactions per second (TPS) for the ListRxNormInferenceJobs operation | 10.0 | None | True | False |
| Transactions per second (TPS) for the StartEntitiesDetectionV2Job operation | 5.0 | None | True | False |
| Transactions per second (TPS) for the StartICD10CMInferenceJob operation | 5.0 | None | True | False |
| Transactions per second (TPS) for the StartPHIDetectionJob operation | 5.0 | None | True | False |
| Transactions per second (TPS) for the StartRxNormInferenceJob operation | 5.0 | None | True | False |
| Transactions per second (TPS) for the StopEntitiesDetectionV2Job operation | 5.0 | None | True | False |
| Transactions per second (TPS) for the StopICD10CMInferenceJob operation | 5.0 | None | True | False |
| Transactions per second (TPS) for the StopPHIDetectionJob operation | 5.0 | None | True | False |
| Transactions per second (TPS) for the StopRxNormInferenceJob operation | 5.0 | None | True | False |

## Amazon Connect (AWS Service: connect)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| AWS Lambda functions per instance | 50.0 | None | True | False |
| Agent status per instance | 50.0 | None | False | False |
| Amazon Connect instance count | 2.0 | None | True | False |
| Amazon Lex V2 bot aliases per instance | 100.0 | None | True | False |
| Amazon Lex bots per instance | 70.0 | None | True | False |
| Concurrent active calls per instance | 10.0 | None | True | False |
| Concurrent active chats per instance | 100.0 | None | True | False |
| Concurrent active tasks per instance | 2500.0 | None | True | False |
| Contact flows per instance | 100.0 | None | True | False |
| Hours of operation per instance | 100.0 | None | True | False |
| Phone numbers per instance | 5.0 | None | True | False |
| Prompts per instance | 500.0 | None | True | False |
| Queues per instance | 50.0 | None | True | False |
| Queues per routing profile per instance | 50.0 | None | True | False |
| Quick connects per instance | 100.0 | None | True | False |
| Rate of AssociateQueueQuickConnects API requests | 2.0 | None | True | False |
| Rate of AssociateRoutingProfileQueues API requests | 2.0 | None | True | False |
| Rate of CreateQueue API requests | 2.0 | None | True | False |
| Rate of CreateQuickConnect API requests | 2.0 | None | True | False |
| Rate of CreateRoutingProfile API requests | 2.0 | None | True | False |
| Rate of CreateUser API requests | 2.0 | None | True | False |
| Rate of CreateUserHierarchyGroup API requests | 2.0 | None | True | False |
| Rate of DeleteQuickConnect API requests | 2.0 | None | True | False |
| Rate of DeleteUser API requests | 2.0 | None | True | False |
| Rate of DeleteUserHierarchyGroup API requests | 2.0 | None | True | False |
| Rate of DescribeHoursOfOperation API requests | 2.0 | None | True | False |
| Rate of DescribeQueue API requests | 2.0 | None | True | False |
| Rate of DescribeQuickConnect API requests | 2.0 | None | True | False |
| Rate of DescribeRoutingProfile API requests | 2.0 | None | True | False |
| Rate of DescribeUser API requests | 2.0 | None | True | False |
| Rate of DescribeUserHierarchyGroup API requests | 2.0 | None | True | False |
| Rate of DescribeUserHierarchyStructure API requests | 2.0 | None | True | False |
| Rate of DisassociateQueueQuickConnects API requests | 2.0 | None | True | False |
| Rate of DisassociateRoutingProfileQueues API requests | 2.0 | None | True | False |
| Rate of GetContactAttributes API requests | 2.0 | None | True | False |
| Rate of GetCurrentMetricData API requests | 5.0 | None | True | False |
| Rate of GetFederationToken API requests | 2.0 | None | True | False |
| Rate of GetMetricData API requests | 5.0 | None | True | False |
| Rate of ListContactFlows API requests | 2.0 | None | True | False |
| Rate of ListHoursOfOperations API requests | 2.0 | None | True | False |
| Rate of ListPhoneNumbers API requests | 2.0 | None | True | False |
| Rate of ListQueueQuickConnects API requests | 2.0 | None | True | False |
| Rate of ListQueues API requests | 2.0 | None | True | False |
| Rate of ListQuickConnects API requests | 2.0 | None | True | False |
| Rate of ListRoutingProfileQueues API requests | 2.0 | None | True | False |
| Rate of ListRoutingProfiles API requests | 2.0 | None | True | False |
| Rate of ListSecurityProfiles API requests | 2.0 | None | True | False |
| Rate of ListTagsForResource API requests | 2.0 | None | True | False |
| Rate of ListUserHierarchyGroups API requests | 2.0 | None | True | False |
| Rate of ListUsers API requests | 2.0 | None | True | False |
| Rate of StartOutboundVoiceContact API requests | 2.0 | None | True | False |
| Rate of StopContact API requests | 2.0 | None | True | False |
| Rate of TagResource API requests | 2.0 | None | True | False |
| Rate of UntagResource API requests | 2.0 | None | True | False |
| Rate of UpdateContactAttributes API requests | 2.0 | None | True | False |
| Rate of UpdateQueueHoursOfOperation API requests | 2.0 | None | True | False |
| Rate of UpdateQueueMaxContacts API requests | 2.0 | None | True | False |
| Rate of UpdateQueueName API requests | 2.0 | None | True | False |
| Rate of UpdateQueueOutboundCallerConfig API requests | 2.0 | None | True | False |
| Rate of UpdateQueueStatus API requests | 2.0 | None | True | False |
| Rate of UpdateQuickConnectConfig API requests | 2.0 | None | True | False |
| Rate of UpdateQuickConnectName API requests | 2.0 | None | True | False |
| Rate of UpdateRoutingProfileConcurrency API requests | 2.0 | None | True | False |
| Rate of UpdateRoutingProfileDefaultOutboundQueue API requests | 2.0 | None | True | False |
| Rate of UpdateRoutingProfileName API requests | 2.0 | None | True | False |
| Rate of UpdateRoutingProfileQueues API requests | 2.0 | None | True | False |
| Rate of UpdateUserHierarchy API requests | 2.0 | None | True | False |
| Rate of UpdateUserHierarchyGroupName API requests | 2.0 | None | True | False |
| Rate of UpdateUserIdentityInfo API requests | 2.0 | None | True | False |
| Rate of UpdateUserPhoneConfig API requests | 2.0 | None | True | False |
| Rate of UpdateUserRoutingProfile API requests | 2.0 | None | True | False |
| Rate of UpdateUserSecurityProfiles API requests | 2.0 | None | True | False |
| Reports per instance | 500.0 | None | True | False |
| Routing profiles per instance | 100.0 | None | True | False |
| Scheduled reports per instance | 50.0 | None | True | False |
| Security profiles per instance | 100.0 | None | True | False |
| User hierarchy groups per instance | 500.0 | None | True | False |
| Users per instance | 500.0 | None | True | False |

## Amazon Connect High-Volume Outbound Communications (AWS Service: connect-campaigns)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Amazon Connect High-Volume Outbound Communications campaign count | 25.0 | None | True | False |

## AWS Glue DataBrew (AWS Service: databrew)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Concurrent jobs per AWS account | 10.0 | None | True | False |
| Datasets per AWS account | 100.0 | None | True | False |
| Jobs per AWS account | 100.0 | None | True | False |
| Node capacity per AWS account | 300.0 | None | True | False |
| Open projects per AWS account | 10.0 | None | True | False |
| Projects per AWS account | 100.0 | None | True | False |
| Recipes per AWS account | 100.0 | None | True | False |
| Rules per ruleset | 100.0 | None | True | False |
| Rulesets per AWS account | 100.0 | None | True | False |
| Rulesets per dataset | 10.0 | None | True | False |
| Schedules per AWS account | 10.0 | None | True | False |
| Versions per recipe | 100.0 | None | True | False |

## AWS Data Exchange (AWS Service: dataexchange)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Amazon API Gateway API assets per revision | 20.0 | None | True | False |
| Amazon Redshift datashare assets per import job from Redshift | 10.0 | None | False | False |
| Amazon Redshift datashare assets per revision | 20.0 | None | True | False |
| Asset per export job from Amazon S3 | 100.0 | None | False | False |
| Asset size in GB | 100.0 | Gigabytes | False | False |
| Assets per import job from Amazon S3 | 100.0 | None | False | False |
| Assets per revision | 10000.0 | None | True | False |
| Auto export event actions per data set | 5.0 | None | True | False |
| Concurrent in progress jobs to export assets to Amazon S3 | 10.0 | None | False | False |
| Concurrent in progress jobs to export assets to a signed URL | 10.0 | None | False | False |
| Concurrent in progress jobs to export revisions to Amazon S3 | 5.0 | None | False | False |
| Concurrent in progress jobs to import assets from Amazon API Gateway | 10.0 | None | False | False |
| Concurrent in progress jobs to import assets from Amazon Redshift datashares | 10.0 | None | False | False |
| Concurrent in progress jobs to import assets from Amazon S3 | 10.0 | None | False | False |
| Concurrent in progress jobs to import assets from a signed URL | 10.0 | None | False | False |
| Data sets per account | 3000.0 | None | True | False |
| Event actions per account | 50.0 | None | True | False |
| Products per data set | 100.0 | None | True | False |
| Revisions per Amazon API Gateway API data set | 20.0 | None | True | False |
| Revisions per Amazon Redshift datashare data set | 20.0 | None | True | False |
| Revisions per addRevisions change set | 5.0 | None | False | False |
| Revisions per data set | 10000.0 | None | True | False |

## AWS DataSync (AWS Service: datasync)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Files per task | 25000000.0 | None | True | False |
| Tasks | 100.0 | None | True | False |
| Throughput per task | 10.0 | Gigabits | True | False |

## Amazon DynamoDB Accelerator (DAX) (AWS Service: dax)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Nodes per cluster | 11.0 | None | False | False |
| Parameter groups | 20.0 | None | False | False |
| Subnet groups | 50.0 | None | False | False |
| Subnets per subnet group | 20.0 | None | False | False |
| Total number of nodes | 50.0 | None | True | False |

## AWS Application Discovery Service (AWS Service: discovery)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Active agents sending data to the service | 1000.0 | None | False | False |
| Applications per account | 1000.0 | None | False | False |
| Deletions of import records per day | 25000.0 | None | False | False |
| Imported server records per account | 25000.0 | None | False | False |
| Imported servers per account | 10000.0 | None | True | False |
| Inactive agents heartbeating but not collecting data | 10000.0 | None | False | False |
| Servers per application | 400.0 | None | False | False |
| Tags per server | 30.0 | None | False | False |

## Amazon Data Lifecycle Manager (AWS Service: dlm)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Policies per Region | 100.0 | None | True | False |
| Target accounts per sharing rule | 50.0 | None | True | False |

## AWS Database Migration Service (AWS DMS) (AWS Service: dms)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Certificate count | 100.0 | None | True | False |
| Endpoint count | 1000.0 | None | True | False |
| Endpoints per instance | 100.0 | None | True | False |
| Event subscriptions | 60.0 | None | True | False |
| Replication instances | 60.0 | None | True | False |
| Subnet groups | 60.0 | None | True | False |
| Subnets per subnet group | 60.0 | None | True | False |
| Task count | 600.0 | None | True | False |
| Total storage | 30000.0 | Gigabytes | True | False |

## Amazon DocumentDB (with MongoDB compatibility) (AWS Service: docdb)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Cluster parameter groups | 50.0 | None | False | False |
| Clusters | 40.0 | None | True | False |
| Event subscriptions | 20.0 | None | True | False |
| Instances | 40.0 | None | True | False |
| Manual cluster snapshots | 100.0 | None | True | False |
| Read replicas per cluster | 15.0 | None | True | False |
| Subnet groups | 50.0 | None | True | False |
| Subnets per subnet group | 20.0 | None | False | False |
| Tags per resource | 50.0 | None | False | False |
| VPC security groups per instance | 5.0 | None | False | False |

## ElasticDisasterRecovery (AWS Service: drs)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Concurrent jobs in progress | 20.0 | None | False | False |
| Max Total replicating source servers Per AWS Account | 300.0 | None | True | False |
| Max Total source servers Per AWS Account | 3000.0 | None | True | False |
| Max concurrent Jobs per source server | 1.0 | None | False | False |
| Max source servers in a single Job | 200.0 | None | False | False |
| Max source servers in all Jobs | 200.0 | None | False | False |

## AWS Directory Service (AWS Service: ds)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| AD Connector directories | 10.0 | None | True | False |
| AWS Managed Microsoft AD directories | 20.0 | None | True | False |
| AWS Managed Microsoft AD domain controllers | 20.0 | None | True | False |
| AWS Managed Microsoft AD manual snapshots | 5.0 | None | False | False |

## Amazon DynamoDB (AWS Service: dynamodb)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Account-level read throughput limit (Provisioned mode) | 80000.0 | None | True | False |
| Account-level write throughput limit (Provisioned mode) | 80000.0 | None | True | False |
| Concurrent control plane operations | 500.0 | None | True | False |
| Global Secondary Indexes per table | 20.0 | None | True | False |
| Maximum number of tables | 2500.0 | None | True | False |
| Provisioned capacity decreases per day | 27.0 | None | True | False |
| Table-level read throughput limit | 40000.0 | None | True | False |
| Table-level write throughput limit | 40000.0 | None | True | False |
| Write throughput limit for DynamoDB Streams (Provisioned mode) | 10000.0 | None | True | False |

## Amazon Elastic Block Store (Amazon EBS) (AWS Service: ebs)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Archived snapshots per volume | 25.0 | None | True | False |
| CompleteSnapshot requests per account | 10.0 | None | False | False |
| Concurrent snapshot copies per destination Region | 20.0 | None | False | False |
| Concurrent snapshots per Cold HDD (sc1) volume | 1.0 | None | False | False |
| Concurrent snapshots per General Purpose SSD (gp2) volume | 5.0 | None | False | False |
| Concurrent snapshots per General Purpose SSD (gp3) volume | 5.0 | None | False | False |
| Concurrent snapshots per Magnetic (standard) volume | 5.0 | None | False | False |
| Concurrent snapshots per Provisioned IOPS SSD (io1) volume | 5.0 | None | False | False |
| Concurrent snapshots per Provisioned IOPS SSD (io2) volume | 5.0 | None | False | False |
| Concurrent snapshots per Throughput Optimized HDD (st1) volume | 1.0 | None | False | False |
| Fast snapshot restore | 50.0 | None | True | False |
| GetSnapshotBlock requests per account | 1000.0 | None | True | False |
| GetSnapshotBlock requests per snapshot | 1000.0 | None | False | False |
| IOPS for Provisioned IOPS SSD (io1) volumes | 300000.0 | None | True | False |
| IOPS for Provisioned IOPS SSD (io2) volumes | 100000.0 | None | True | False |
| IOPS modifications for Provisioned IOPS SSD (io1) volumes | 500000.0 | None | True | False |
| IOPS modifications for Provisioned IOPS SSD (io2) volumes | 100000.0 | None | True | False |
| In-progress snapshot archives per account | 5.0 | None | True | False |
| In-progress snapshot restores from archive per account | 5.0 | None | True | False |
| ListChangedBlocks requests per account | 50.0 | None | False | False |
| ListSnapshotBlocks requests per account | 50.0 | None | False | False |
| Pending snapshots per account | 100.0 | None | False | False |
| PutSnapshotBlock requests per account | 1000.0 | None | True | False |
| PutSnapshotBlock requests per snapshot | 1000.0 | None | False | False |
| Snapshots per Region | 100000.0 | None | True | False |
| StartSnapshot requests per account | 10.0 | None | False | False |
| Storage for Cold HDD (sc1) volumes, in TiB | 50.0 | None | True | False |
| Storage for General Purpose SSD (gp2) volumes, in TiB | 50.0 | None | True | False |
| Storage for General Purpose SSD (gp3) volumes, in TiB | 50.0 | None | True | False |
| Storage for Magnetic (standard) volumes, in TiB | 50.0 | None | True | False |
| Storage for Provisioned IOPS SSD (io1) volumes, in TiB | 50.0 | None | True | False |
| Storage for Provisioned IOPS SSD (io2) volumes, in TiB | 20.0 | None | True | False |
| Storage for Throughput Optimized HDD (st1) volumes, in TiB | 50.0 | None | True | False |
| Storage modifications for Cold HDD (sc1) volumes, in TiB | 500.0 | None | True | False |
| Storage modifications for General Purpose SSD (gp2) volumes, in TiB | 500.0 | None | True | False |
| Storage modifications for General Purpose SSD (gp3) volumes, in TiB | 500.0 | None | True | False |
| Storage modifications for Magnetic (standard) volumes, in TiB | 500.0 | None | True | False |
| Storage modifications for Provisioned IOPS SSD (io1) volumes, in TiB | 500.0 | None | True | False |
| Storage modifications for Provisioned IOPS SSD (io2) volumes, in TiB | 20.0 | None | True | False |
| Storage modifications for Throughput Optimized HDD (st1) volumes, in TiB | 500.0 | None | True | False |

## Amazon Elastic Compute Cloud (Amazon EC2) (AWS Service: ec2)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| All DL Spot Instance Requests | 0.0 | None | True | False |
| All F Spot Instance Requests | 0.0 | None | True | False |
| All G and VT Spot Instance Requests | 0.0 | None | True | False |
| All Inf Spot Instance Requests | 0.0 | None | True | False |
| All P Spot Instance Requests | 0.0 | None | True | False |
| All Standard (A, C, D, H, I, M, R, T, Z) Spot Instance Requests | 5.0 | None | True | False |
| All X Spot Instance Requests | 0.0 | None | True | False |
| Amazon FPGA images (AFIs) | 100.0 | None | True | False |
| Attachments per VPC | 5.0 | None | False | False |
| Attachments per transit gateway | 5000.0 | None | True | False |
| Authorization rules per Client VPN endpoint | 50.0 | None | True | False |
| Client VPN endpoints per Region | 5.0 | None | True | False |
| Concurrent client connections per Client VPN endpoint | 20000.0 | None | True | False |
| Concurrent operations per Client VPN endpoint | 10.0 | None | False | False |
| Customer gateways per region | 50.0 | None | True | False |
| Direct Connect gateways per transit gateway | 20.0 | None | False | False |
| Dynamic routes advertised from CGW to VPN connection | 100.0 | None | False | False |
| EC2-VPC Elastic IPs | 5.0 | None | True | False |
| Entries in a client certificate revocation list for Client VPN endpoints | 20000.0 | None | False | False |
| Members per transit gateway multicast group | 100.0 | None | True | False |
| Multicast Network Interfaces per transit gateway | 1000.0 | None | True | False |
| Multicast domain associations per VPC | 20.0 | None | True | False |
| Multicast domains per transit gateway | 20.0 | None | True | False |
| New Reserved Instances per month | 20.0 | None | True | False |
| Peering attachments per transit gateway | 50.0 | None | True | False |
| Pending peering attachments per transit gateway | 10.0 | None | True | False |
| Route Tables per transit gateway | 20.0 | None | True | False |
| Routes advertised from VPN connection to CGW | 1000.0 | None | False | False |
| Routes per Client VPN endpoint | 10.0 | None | True | False |
| Routes per transit gateway | 10000.0 | None | True | False |
| Running Dedicated c4 Hosts | 0.0 | None | True | False |
| Running Dedicated c5 Hosts | 0.0 | None | True | False |
| Running Dedicated c5a Hosts | 0.0 | None | True | False |
| Running Dedicated c5d Hosts | 0.0 | None | True | False |
| Running Dedicated c5n Hosts | 0.0 | None | True | False |
| Running Dedicated c6g Hosts | 0.0 | None | True | False |
| Running Dedicated c6gd Hosts | 0.0 | None | True | False |
| Running Dedicated c6gn Hosts | 0.0 | None | True | False |
| Running Dedicated c6i Hosts | 0.0 | None | True | False |
| Running Dedicated d2 Hosts | 0.0 | None | True | False |
| Running Dedicated f1 Hosts | 0.0 | None | True | False |
| Running Dedicated g3 Hosts | 0.0 | None | True | False |
| Running Dedicated g3s Hosts | 0.0 | None | True | False |
| Running Dedicated g4ad Hosts | 0.0 | None | True | False |
| Running Dedicated g4dn Hosts | 0.0 | None | True | False |
| Running Dedicated g5 Hosts | 0.0 | None | True | False |
| Running Dedicated i3 Hosts | 0.0 | None | True | False |
| Running Dedicated i3en Hosts | 0.0 | None | True | False |
| Running Dedicated i4i Hosts | 0.0 | None | True | False |
| Running Dedicated inf Hosts | 0.0 | None | True | False |
| Running Dedicated m4 Hosts | 0.0 | None | True | False |
| Running Dedicated m5 Hosts | 0.0 | None | True | False |
| Running Dedicated m5a Hosts | 0.0 | None | True | False |
| Running Dedicated m5ad Hosts | 0.0 | None | True | False |
| Running Dedicated m5d Hosts | 0.0 | None | True | False |
| Running Dedicated m6g Hosts | 0.0 | None | True | False |
| Running Dedicated m6gd Hosts | 0.0 | None | True | False |
| Running Dedicated m6i Hosts | 0.0 | None | True | False |
| Running Dedicated mac1 Hosts | 0.0 | None | True | False |
| Running Dedicated p3 Hosts | 0.0 | None | True | False |
| Running Dedicated r4 Hosts | 0.0 | None | True | False |
| Running Dedicated r5 Hosts | 0.0 | None | True | False |
| Running Dedicated r5a Hosts | 0.0 | None | True | False |
| Running Dedicated r5ad Hosts | 0.0 | None | True | False |
| Running Dedicated r5b Hosts | 0.0 | None | True | False |
| Running Dedicated r5d Hosts | 0.0 | None | True | False |
| Running Dedicated r5n Hosts | 0.0 | None | True | False |
| Running Dedicated r6g Hosts | 0.0 | None | True | False |
| Running Dedicated r6i Hosts | 0.0 | None | True | False |
| Running Dedicated t3 Hosts | 0.0 | None | True | False |
| Running Dedicated x1 Hosts | 0.0 | None | True | False |
| Running Dedicated x2idn Hosts | 0.0 | None | True | False |
| Running Dedicated x2iedn Hosts | 0.0 | None | True | False |
| Running Dedicated z1d Hosts | 0.0 | None | True | False |
| Running On-Demand DL instances | 0.0 | None | True | False |
| Running On-Demand F instances | 0.0 | None | True | False |
| Running On-Demand G and VT instances | 0.0 | None | True | False |
| Running On-Demand High Memory instances | 0.0 | None | True | False |
| Running On-Demand Inf instances | 0.0 | None | True | False |
| Running On-Demand P instances | 0.0 | None | True | False |
| Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances | 5.0 | None | True | False |
| Running On-Demand X instances | 0.0 | None | True | False |
| Sources per transit gateway multicast group | 1.0 | None | True | False |
| Transit gateways per Direct Connect Gateway | 3.0 | None | False | False |
| Transit gateways per account | 5.0 | None | True | False |
| VPC Attachment Bandwidth | 50.0 | Gigabits | False | False |
| VPN connections per VGW | 10.0 | None | True | False |
| VPN connections per region | 50.0 | None | True | False |
| Virtual private gateways per region | 5.0 | None | True | False |

## IPAM (AWS Service: ec2-ipam)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| CIDRs per IPAM pool | 50.0 | None | True | False |
| IPAM pool depth | 10.0 | None | True | False |
| IPAMs per Region | 1.0 | None | False | False |
| Pools per IPAM scope | 50.0 | None | True | False |
| Scopes per IPAM | 5.0 | None | True | False |

## EC2 Fast Launch (AWS Service: ec2fastlaunch)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Parallel instance launches | 40.0 | None | True | False |

## Amazon Elastic Container Registry (Amazon ECR) (AWS Service: ecr)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Filters per rule in a replication configuration | 100.0 | None | False | False |
| Images per repository | 10000.0 | None | True | False |
| Layer parts | 4200.0 | None | False | False |
| Lifecycle policy length | 30720.0 | None | False | False |
| Maximum layer part size | 10.0 | None | False | False |
| Maximum layer size | 42000.0 | None | False | False |
| Minimum layer part size | 5.0 | None | False | False |
| Rate of BatchCheckLayerAvailability requests | 1000.0 | None | True | False |
| Rate of BatchGetImage requests | 2000.0 | None | True | False |
| Rate of CompleteLayerUpload requests | 100.0 | None | True | False |
| Rate of GetAuthorizationToken requests | 500.0 | None | True | False |
| Rate of GetDownloadUrlForLayer requests | 3000.0 | None | True | False |
| Rate of InitiateLayerUpload requests | 100.0 | None | True | False |
| Rate of PutImage requests | 10.0 | None | True | False |
| Rate of UploadLayerPart requests | 500.0 | None | True | False |
| Rate of image scans | 1.0 | None | False | False |
| Registered repositories | 10000.0 | None | True | False |
| Rules per lifecycle policy | 50.0 | None | False | False |
| Rules per replication configuration | 10.0 | None | False | False |
| Tags per image | 1000.0 | None | False | False |
| Unique destinations across all rules in a replication configuration | 25.0 | None | False | False |

## Amazon Elastic Container Service (Amazon ECS) (AWS Service: ecs)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Capacity providers per cluster | 10.0 | None | False | False |
| Classic Load Balancers per service | 1.0 | None | False | False |
| Clusters per account | 10000.0 | None | True | False |
| Container instances per cluster | 5000.0 | None | False | False |
| Container instances per start-task | 10.0 | None | False | False |
| Containers per task definition | 10.0 | None | False | False |
| ECS Exec sessions | 20.0 | None | True | False |
| Rate of tasks launched by a service on AWS Fargate | 500.0 | None | True | False |
| Rate of tasks launched by a service on an Amazon EC2 or External instance | 500.0 | None | True | False |
| Revisions per task definition family | 1000000.0 | None | False | False |
| Security groups per awsvpcConfiguration | 5.0 | None | False | False |
| Services per cluster | 5000.0 | None | True | False |
| Subnets per awsvpcConfiguration | 16.0 | None | False | False |
| Tags per resource | 50.0 | None | False | False |
| Target groups per service | 5.0 | None | False | False |
| Task definition size | 64.0 | Kilobytes | False | False |
| Tasks in PROVISIONING state per cluster | 300.0 | None | False | False |
| Tasks launched per run-task | 10.0 | None | False | False |
| Tasks per service | 5000.0 | None | True | False |

## Amazon Elastic Kubernetes Service (Amazon EKS) (AWS Service: eks)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Clusters | 100.0 | None | True | False |
| Control plane security groups per cluster | 4.0 | None | False | False |
| Fargate profiles per cluster | 10.0 | None | True | False |
| Label pairs per Fargate profile selector | 5.0 | None | True | False |
| Managed node groups per cluster | 30.0 | None | True | False |
| Nodes per managed node group | 450.0 | None | True | False |
| Public endpoint access CIDR ranges per cluster | 40.0 | None | False | False |
| Registered clusters | 10.0 | None | True | False |
| Selectors per Fargate profile | 5.0 | None | True | False |

## Amazon ElastiCache (AWS Service: elasticache)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Nodes per Region | 300.0 | None | True | False |
| Nodes per cluster (Memcached) | 40.0 | None | True | False |
| Nodes per cluster per instance type (Redis cluster mode enabled) | 90.0 | None | True | False |
| Nodes per shard (Redis) | 6.0 | None | False | False |
| Parameter groups per Region | 150.0 | None | True | False |
| Security groups per Region | 50.0 | None | True | False |
| Shards per cluster (Redis cluster mode disabled) | 1.0 | None | False | False |
| Subnet groups per Region | 150.0 | None | True | False |
| Subnets per subnet group | 20.0 | None | True | False |

## AWS Elastic Beanstalk (AWS Service: elasticbeanstalk)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Application versions | 1000.0 | None | True | False |
| Applications | 75.0 | None | True | False |
| Configuration templates | 2000.0 | None | True | False |
| Custom platform versions | 50.0 | None | True | False |
| Environments | 200.0 | None | True | False |

## Amazon Elastic File System (EFS) (AWS Service: elasticfilesystem)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Active users per NFS client | 128.0 | None | False | False |
| Bursting throughput | 1024.0 | Megabytes | False | False |
| Directory depth | 1000.0 | None | False | False |
| EFS file locks | 512.0 | None | False | False |
| File hard links | 177.0 | None | False | False |
| File size | 52673613135872.0 | Bytes | False | False |
| File system name length | 255.0 | Bytes | False | False |
| File system symbolic link (symlink) length | 4080.0 | Bytes | False | False |
| File systems per account | 1000.0 | None | True | False |
| Locks across unique file/process pairs | 65536.0 | None | False | False |
| Minimum wait time between Provisioned Throughput decreases | 86400.0 | Seconds | False | False |
| Minimum wait time between Throughput mode changes | 86400.0 | Seconds | False | False |
| Mount targets per Availability Zone | 1.0 | None | False | False |
| Mount targets per VPC | 400.0 | None | False | False |
| Open files per NFS client | 32768.0 | None | False | False |
| Provisioned throughput | 1024.0 | Megabytes | False | False |
| Rate of file system operations | 35000.0 | None | False | False |
| Security groups per mount target | 5.0 | None | False | False |
| Tags | 50.0 | None | False | False |
| Throughput per NFS client | 524.288 | Megabytes | False | False |
| VPCs per file system | 1.0 | None | False | False |

## Elastic Load Balancing (ELB) (AWS Service: elasticloadbalancing)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Application Load Balancers per Region | 50.0 | None | True | False |
| Certificates per Application Load Balancer | 25.0 | None | True | False |
| Certificates per Network Load Balancer | 25.0 | None | True | False |
| Classic Load Balancers per Region | 20.0 | None | True | False |
| Condition Values per Rule | 5.0 | None | False | False |
| Condition Wildcards per Rule | 5.0 | None | False | False |
| Listeners per Application Load Balancer | 50.0 | None | True | False |
| Listeners per Classic Load Balancer | 100.0 | None | True | False |
| Listeners per Network Load Balancer | 50.0 | None | False | False |
| Network Load Balancer ENIs per VPC | 1200.0 | None | True | False |
| Network Load Balancers per Region | 50.0 | None | True | False |
| Number of times a target can be registered per Application Load Balancer | 1000.0 | None | False | False |
| Registered Instances per Classic Load Balancer | 1000.0 | None | True | False |
| Rules per Application Load Balancer | 100.0 | None | True | False |
| Target Groups per Action per Application Load Balancer | 5.0 | None | False | False |
| Target Groups per Action per Network Load Balancer | 1.0 | None | False | False |
| Target Groups per Application Load Balancer | 100.0 | None | False | False |
| Target Groups per Region | 3000.0 | None | True | False |
| Targets per Application Load Balancer | 1000.0 | None | True | False |
| Targets per Availability Zone per Network Load Balancer | 500.0 | None | True | False |
| Targets per Network Load Balancer | 3000.0 | None | True | False |
| Targets per Target Group per Region | 1000.0 | None | True | False |

## Amazon EMR (AWS Service: elasticmapreduce)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Replenishment rate of AddInstanceFleet calls | 0.5 | None | True | False |
| Replenishment rate of AddInstanceGroups calls | 0.2 | None | True | False |
| Replenishment rate of AddJobFlowSteps calls | 0.5 | None | True | False |
| Replenishment rate of AddTags calls | 0.5 | None | True | False |
| Replenishment rate of CancelSteps calls | 0.5 | None | True | False |
| Replenishment rate of CreateSecurityConfiguration calls | 0.5 | None | True | False |
| Replenishment rate of DeleteSecurityConfiguration calls | 0.5 | None | True | False |
| Replenishment rate of DescribeCluster calls | 1.0 | None | True | False |
| Replenishment rate of DescribeJobFlows calls | 0.2 | None | True | False |
| Replenishment rate of DescribeSecurityConfiguration calls | 0.5 | None | True | False |
| Replenishment rate of DescribeStep calls | 0.5 | None | True | False |
| Replenishment rate of ListBootstrapActions calls | 1.0 | None | True | False |
| Replenishment rate of ListClusters calls | 0.5 | None | True | False |
| Replenishment rate of ListInstanceFleets calls | 0.5 | None | True | False |
| Replenishment rate of ListInstanceGroups calls | 1.0 | None | True | False |
| Replenishment rate of ListInstances calls | 0.5 | None | True | False |
| Replenishment rate of ListSecurityConfigurations calls | 0.5 | None | True | False |
| Replenishment rate of ListSteps calls | 0.5 | None | True | False |
| Replenishment rate of ModifyCluster calls | 0.5 | None | True | False |
| Replenishment rate of ModifyInstanceFleet calls | 0.5 | None | True | False |
| Replenishment rate of ModifyInstanceGroups calls | 0.5 | None | True | False |
| Replenishment rate of PutAutoScalingPolicy calls | 0.5 | None | True | False |
| Replenishment rate of RemoveAutoScalingPolicy calls | 0.5 | None | True | False |
| Replenishment rate of RemoveTags calls | 0.5 | None | True | False |
| Replenishment rate of RunJobFlow calls | 0.5 | None | True | False |
| Replenishment rate of SetTerminationProtection calls | 0.2 | None | True | False |
| Replenishment rate of SetVisibleToAllUsers calls | 0.2 | None | True | False |
| Replenishment rate of TerminateJobFlows calls | 0.5 | None | True | False |
| The maximum number of API requests that you can make per second. | 25.0 | None | True | False |
| The maximum number of AddInstanceFleet API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of AddInstanceGroups API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of AddJobFlowSteps API requests that you can make per second. | 10.0 | None | True | False |
| The maximum number of AddTags API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of CancelSteps API requests that you can make per second. | 10.0 | None | True | False |
| The maximum number of CreateSecurityConfiguration API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of DeleteSecurityConfiguration API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of DescribeCluster API requests that you can make per second. | 10.0 | None | True | False |
| The maximum number of DescribeJobFlows API requests that you can make per second. | 20.0 | None | True | False |
| The maximum number of DescribeSecurityConfiguration API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of DescribeStep API requests that you can make per second. | 10.0 | None | True | False |
| The maximum number of ListBootstrapActions API requests that you can make per second. | 10.0 | None | True | False |
| The maximum number of ListClusters API requests that you can make per second. | 20.0 | None | True | False |
| The maximum number of ListInstanceFleets API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of ListInstanceGroups API requests that you can make per second. | 10.0 | None | True | False |
| The maximum number of ListInstances API requests that you can make per second. | 10.0 | None | True | False |
| The maximum number of ListSecurityConfigurations API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of ListSteps API requests that you can make per second. | 10.0 | None | True | False |
| The maximum number of ModifyCluster API requests that you can make per second. | 10.0 | None | True | False |
| The maximum number of ModifyInstanceFleet API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of ModifyInstanceGroups API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of PutAutoScalingPolicy API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of RemoveAutoScalingPolicy API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of RemoveTags API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of RunJobFlow API requests that you can make per second. | 10.0 | None | True | False |
| The maximum number of SetTerminationProtection API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of SetVisibileToAllUsers API requests that you can make per second. | 5.0 | None | True | False |
| The maximum number of TerminateJobFlows API requests that you can make per second. | 10.0 | None | True | False |
| The maximum number of active clusters can be run at the same time | 500.0 | None | True | False |
| The maximum number of active instances per instance group | 2000.0 | None | True | False |
| The maximum rate at which your bucket replenishes for all EMR operations. | 5.0 | None | True | False |

## Amazon OpenSearch Service (AWS Service: es)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Dedicated master instances per domain | 5.0 | None | False | False |
| Domains per Region | 100.0 | None | True | False |
| Instances per domain | 80.0 | None | True | False |
| Instances per domain (T2 instance type) | 10.0 | None | False | False |
| Warm instances per domain | 150.0 | None | False | False |

## Amazon EventBridge (CloudWatch Events) (AWS Service: events)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Api destinations | 3000.0 | None | True | False |
| Connections | 3000.0 | None | True | False |
| CreateEndpoint throttle limit in transactions per second | 5.0 | None | False | False |
| DeleteEndpoint throttle limit in transactions per second | 5.0 | None | False | False |
| Endpoints | 100.0 | None | True | False |
| Invocations throttle limit in transactions per second | 2250.0 | None | True | False |
| Number of rules | 300.0 | None | True | False |
| PutEvents throttle limit in transactions per second | 1200.0 | None | True | False |
| Rate of invocations per API destination | 300.0 | None | True | False |
| Targets per rule | 5.0 | None | False | False |
| Throttle limit in transactions per second | 50.0 | None | True | False |
| UpdateEndpoint throttle limit in transactions per second | 5.0 | None | False | False |

## AWS Fargate (AWS Service: fargate)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Fargate On-Demand resource count | 1000.0 | None | True | False |
| Fargate Spot resource count | 1000.0 | None | True | False |

## Amazon Kinesis Data Firehose (AWS Service: firehose)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Delivery streams | 50.0 | None | True | False |
| Dynamic Partitions | 500.0 | None | False | False |
| Rate of CreateDeliveryStream requests | 5.0 | None | False | False |
| Rate of DeleteDeliveryStream requests | 5.0 | None | False | False |
| Rate of DescribeDeliveryStream requests | 5.0 | None | False | False |
| Rate of ListDeliveryStream requests | 5.0 | None | False | False |
| Rate of ListTagsForDeliveryStream requests | 5.0 | None | False | False |
| Rate of Put requests | 1000.0 | None | False | False |
| Rate of StartDeliveryStreamEncryption requests | 5.0 | None | False | False |
| Rate of StopDeliveryStreamEncryption requests | 5.0 | None | False | False |
| Rate of TagDeliveryStream requests | 5.0 | None | False | False |
| Rate of UntagDeliveryStream requests | 5.0 | None | False | False |
| Rate of UpdateDestination requests | 5.0 | None | False | False |
| Rate of data | 1.0 | None | False | False |
| Rate of records | 100000.0 | None | False | False |

## AWS Fault Injection Simulator (AWS Service: fis)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Action duration in hours | 12.0 | None | False | False |
| Actions per experiment template | 20.0 | None | False | False |
| Active experiments | 5.0 | None | False | False |
| Completed experiment data retention in days | 120.0 | None | False | False |
| Experiment duration in hours | 12.0 | None | False | False |
| Experiment templates | 500.0 | None | False | False |
| Parallel actions per experiment | 10.0 | None | False | False |
| Resources per experiment target | 5.0 | None | False | False |
| Stop conditions per experiment template | 5.0 | None | False | False |

## AWS Firewall Manager (AWS Service: fms)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| AWS WAF Classic rule groups per AWS WAF Classic policy | 2.0 | None | False | False |
| Amazon VPC instances in scope of a common security group policy | 100.0 | None | True | False |
| Applications per application list | 50.0 | None | True | False |
| Audit security groups per security group content audit policy | 1.0 | None | True | False |
| Custom managed application lists in any content audit security group policy setting | 1.0 | None | True | False |
| Custom managed application lists per account | 10.0 | None | True | False |
| Custom managed protocol lists in any content audit security group policy setting | 1.0 | None | True | False |
| Custom managed protocol lists per account | 10.0 | None | True | False |
| Explicitly included or excluded accounts per policy per Region | 200.0 | None | True | False |
| Firewall Manager policies per organization per Region | 20.0 | None | True | False |
| IPV4 CIDRs for a Network Firewall policy | 50.0 | None | False | False |
| Organizational units in scope per policy per Region | 20.0 | None | True | False |
| Primary security groups per common security group policy | 1.0 | None | True | False |
| Protocols per protocol list | 5.0 | None | True | False |
| Route 53 Resolver DNS Firewall rule groups per DNS Firewall policy | 2.0 | None | True | False |
| Rule groups per AWS WAF policy | 50.0 | None | True | False |
| Tags to include or exclude resources per policy | 8.0 | None | True | False |
| VPCs that a single Network Firewall policy can automatically remediate | 1000.0 | None | False | False |
| Web ACL capacity units (WCU) used in an AWS WAF policy | 1500.0 | None | True | False |

## Amazon FSx (AWS Service: fsx)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Lustre Persistent HDD storage capacity (per file system) | 102000.0 | None | True | False |
| Lustre Persistent_1 file systems | 100.0 | None | True | False |
| Lustre Persistent_1 storage capacity | 100800.0 | None | True | False |
| Lustre Scratch file systems | 100.0 | None | True | False |
| Lustre Scratch storage capacity | 100800.0 | None | True | False |
| Lustre backups | 500.0 | None | True | False |
| ONTAP SSD IOPS | 1000000.0 | None | True | False |
| ONTAP SSD storage capacity | 524288.0 | None | True | False |
| ONTAP backups | 10000.0 | None | True | False |
| ONTAP file systems | 100.0 | None | True | False |
| ONTAP throughput capacity | 10240.0 | None | True | False |
| Windows HDD storage capacity | 524288.0 | None | True | False |
| Windows SSD storage capacity | 524288.0 | None | True | False |
| Windows backups | 500.0 | None | True | False |
| Windows file systems | 100.0 | None | True | False |
| Windows throughput capacity | 10240.0 | None | True | False |

## Amazon GameLift (AWS Service: gamelift)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Aliases per region | 100.0 | None | True | False |
| Build capacity | 100.0 | Gigabytes | False | False |
| Builds per region | 1000.0 | None | True | False |
| Fleets per region | 10.0 | None | True | False |
| Game server groups per region | 20.0 | None | True | False |
| Game servers per game server group | 1000.0 | None | True | False |
| Game session log file size | 200.0 | Megabytes | False | False |
| Game session queues per region | 20.0 | None | True | False |
| Instances per region | 15.0 | None | True | False |
| Player sessions per game session | 200.0 | None | False | False |
| Queue destinations per game session queue | 10.0 | None | True | False |
| Scripts per region | 1000.0 | None | True | False |
| Server processes per instance (GameLift SDK v2) | 1.0 | None | False | False |
| Server processes per instance (GameLift SDK v3 and up) | 50.0 | None | False | False |

## Amazon Glacier (AWS Service: glacier)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Archive size in GB. | 40000.0 | Gigabytes | False | False |
| Archive size. | 4.0 | Megabytes | False | False |
| Multipart parts size. | 4.0 | Gigabytes | False | False |
| Number of multipart parts. | 10000.0 | None | False | False |
| Number of random restore requests. | 35.0 | None | False | False |
| Number of vault tags. | 50.0 | None | False | False |
| Provisioned capacity units | 2.0 | None | False | False |
| Vaults per account | 1000.0 | None | False | False |

## AWS Glue (AWS Service: glue)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Concurrent machine learning task runs per transform | 3.0 | None | True | False |
| Label file size | 10.0 | Megabytes | True | False |
| Max concurrent job runs per account | 200.0 | None | True | False |
| Max concurrent job runs per job | 1000.0 | None | True | False |
| Max connection per account | 1000.0 | None | True | False |
| Max databases per account | 10000.0 | None | True | False |
| Max databases per catalog | 10000.0 | None | True | False |
| Max development endpoint per account | 25.0 | None | True | False |
| Max dpus per dev endpoint | 50.0 | None | True | False |
| Max functions per account | 100.0 | None | True | False |
| Max functions per database | 100.0 | None | True | False |
| Max jobs per account | 1000.0 | None | True | False |
| Max jobs per trigger | 50.0 | None | True | False |
| Max partitions per account | 20000000.0 | None | True | False |
| Max partitions per table | 10000000.0 | None | True | False |
| Max security configurations per account | 250.0 | None | True | False |
| Max spare compute capacity consumed in data processing units (DPUs) per account. | 50.0 | None | True | False |
| Max table versions per account | 1000000.0 | None | True | False |
| Max table versions per table | 100000.0 | None | True | False |
| Max tables per account | 1000000.0 | None | True | False |
| Max tables per database | 200000.0 | None | True | False |
| Max task dpus per account | 500.0 | None | True | False |
| Max triggers per account | 1000.0 | None | True | False |
| Number of Schema Registries. | 10.0 | None | True | False |
| Number of Schema Versions. | 1000.0 | None | True | False |
| Number of crawlers per account | 1000.0 | None | True | False |
| Number of crawlers running concurrently per account | 150.0 | None | True | False |
| Number of machine learning transforms | 100.0 | None | True | False |
| Number of metadata key value pairs per Schema Version. | 10.0 | None | False | False |
| Number of workflows | 250.0 | None | True | False |
| Total concurrent machine learning task runs for transforms per account | 30.0 | None | True | False |

## Amazon Managed Grafana (AWS Service: grafana)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Number of workspaces | 5.0 | None | True | False |
| Rate of AssociateLicense requests | 1.0 | None | False | False |
| Rate of CreateWorkspace requests | 1.0 | None | False | False |
| Rate of DeleteWorkspace requests | 1.0 | None | False | False |
| Rate of DescribeWorkspace requests | 5.0 | None | False | False |
| Rate of DescribeWorkspaceAuthentication requests | 1.0 | None | False | False |
| Rate of DisassociateLicense requests | 1.0 | None | False | False |
| Rate of ListPermissions requests | 10.0 | None | False | False |
| Rate of ListWorkspaces requests | 5.0 | None | False | False |
| Rate of UpdatePermissions requests | 10.0 | None | False | False |
| Rate of UpdateWorkspace requests | 10.0 | None | False | False |
| Rate of UpdateWorkspaceAuthentication requests | 1.0 | None | False | False |

## AWS IoT Greengrass (AWS Service: greengrass)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| AWS IoT devices per Greengrass group | 2500.0 | None | False | False |
| Component recipe size | 8.0 | Kilobytes | False | False |
| Components | 5000.0 | None | True | False |
| Core device thing name length | 124.0 | None | False | False |
| Deployment document size (with large configuration support) | 10.0 | Megabytes | False | False |
| Lambda functions per Greengrass group | 200.0 | None | False | False |
| Rate of API requests | 30.0 | None | False | False |
| Rate of CreateComponentVersion requests | 1.0 | None | False | False |
| Rate of CreateDeployment requests (V1) | 20.0 | None | False | False |
| Resources per Greengrass group | 200.0 | None | False | False |
| Resources per Lambda function (V1) | 20.0 | None | False | False |
| Subscriptions per Greengrass group | 10000.0 | None | False | False |
| Subscriptions with 'cloud' message source per Greengrass group | 50.0 | None | False | False |
| Thing deployment document size (without large configuration support) | 7.0 | Kilobytes | False | False |
| Thing group deployment document size (without large configuration support) | 31.0 | Kilobytes | False | False |
| Total component artifact size | 2.0 | Gigabytes | False | False |
| Versions per component | 5000.0 | None | True | False |

## Amazon GuardDuty (AWS Service: guardduty)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Detectors | 1.0 | None | False | False |
| Filters | 100.0 | None | False | False |
| Finding retention period | 90.0 | None | False | False |
| Member accounts | 5000.0 | None | False | False |
| Threat intel sets | 6.0 | None | True | False |
| Trusted IP sets | 1.0 | None | False | False |

## EC2 Image Builder (AWS Service: imagebuilder)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Component parameter length | 1024.0 | None | True | False |
| Component size | 64.0 | Kilobytes | True | False |
| Components | 1000.0 | None | True | False |
| Components per image recipe | 20.0 | None | False | False |
| Concurrent AMI copies per distribution configuration | 50.0 | None | True | False |
| Concurrent builds | 100.0 | None | True | False |
| Container recipes | 1000.0 | None | True | False |
| Distribution configurations | 1000.0 | None | True | False |
| Docker template size | 64.0 | Kilobytes | True | False |
| Image pipelines | 75.0 | None | True | False |
| Image recipes | 1000.0 | None | True | False |
| Infrastructure configurations | 1000.0 | None | True | False |
| Launch templates modified per distribution configuration | 5.0 | None | True | False |
| Parameters per component | 25.0 | None | True | False |

## Amazon Inspector (AWS Service: inspector2)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Number of Suppression Rules | 500.0 | None | False | False |

## AWS IoT (AWS Service: iot)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Active continuous jobs | 100000.0 | None | True | False |
| Active snapshot jobs | 100000.0 | None | True | False |
| AssociateTargetsWithJob throttle limit | 10.0 | None | True | False |
| AttachSecurityProfile API TPS | 10.0 | None | False | False |
| Behavior metric value elements for each security profile | 1000.0 | None | False | False |
| Behaviors for each security profile | 100.0 | None | False | False |
| CancelAuditMitigationActionsTask API TPS | 10.0 | None | False | False |
| CancelAuditTask API TPS | 10.0 | None | False | False |
| CancelDetectMitigationActionsTask API TPS | 10.0 | None | False | False |
| CancelJob throttle limit | 10.0 | None | True | False |
| CancelJobExecution throttle limit | 10.0 | None | True | False |
| CloseTunnel API throttle limit | 1.0 | None | True | False |
| Comment length | 2028.0 | None | False | False |
| Concurrent jobs | 500.0 | None | True | False |
| CreateAuditSuppression API TPS | 10.0 | None | False | False |
| CreateCustomMetric API TPS | 10.0 | None | False | False |
| CreateJob throttle limit | 10.0 | None | False | False |
| CreateJobTemplate throttle limit | 10.0 | None | True | False |
| CreateMitigationAction API TPS | 10.0 | None | False | False |
| CreateOTAUpdate API TPS | 10.0 | None | True | False |
| CreateScheduledAudit API TPS | 5.0 | None | False | False |
| CreateSecurityProfile API TPS | 10.0 | None | False | False |
| CreateStream API TPS | 15.0 | None | True | False |
| Custom metrics | 100.0 | None | True | False |
| Data retention | 730.0 | None | False | False |
| DeleteAccountAuditConfiguration API TPS | 5.0 | None | False | False |
| DeleteAuditSuppression API TPS | 10.0 | None | False | False |
| DeleteCustomMetric API TPS | 10.0 | None | False | False |
| DeleteDimension API TPS | 10.0 | None | False | False |
| DeleteJob throttle limit | 10.0 | None | True | False |
| DeleteJobExecution throttle limit | 10.0 | None | True | False |
| DeleteJobTemplate throttle limit | 10.0 | None | True | False |
| DeleteMitigationAction API TPS | 10.0 | None | False | False |
| DeleteOTAUpdate API TPS | 5.0 | None | True | False |
| DeleteScheduledAudit API TPS | 5.0 | None | False | False |
| DeleteSecurityProfile API TPS | 10.0 | None | False | False |
| DeleteStream API TPS | 15.0 | None | True | False |
| DescribeAccountAuditConfiguration API TPS | 5.0 | None | False | False |
| DescribeAuditFinding API TPS | 25.0 | None | False | False |
| DescribeAuditMitigationActionsTask API TPS | 25.0 | None | False | False |
| DescribeAuditSuppression API TPS | 10.0 | None | False | False |
| DescribeAuditTask API TPS | 25.0 | None | False | False |
| DescribeCustomMetric API TPS | 25.0 | None | False | False |
| DescribeDetectMitigationActionsTask API TPS | 10.0 | None | False | False |
| DescribeDimension API TPS | 10.0 | None | False | False |
| DescribeIndex rate | 10.0 | None | True | False |
| DescribeJob throttle limit | 10.0 | None | True | False |
| DescribeJobExecution throttle limit | 10.0 | None | True | False |
| DescribeJobExecution/GetPendingJobExecutions throttle limit | 200.0 | None | False | False |
| DescribeJobTemplate throttle limit | 10.0 | None | True | False |
| DescribeMitigationAction API TPS | 25.0 | None | False | False |
| DescribeScheduledAudit API TPS | 5.0 | None | False | False |
| DescribeSecurityProfile API TPS | 25.0 | None | False | False |
| DescribeStream API TPS | 15.0 | None | True | False |
| DescribeTunnel API throttle limit | 10.0 | None | True | False |
| DetachSecurityProfile API TPS | 10.0 | None | False | False |
| Device metric minimum delay | 300.0 | Seconds | True | False |
| Device metric peak reporting rate for an account | 3500.0 | None | True | False |
| DocumentSource length | 1350.0 | None | False | False |
| File size | 16.0 | Megabytes | False | False |
| Files per stream | 10.0 | None | False | False |
| GetCardinality rate | 15.0 | None | True | False |
| GetIndexingConfiguration rate | 20.0 | None | True | False |
| GetJobDocument throttle limit | 10.0 | None | True | False |
| GetOTAUpdate API TPS | 15.0 | None | True | False |
| GetPercentiles rate | 15.0 | None | True | False |
| GetStatistics rate | 15.0 | None | True | False |
| In Progress timeout | 10080.0 | None | False | False |
| Job Targets | 100.0 | None | False | False |
| Job Template description length | 2028.0 | None | False | False |
| Job description length | 2028.0 | None | False | False |
| Job execution roll out rate | 1000.0 | None | True | False |
| JobId Length | 64.0 | None | False | False |
| JobTemplateId Length | 64.0 | None | False | False |
| List results per page | 250.0 | None | False | False |
| ListActiveViolations API TPS | 10.0 | None | False | False |
| ListAuditFindings API TPS | 10.0 | None | False | False |
| ListAuditMitigationActionsExecutions API TPS | 10.0 | None | False | False |
| ListAuditMitigationActionsTasks API TPS | 10.0 | None | False | False |
| ListAuditSuppressions API TPS | 10.0 | None | False | False |
| ListAuditTasks API TPS | 10.0 | None | False | False |
| ListCustomMetrics API TPS | 10.0 | None | False | False |
| ListDetectMitigationActionsExecutions API TPS | 10.0 | None | False | False |
| ListDetectMitigationActionsTasks API TPS | 10.0 | None | False | False |
| ListDimensions API TPS | 10.0 | None | False | False |
| ListIndices rate | 5.0 | None | True | False |
| ListJobExecutionsForJob throttle limit | 10.0 | None | True | False |
| ListJobExecutionsForThing throttle limit | 10.0 | None | True | False |
| ListJobTemplates throttle limit | 10.0 | None | True | False |
| ListJobs throttle limit | 10.0 | None | True | False |
| ListMetricValues API TPS | 15.0 | None | True | False |
| ListMitigationActions API TPS | 10.0 | None | False | False |
| ListOTAUpdates API TPS | 15.0 | None | True | False |
| ListScheduledAudits API TPS | 5.0 | None | False | False |
| ListSecurityProfiles API TPS | 10.0 | None | False | False |
| ListSecurityProfilesForTarget API TPS | 10.0 | None | False | False |
| ListStreams API TPS | 15.0 | None | True | False |
| ListTagsForResource API throttle limit | 10.0 | None | True | False |
| ListTargetsForSecurityProfile API TPS | 10.0 | None | False | False |
| ListTunnels API throttle limit | 10.0 | None | True | False |
| ListViolationEvents API TPS | 10.0 | None | False | False |
| Maximum bandwidth per tunnel | 800.0 | None | False | False |
| Maximum connection rate | 10.0 | None | True | False |
| Maximum length of a custom field name | 1024.0 | None | True | False |
| Maximum length of a query | 1000.0 | None | True | False |
| Maximum number of * wildcard operators per query term | 2.0 | None | False | False |
| Maximum number of ? wildcard operators per query term | 5.0 | None | False | False |
| Maximum number of custom fields in AWS thing groups index | 5.0 | None | True | False |
| Maximum number of custom fields in AWS things index | 5.0 | None | True | False |
| Maximum number of dynamic groups | 100.0 | None | True | False |
| Maximum number of fleet metrics | 100.0 | None | True | False |
| Maximum number of job templates | 100.0 | None | True | False |
| Maximum number of names in the named shadow names filter | 10.0 | None | True | False |
| Maximum number of percentile values per fleet metric | 5.0 | None | False | False |
| Maximum number of query terms per fleet metric | 7.0 | None | True | False |
| Maximum number of query terms per query | 7.0 | None | True | False |
| Maximum number of results per search query | 500.0 | None | False | False |
| Maximum number of tags per resource | 50.0 | None | False | False |
| Maximum period of a fleet metric | 86400.0 | Seconds | False | False |
| Maximum tag key length | 128.0 | None | False | False |
| Maximum tag value length | 256.0 | None | False | False |
| Maximum tunnel lifetime | 12.0 | None | False | False |
| Metric dimensions | 10.0 | None | False | False |
| Minimum job execution roll out rate | 1.0 | None | False | False |
| Minimum period of a fleet metric | 60.0 | Seconds | False | False |
| Minimum pre-signed URL lifetime | 60.0 | Seconds | False | False |
| Mitigation actions | 100.0 | None | False | False |
| OpenTunnel API throttle limit | 1.0 | None | True | False |
| Pre-signed URL lifetime | 3600.0 | Seconds | False | False |
| PutVerificationStateOnViolation API TPS | 10.0 | None | False | False |
| S3 job document length | 32768.0 | Bytes | True | False |
| Scheduled audits | 5.0 | None | False | False |
| SearchIndex rate | 15.0 | None | True | False |
| Security profiles for each target | 5.0 | None | False | False |
| Simultaneous in progress on-demand audits | 10.0 | None | False | False |
| StartAuditMitigationActionsTask API TPS | 10.0 | None | False | False |
| StartDetectMitigationActionsTask API TPS | 10.0 | None | False | False |
| StartNextPendingJobExecution/UpdateJobExecution throttle limit | 200.0 | None | False | False |
| StartOnDemandAuditTask API TPS | 10.0 | None | False | False |
| StatusDetail map key length | 128.0 | None | False | False |
| StatusDetail map key-value pairs | 10.0 | None | False | False |
| StatusDetail map value length | 1024.0 | None | False | False |
| Step Timer | 10080.0 | None | False | False |
| Storage duration for audit findings | 90.0 | None | False | False |
| Storage duration for detect metrics | 14.0 | None | False | False |
| Storage duration for detect violations | 30.0 | None | False | False |
| Streams per account | 10000.0 | None | False | False |
| TagResource API throttle limit | 10.0 | None | True | False |
| UntagResource API trottle limit | 10.0 | None | True | False |
| UpdateAccountAuditConfiguration API TPS | 5.0 | None | False | False |
| UpdateAuditSuppression API TPS | 10.0 | None | False | False |
| UpdateCustomMetric API TPS | 10.0 | None | False | False |
| UpdateDimension API TPS | 10.0 | None | False | False |
| UpdateIndexingConfiguration rate | 1.0 | None | True | False |
| UpdateJob throttle limit | 10.0 | None | True | False |
| UpdateMitigationAction API TPS | 10.0 | None | False | False |
| UpdateScheduledAudit API TPS | 5.0 | None | False | False |
| UpdateSecurityProfile API TPS | 10.0 | None | False | False |
| UpdateStream API TPS | 15.0 | None | True | False |
| ValidateSecurityProfileBehaviors API TPS | 10.0 | None | False | False |

## AWS IoT 1-Click (AWS Service: iot1click)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| AssociateDeviceWithPlacement API TPS | 10.0 | None | False | False |
| CreatePlacement API TPS | 10.0 | None | False | False |
| CreateProject API TPS | 10.0 | None | False | False |
| DeletePlacement API TPS | 10.0 | None | False | False |
| DeleteProject API TPS | 10.0 | None | False | False |
| DescribePlacement API TPS | 10.0 | None | False | False |
| DescribeProject API TPS | 10.0 | None | False | False |
| DisassociateDeviceFromPlacement API TPS | 10.0 | None | False | False |
| GetDevicesInPlacement API TPS | 10.0 | None | False | False |
| ListPlacements API TPS | 10.0 | None | False | False |
| ListProjects API TPS | 10.0 | None | False | False |
| ListTagsForResource API TPS | 10.0 | None | False | False |
| TagResource API TPS | 10.0 | None | False | False |
| UntagResource API TPS | 10.0 | None | False | False |
| UpdatePlacement API TPS | 10.0 | None | False | False |
| UpdateProject API TPS | 10.0 | None | False | False |

## AWS IoT Core (AWS Service: iotcore)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| AcceptCertificateTransfer API TPS | 10.0 | None | True | False |
| AddThingToBillingGroup API TPS | 60.0 | None | True | False |
| AddThingToThingGroup API TPS | 100.0 | None | True | False |
| Allowed registration tasks | 1.0 | None | False | False |
| AssumeRoleWithCertificate API TPS | 50.0 | None | True | False |
| AttachPolicy API TPS | 15.0 | None | True | False |
| AttachPrincipalPolicy API TPS | 15.0 | None | True | False |
| AttachThingPrincipal API TPS | 100.0 | None | True | False |
| CancelCertificateTransfer API TPS | 10.0 | None | True | False |
| ClearDefaultAuthorizer API TPS | 10.0 | None | True | False |
| Client ID size | 128.0 | Bytes | False | False |
| Configurable endpoints: maximum number of domain configurations per account | 10.0 | None | True | False |
| Connect requests per second per account | 500.0 | None | True | False |
| Connect requests per second per client ID | 1.0 | None | False | False |
| Connection inactivity (keep-alive interval) | 1200.0 | Seconds | False | False |
| CreateAuthorizer API TPS | 10.0 | None | False | False |
| CreateBillingGroup API TPS | 25.0 | None | True | False |
| CreateCertificateFromCsr API TPS | 15.0 | None | True | False |
| CreateDomainConfiguration API TPS | 1.0 | None | False | False |
| CreateDynamicThingGroup API TPS | 5.0 | None | True | False |
| CreateKeysAndCertificate API TPS | 10.0 | None | True | False |
| CreatePolicy API TPS | 10.0 | None | True | False |
| CreatePolicyVersion API TPS | 10.0 | None | True | False |
| CreateProvisioningClaim API TPS | 10.0 | None | True | False |
| CreateProvisioningTemplate API TPS | 10.0 | None | False | False |
| CreateProvisioningTemplateVersion API TPS | 10.0 | None | False | False |
| CreateRoleAlias API TPS | 10.0 | None | False | False |
| CreateThing API TPS | 100.0 | None | True | False |
| CreateThingGroup API TPS | 25.0 | None | True | False |
| CreateThingType API TPS | 15.0 | None | True | False |
| CreateTopicRule API TPS | 5.0 | None | False | False |
| CreateTopicRuleDestination API TPS | 5.0 | None | False | False |
| Custom authentication: maximum number of authorizers per account | 10.0 | None | False | False |
| Data retention policy | 2592000.0 | Seconds | False | False |
| DeleteAuthorizer API TPS | 10.0 | None | False | False |
| DeleteBillingGroup API TPS | 15.0 | None | True | False |
| DeleteCACertificate API TPS | 10.0 | None | True | False |
| DeleteCertificate API TPS | 10.0 | None | True | False |
| DeleteDomainConfiguration API TPS | 10.0 | None | False | False |
| DeleteDynamicThingGroup API TPS | 5.0 | None | True | False |
| DeletePolicy API TPS | 10.0 | None | True | False |
| DeletePolicyVersion API TPS | 10.0 | None | True | False |
| DeleteProvisioningTemplate API TPS | 10.0 | None | True | False |
| DeleteProvisioningTemplateVersion API TPS | 10.0 | None | False | False |
| DeleteRegistrationCode API TPS | 10.0 | None | True | False |
| DeleteRoleAlias API TPS | 10.0 | None | False | False |
| DeleteThing API TPS | 100.0 | None | True | False |
| DeleteThingGroup API TPS | 15.0 | None | True | False |
| DeleteThingType API TPS | 15.0 | None | True | False |
| DeleteTopicRule API TPS | 20.0 | None | False | False |
| DeleteTopicRuleDestination API TPS | 5.0 | None | False | False |
| DeleteV2LoggingLevel API TPS | 2.0 | None | False | False |
| DeprecateThingType API TPS | 15.0 | None | True | False |
| DescribeAuthorizer API TPS | 10.0 | None | True | False |
| DescribeBillingGroup API TPS | 100.0 | None | True | False |
| DescribeCACertificate API TPS | 10.0 | None | True | False |
| DescribeCertificate API TPS | 10.0 | None | True | False |
| DescribeCertificateTag API TPS | 10.0 | None | True | False |
| DescribeDefaultAuthorizer API TPS | 10.0 | None | True | False |
| DescribeDomainConfiguration API TPS | 10.0 | None | True | False |
| DescribeEndpoint API TPS | 10.0 | None | False | False |
| DescribeProvisioningTemplate API TPS | 10.0 | None | True | False |
| DescribeProvisioningTemplateVersion API TPS | 10.0 | None | True | False |
| DescribeRoleAlias API TPS | 10.0 | None | True | False |
| DescribeThing API TPS | 350.0 | None | True | False |
| DescribeThingGroup API TPS | 100.0 | None | True | False |
| DescribeThingType API TPS | 100.0 | None | True | False |
| DetachPolicy API TPS | 15.0 | None | True | False |
| DetachPrincipalPolicy API TPS | 15.0 | None | True | False |
| DetachThingPrincipal API TPS | 100.0 | None | True | False |
| Device Shadow API requests/second per account | 4000.0 | None | True | False |
| DisableTopicRule API TPS | 5.0 | None | False | False |
| EnableTopicRule API TPS | 5.0 | None | False | False |
| Fleet Provisioning CreateCertificateFromCsr MQTT API TPS | 100.0 | None | True | False |
| Fleet Provisioning CreateKeysAndCertificate MQTT API TPS | 10.0 | None | True | False |
| Fleet Provisioning RegisterThing MQTT API TPS | 10.0 | None | True | False |
| GetEffectivePolicies API TPS | 5.0 | None | True | False |
| GetLoggingOptions API TPS | 2.0 | None | False | False |
| GetPolicy API TPS | 10.0 | None | True | False |
| GetPolicyVersion API TPS | 15.0 | None | True | False |
| GetRegistrationCode API TPS | 10.0 | None | True | False |
| GetRetainedMessage API TPS | 500.0 | None | True | False |
| GetTopicRule API TPS | 200.0 | None | False | False |
| GetTopicRuleDestination API TPS | 50.0 | None | False | False |
| GetV2LoggingOptions API TPS | 2.0 | None | False | False |
| HTTP Action: Maximum length of an endpoint URL | 2.0 | Kilobytes | False | False |
| HTTP Action: Maximum number of headers per action | 100.0 | None | False | False |
| HTTP Action: Maximum size of a header key | 256.0 | Bytes | False | False |
| HTTP Action: Maximum topic rule destinations per AWS account | 1000.0 | None | False | False |
| HTTP Action: Request timeout | 3000.0 | Milliseconds | False | False |
| Inbound publish requests per second per account | 20000.0 | None | True | False |
| ListAttachedPolicies API TPS | 15.0 | None | True | False |
| ListAuthorizers API TPS | 10.0 | None | True | False |
| ListBillingGroups API TPS | 10.0 | None | True | False |
| ListCACertificates API TPS | 10.0 | None | True | False |
| ListCertificates API TPS | 10.0 | None | True | False |
| ListCertificatesByCA API TPS | 10.0 | None | True | False |
| ListDomainConfigurations API TPS | 10.0 | None | True | False |
| ListOutgoingCertificates API TPS | 10.0 | None | True | False |
| ListPolicies API TPS | 10.0 | None | True | False |
| ListPolicyPrincipals API TPS | 10.0 | None | True | False |
| ListPolicyVersions API TPS | 10.0 | None | True | False |
| ListPrincipalPolicies API TPS | 15.0 | None | True | False |
| ListPrincipalThings API TPS | 10.0 | None | True | False |
| ListProvisioningTemplateVersions API TPS | 10.0 | None | True | False |
| ListProvisioningTemplates API TPS | 10.0 | None | True | False |
| ListRetainedMessages API TPS | 10.0 | None | True | False |
| ListRoleAliases API TPS | 10.0 | None | True | False |
| ListTagsForResource API TPS | 10.0 | None | True | False |
| ListTargetsForPolicy API TPS | 10.0 | None | True | False |
| ListThingGroups API TPS | 10.0 | None | True | False |
| ListThingGroupsForThing API TPS | 100.0 | None | True | False |
| ListThingPrincipals API TPS | 10.0 | None | True | False |
| ListThingTypes API TPS | 10.0 | None | True | False |
| ListThings API TPS | 10.0 | None | True | False |
| ListThingsInBillingGroup API TPS | 25.0 | None | True | False |
| ListThingsInThingGroup API TPS | 25.0 | None | True | False |
| ListTopicRuleDestinations API TPS | 1.0 | None | False | False |
| ListTopicRules API TPS | 1.0 | None | False | False |
| ListV2LoggingLevels API TPS | 2.0 | None | False | False |
| Maximum concurrent client connections per account | 500000.0 | None | True | False |
| Maximum depth of JSON device state documents | 5.0 | None | False | False |
| Maximum depth of a thing group hierarchy | 7.0 | None | False | False |
| Maximum inbound unacknowledged QoS 1 publish requests | 100.0 | None | False | False |
| Maximum line length | 256000.0 | None | False | False |
| Maximum number of AWS IoT Core role aliases | 100.0 | None | False | False |
| Maximum number of CA certificates with the same subject field allowed per AWS account per Region | 10.0 | None | False | False |
| Maximum number of actions per rule | 10.0 | None | False | False |
| Maximum number of attributes associated with a thing group | 50.0 | None | False | False |
| Maximum number of device certificates that can be registered per second | 15.0 | None | True | False |
| Maximum number of direct child groups | 100.0 | None | False | False |
| Maximum number of domain configurations per account per region | 10.0 | None | True | False |
| Maximum number of dynamic groups | 100.0 | None | False | False |
| Maximum number of fleet provisioning template versions per template | 5.0 | None | False | False |
| Maximum number of fleet provisioning templates per customer | 256.0 | None | False | False |
| Maximum number of in-flight, unacknowledged messages per thing | 10.0 | None | False | False |
| Maximum number of named policy versions | 5.0 | None | False | False |
| Maximum number of policies that can be attached to a certificate or Amazon Cognito identity | 10.0 | None | False | False |
| Maximum number of provisioning claims that can be generated per second by trusted user | 10.0 | None | False | False |
| Maximum number of retained messages per account | 5000.0 | None | True | False |
| Maximum number of rules per AWS account | 1000.0 | None | True | False |
| Maximum number of slashes in topic and topic filter | 7.0 | None | False | False |
| Maximum number of thing attributes for a thing with a thing type | 50.0 | None | True | False |
| Maximum number of thing attributes for a thing without a thing type | 3.0 | None | False | False |
| Maximum number of thing groups a thing can belong to | 10.0 | None | False | False |
| Maximum outbound unacknowledged QoS 1 publish requests | 100.0 | None | False | False |
| Maximum policy document size | 2048.0 | None | False | False |
| Maximum retry interval for delivering QoS 1 messages | 3600.0 | Seconds | False | False |
| Maximum shadow name size | 64.0 | Bytes | False | False |
| Maximum size of a JSON state document | 8.0 | Kilobytes | True | False |
| Maximum size of a thing group attribute name, in chars | 128.0 | None | False | False |
| Maximum size of a thing group attribute value, in chars | 800.0 | None | False | False |
| Maximum size of fleet provisioning template | 10.0 | Kilobytes | False | False |
| Maximum subscriptions per subscribe request | 8.0 | None | False | False |
| Maximum thing group name size | 128.0 | Bytes | False | False |
| Maximum thing name size | 128.0 | Bytes | False | False |
| Maximum thing name size | 128.0 | Bytes | False | False |
| Message size | 128.0 | Kilobytes | False | False |
| Number of thing types that can be associated with a thing | 1.0 | None | False | False |
| Outbound publish requests per second per account | 20000.0 | None | True | False |
| Persistent session expiry period | 3600.0 | Seconds | True | False |
| Publish requests per second per connection | 100.0 | None | False | False |
| Queued messages per second per account | 500.0 | None | True | False |
| RegisterCACertificate API TPS | 10.0 | None | True | False |
| RegisterCertificate API TPS | 10.0 | None | True | False |
| RegisterCertificateWithoutCA API TPS | 10.0 | None | True | False |
| RegisterThing API TPS | 10.0 | None | True | False |
| Registration task termination | 2592000.0 | Seconds | False | False |
| RejectCertificateTransfer API TPS | 10.0 | None | True | False |
| RemoveThingFromBillingGroup API TPS | 15.0 | None | True | False |
| RemoveThingFromThingGroup API TPS | 100.0 | None | True | False |
| ReplaceTopicRule API TPS | 5.0 | None | False | False |
| Requests per second per thing | 20.0 | None | False | False |
| Retained message inbound publish requests per second per account | 500.0 | None | True | False |
| Retained message inbound publish requests per second per topic | 1.0 | None | False | False |
| Rule evaluations per second per AWS account | 20000.0 | None | True | False |
| Rule size | 256.0 | Kilobytes | False | False |
| SetDefaultAuthorizer API TPS | 10.0 | None | True | False |
| SetDefaultPolicyVersion API TPS | 10.0 | None | True | False |
| SetLoggingOptions API TPS | 2.0 | None | False | False |
| SetV2LoggingLevel API TPS | 2.0 | None | False | False |
| SetV2LoggingOptions API TPS | 2.0 | None | False | False |
| Size of thing attributes per thing | 47.0 | Kilobytes | True | False |
| Subscriptions per account | 500000.0 | None | True | False |
| Subscriptions per connection | 50.0 | None | False | False |
| Subscriptions per second per account | 500.0 | None | True | False |
| TagResource API TPS | 10.0 | None | True | False |
| TestAuthorization API TPS | 10.0 | None | False | False |
| TestInvokeAuthorizer API TPS | 10.0 | None | False | False |
| Throughput per second per connection | 512.0 | Kilobytes | False | False |
| Topic size | 256.0 | Bytes | False | False |
| TransferCertificate API TPS | 10.0 | None | True | False |
| UntagResource API TPS | 10.0 | None | True | False |
| UpdateAuthorizer API TPS | 10.0 | None | True | False |
| UpdateBillingGroup API TPS | 15.0 | None | True | False |
| UpdateCACertificate API TPS | 10.0 | None | True | False |
| UpdateCertificate API TPS | 10.0 | None | True | False |
| UpdateCertificateMode API TPS | 10.0 | None | True | False |
| UpdateCertificateTag API TPS | 10.0 | None | True | False |
| UpdateDomainConfiguration API TPS | 10.0 | None | True | False |
| UpdateDynamicThingGroup API TPS | 5.0 | None | True | False |
| UpdateProvisioningTemplate API TPS | 10.0 | None | True | False |
| UpdateRoleAlias API TPS | 10.0 | None | True | False |
| UpdateThing API TPS | 100.0 | None | True | False |
| UpdateThingGroup API TPS | 15.0 | None | True | False |
| UpdateTopicRuleDestination API TPS | 5.0 | None | False | False |
| WebSocket connection duration | 86400.0 | Seconds | False | False |

## AWS IoT Events (AWS Service: iotevents)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Detector model definition size | 512.0 | Kilobytes | False | False |
| Detector model versions | 500.0 | None | True | False |
| Detector models | 50.0 | None | True | False |
| Detector models per input | 10.0 | None | False | False |
| Detectors per detector model | 100000.0 | None | True | False |
| Inputs | 50.0 | None | True | False |
| Maximum actions per alarm model | 10.0 | None | True | False |
| Maximum actions per event | 10.0 | None | True | False |
| Maximum alarm model versions per alarm model | 500.0 | None | True | False |
| Maximum alarm models per account | 200.0 | None | True | False |
| Maximum alarm models per input | 10.0 | None | False | False |
| Maximum alarms per alarm model | 100000.0 | None | True | False |
| Maximum events per state | 20.0 | None | True | False |
| Maximum messages per alarm per second | 10.0 | None | False | False |
| Maximum number of alarm models per property in an AWS IoT SiteWise asset model | 10.0 | None | True | False |
| Maximum number of recipients per notification action in an alarm model | 10.0 | None | True | False |
| Maximum total messages evaluated per second | 1000.0 | None | True | False |
| Maximum transition events per state | 20.0 | None | True | False |
| Message size | 1.0 | Kilobytes | True | False |
| Messages per detector per second | 10.0 | None | False | False |
| Minimum timer duration | 60.0 | Seconds | True | False |
| Number of detector model analyses in RUNNING status | 10.0 | None | True | False |
| State variables per detector model definition | 50.0 | None | True | False |
| States per detector model | 20.0 | None | True | False |
| Timers scheduled per detector | 5.0 | None | True | False |
| Trigger expressions | 20.0 | None | True | False |

## Amazon Managed Streaming for Kafka (MSK) (AWS Service: kafka)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Number of brokers per account | 90.0 | None | True | False |
| Number of brokers per cluster | 30.0 | None | True | False |
| Number of configurations per account | 100.0 | None | True | False |
| Number of revisions per configuration | 50.0 | None | True | False |

## Amazon Kinesis Data Streams (AWS Service: kinesis)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Shards per Region | 200.0 | None | True | False |

## Amazon Kinesis Data Analytics (AWS Service: kinesisanalytics)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Apache Flink Kinesis Processing Units (KPUs) | 32.0 | None | True | False |
| Application count | 50.0 | None | True | False |
| Input Parallelism in input streams for SQL applications | 64.0 | None | False | False |
| SQL Kinesis Processing Units (KPUs) | 8.0 | None | True | False |

## Amazon Kinesis Video Streams (AWS Service: kinesisvideo)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| ConnectAsMaster GO_AWAY message grace period | 60.0 | Seconds | False | False |
| ConnectAsMaster connection duration | 3600.0 | Seconds | False | False |
| ConnectAsMaster connections per signaling channel | 1.0 | None | False | False |
| ConnectAsMaster idle connection timeout | 600.0 | Seconds | False | False |
| ConnectAsViewer GO_AWAY message grace period | 60.0 | Seconds | False | False |
| ConnectAsViewer connection duration | 3600.0 | Seconds | False | False |
| ConnectAsViewer connections per signaling channel | 10.0 | None | True | False |
| ConnectAsViewer idle connection timeout | 600.0 | Seconds | False | False |
| GetClip file size | 100.0 | Megabytes | False | False |
| GetClip fragments | 200.0 | None | False | False |
| GetDASHManifestPlaylist fragments | 5000.0 | None | False | False |
| GetHLSMediaPlaylist fragments | 5000.0 | None | False | False |
| GetMedia bandwidth | 200.0 | Megabits | True | False |
| GetMedia concurrent connections per stream | 3.0 | None | True | False |
| GetMediaForFragmentList bandwidth | 200.0 | Megabits | True | False |
| GetMediaForFragmentList connections per stream | 5.0 | None | False | False |
| GetMediaForFragmentList fragments | 1000.0 | None | False | False |
| Number of signaling channels | 5000.0 | None | True | False |
| Number of video streams | 5000.0 | None | True | False |
| PutMedia bandwidth | 100.0 | Megabits | True | False |
| PutMedia concurrent connections per stream | 1.0 | None | False | False |
| PutMedia fragment duration | 10.0 | Seconds | True | False |
| PutMedia fragment size | 50.0 | Megabytes | False | False |
| PutMedia minimum fragment duration | 1.0 | Seconds | False | False |
| PutMedia tracks | 3.0 | None | False | False |
| Rate of ConnectAsMasterAPI requests per signaling channel | 3.0 | None | False | False |
| Rate of ConnectAsViewerAPI requests per signaling channel | 3.0 | None | False | False |
| Rate of CreateSignalingChannelAPI requests | 50.0 | None | True | False |
| Rate of CreateStreamAPI requests | 50.0 | None | True | False |
| Rate of DeleteSignalingChannelAPI requests | 50.0 | None | True | False |
| Rate of DeleteSignalingChannelAPI requests per signaling channel | 5.0 | None | True | False |
| Rate of DeleteStreamAPI requests | 50.0 | None | True | False |
| Rate of DeleteStreamAPI requests per stream | 5.0 | None | True | False |
| Rate of DescribeSignalingChannelAPI requests | 300.0 | None | True | False |
| Rate of DescribeSignalingChannelAPI requests per signaling channel | 5.0 | None | True | False |
| Rate of DescribeStreamAPI requests | 300.0 | None | True | False |
| Rate of DescribeStreamAPI requests per stream | 5.0 | None | True | False |
| Rate of GetDASHManifestPlaylistAPI requests per session | 5.0 | None | True | False |
| Rate of GetDASHStreamingSessionURLAPI requests per stream | 25.0 | None | True | False |
| Rate of GetDataEndpointAPI requests | 300.0 | None | True | False |
| Rate of GetDataEndpointAPI requests per stream | 5.0 | None | True | False |
| Rate of GetHLSMasterPlaylistAPI requests per session | 5.0 | None | True | False |
| Rate of GetHLSMediaPlaylistAPI requests per session | 5.0 | None | True | False |
| Rate of GetHLSStreamingSessionURLAPI requests per stream | 25.0 | None | True | False |
| Rate of GetICEServerConfigAPI requests per signaling channel | 5.0 | None | False | False |
| Rate of GetMP4InitFragmentAPI requests per session | 5.0 | None | True | False |
| Rate of GetMP4MediaFragmentAPI requests per session | 20.0 | None | True | False |
| Rate of GetMediaAPI requests per stream | 5.0 | None | True | False |
| Rate of GetSignalingChannelEndpointAPI requests | 300.0 | None | True | False |
| Rate of GetSignalingChannelEndpointAPI requests per signaling channel | 5.0 | None | True | False |
| Rate of GetTSFragmentAPI requests per session | 20.0 | None | True | False |
| Rate of ListSignalingChannelsAPI requests | 50.0 | None | True | False |
| Rate of ListStreamsAPI requests | 50.0 | None | True | False |
| Rate of ListTagsForResourceAPI requests | 50.0 | None | True | False |
| Rate of ListTagsForResourceAPI requests per resource | 5.0 | None | True | False |
| Rate of ListTagsForStreamAPI requests | 50.0 | None | True | False |
| Rate of ListTagsForStreamAPI requests per stream | 5.0 | None | True | False |
| Rate of PutMediaAPI requests per stream | 5.0 | None | True | False |
| Rate of SendAlexaOfferToMasterAPI requests per signaling channel | 5.0 | None | False | False |
| Rate of SendICECandidateAPI requests per websocket connection | 20.0 | None | False | False |
| Rate of SendSDPAnswerAPI requests per websocket connection | 5.0 | None | False | False |
| Rate of SendSDPOfferAPI requests per websocket connection | 5.0 | None | False | False |
| Rate of TagResourceAPI requests | 50.0 | None | True | False |
| Rate of TagResourceAPI requests per resource | 5.0 | None | True | False |
| Rate of TagStreamAPI requests | 50.0 | None | True | False |
| Rate of TagStreamAPI requests per stream | 5.0 | None | True | False |
| Rate of UntagResourceAPI requests | 50.0 | None | True | False |
| Rate of UntagResourceAPI requests per resource | 5.0 | None | True | False |
| Rate of UntagStreamAPI requests | 50.0 | None | True | False |
| Rate of UntagStreamAPI requests per stream | 5.0 | None | True | False |
| Rate of UpdateDataRetentionAPI requests | 50.0 | None | True | False |
| Rate of UpdateDataRetentionAPI requests per stream | 5.0 | None | True | False |
| Rate of UpdateSignalingChannelAPI requests | 50.0 | None | True | False |
| Rate of UpdateSignalingChannelAPI requests per signaling channel | 5.0 | None | True | False |
| Rate of UpdateStreamAPI requests | 50.0 | None | True | False |
| Rate of UpdateStreamAPI requests per stream | 5.0 | None | True | False |
| Rate of archived fragment media per stream | 500.0 | None | True | False |
| Rate of archived fragment metadata per stream | 10000.0 | None | True | False |
| SendICECandidate message payload size | 10.0 | Kilobytes | False | False |
| SendSDPAnswer message payload size | 10.0 | Kilobytes | False | False |
| SendSDPOffer message payload size | 10.0 | Kilobytes | False | False |
| TURN session bandwidth | 5.0 | Megabits | False | False |
| TURN session concurrent allocations per signaling channel | 50.0 | None | False | False |
| TURN session expiration | 300.0 | Seconds | False | False |

## AWS Key Management Service (AWS KMS) (AWS Service: kms)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Aliases per CMK | 50.0 | None | True | False |
| CancelKeyDeletion request rate | 5.0 | None | True | False |
| ConnectCustomKeyStore request rate | 5.0 | None | True | False |
| CreateAlias request rate | 5.0 | None | True | False |
| CreateCustomKeyStore request rate | 5.0 | None | True | False |
| CreateGrant request rate | 50.0 | None | True | False |
| CreateKey request rate | 5.0 | None | True | False |
| Cryptographic operations (ECC) request rate | 300.0 | None | True | False |
| Cryptographic operations (RSA) request rate | 500.0 | None | True | False |
| Cryptographic operations (symmetric) request rate | 10000.0 | None | True | False |
| Customer Master Keys (CMKs) | 100000.0 | None | True | False |
| DeleteAlias request rate | 15.0 | None | True | False |
| DeleteCustomKeyStore request rate | 5.0 | None | True | False |
| DeleteImportedKeyMaterial request rate | 5.0 | None | True | False |
| DescribeCustomKeyStores request rate | 5.0 | None | True | False |
| DescribeKey request rate | 2000.0 | None | True | False |
| DisableKey request rate | 5.0 | None | True | False |
| DisableKeyRotation request rate | 5.0 | None | True | False |
| DisconnectCustomKeyStore request rate | 5.0 | None | True | False |
| EnableKey request rate | 5.0 | None | True | False |
| EnableKeyRotation request rate | 15.0 | None | True | False |
| GenerateDataKeyPair (ECC_NIST_P256) request rate | 25.0 | None | True | False |
| GenerateDataKeyPair (ECC_NIST_P384) request rate | 10.0 | None | True | False |
| GenerateDataKeyPair (ECC_NIST_P521) request rate | 5.0 | None | True | False |
| GenerateDataKeyPair (ECC_SECG_P256K1) request rate | 25.0 | None | True | False |
| GenerateDataKeyPair (RSA_2048) request rate | 1.0 | None | True | False |
| GenerateDataKeyPair (RSA_3072) request rate | 0.5 | None | True | False |
| GenerateDataKeyPair (RSA_4096) request rate | 0.1 | None | True | False |
| GetKeyPolicy request rate | 1000.0 | None | True | False |
| GetKeyRotationStatus request rate | 1000.0 | None | True | False |
| GetParametersForImport request rate | 0.25 | None | True | False |
| GetPublicKey request rate | 2000.0 | None | True | False |
| Grants per CMK | 50000.0 | None | True | False |
| ImportKeyMaterial request rate | 5.0 | None | True | False |
| Key policy document size | 32768.0 | Bytes | False | False |
| ListAliases request rate | 500.0 | None | True | False |
| ListGrants request rate | 100.0 | None | True | False |
| ListKeyPolicies request rate | 100.0 | None | True | False |
| ListKeys request rate | 500.0 | None | True | False |
| ListResourceTags request rate | 2000.0 | None | True | False |
| ListRetirableGrants request rate | 100.0 | None | True | False |
| PutKeyPolicy request rate | 15.0 | None | True | False |
| ReplicateKey request rate | 5.0 | None | True | False |
| RetireGrant request rate | 30.0 | None | True | False |
| RevokeGrant request rate | 30.0 | None | True | False |
| ScheduleKeyDeletion request rate | 15.0 | None | True | False |
| TagResource request rate | 10.0 | None | True | False |
| UntagResource request rate | 5.0 | None | True | False |
| UpdateAlias request rate | 5.0 | None | True | False |
| UpdateCustomKeyStore request rate | 5.0 | None | True | False |
| UpdateKeyDescription request rate | 5.0 | None | True | False |
| UpdatePrimaryRegion request rate | 5.0 | None | True | False |

## AWS Lake Formation (AWS Service: lakeformation)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Length of a path that can be registered | 700.0 | None | True | False |
| Number of data lake administrators | 30.0 | None | True | False |
| Number of lf tag per account | 1000.0 | None | True | False |
| Number of lf tag policy per principal per resource type | 50.0 | None | True | False |
| Number of registered paths | 10000.0 | None | True | False |
| Number of subfolders in an Amazon S3 path | 20.0 | None | True | False |
| Number of tag values per lf tag | 15.0 | None | True | False |

## AWS Lambda (AWS Service: lambda)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Asynchronous payload | 256.0 | Kilobytes | False | False |
| Burst concurrency | 500.0 | None | False | False |
| Concurrent executions | 1000.0 | None | True | False |
| Deployment package size (console editor) | 3.0 | Megabytes | False | False |
| Deployment package size (direct upload) | 50.0 | Megabytes | False | False |
| Deployment package size (unzipped) | 250.0 | Megabytes | False | False |
| Elastic network interfaces per VPC | 250.0 | None | True | False |
| Environment variable size | 4.0 | Kilobytes | False | False |
| File descriptors | 1024.0 | None | False | False |
| Function and layer storage | 75.0 | Gigabytes | True | False |
| Function layers | 5.0 | None | False | False |
| Function memory maximum | 10240.0 | Megabytes | False | False |
| Function memory minimum | 128.0 | Megabytes | False | False |
| Function resource-based policy | 20.0 | Kilobytes | False | False |
| Function timeout | 900.0 | None | False | False |
| Processes and threads | 1024.0 | None | False | False |
| Rate of GetFunction API requests | 100.0 | None | False | False |
| Rate of GetPolicy API requests | 15.0 | None | False | False |
| Rate of control plane API requests (excludes invocation, GetFunction, and GetPolicy requests) | 15.0 | None | False | False |
| Synchronous payload | 6.0 | Megabytes | False | False |
| Temporary storage | 512.0 | Megabytes | False | False |
| Test events (console editor) | 10.0 | None | False | False |

## AWS Launch Wizard (AWS Service: launchwizard)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Active applications | 25.0 | None | True | False |
| Application name length | 10.0 | None | False | False |
| Applications | 150.0 | None | True | False |
| Parallel deployments | 3.0 | None | False | False |

## Amazon Lex (AWS Service: lex)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Bot channel associations per bot alias (V2) | 10.0 | None | False | False |
| Bots per account (V2) | 100.0 | None | True | False |
| Characters per custom slot type value (V2) | 500.0 | None | False | False |
| Characters per sample utterance (V2) | 500.0 | None | False | False |
| Custom slot type values and synonyms per bot locale (V2) | 50000.0 | None | False | False |
| Custom slot types per bot locale (V2) | 100.0 | None | False | False |
| Sample utterances per intent (V2) | 1500.0 | None | True | False |
| Sample utterances per slot (V2) | 10.0 | None | True | False |
| Slots per bot locale (V2) | 2000.0 | None | False | False |
| Slots per intent (V2) | 100.0 | None | False | False |
| Total characters in sample utterances per bot locale (V2) | 200000.0 | None | False | False |
| Values and synonyms per custom slot type (V2) | 10000.0 | None | False | False |
| Versions per bot (V2) | 100.0 | None | False | False |

## AWS License Manager (AWS Service: license-manager)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Extend license consumption per consumption token | 1.0 | None | False | False |
| GetAccessTokens calls | 10.0 | None | False | False |
| License configuration associations per resource | 10.0 | None | True | False |
| License configurations | 25.0 | None | True | False |
| License conversion tasks per resource per day | 5.0 | None | True | False |
| Maximum number of concurrent organization grant activities | 10.0 | None | False | False |
| Number of Report generators | 25.0 | None | False | False |
| Number of account discovery mode updates per day | 1.0 | None | False | False |
| Number of grants per license | 2000.0 | None | False | False |
| Number of licenses you can create | 2000.0 | None | False | False |
| Number of received licenses per product | 10.0 | None | False | False |
| Number of tokens per account and license | 10.0 | None | False | False |
| Number of updates for a report generator per day | 25.0 | None | False | False |
| Total number counted entitlements per checkout | 5.0 | None | False | False |
| Total number counted entitlements per license | 25.0 | None | False | False |
| Total number uncounted entitlements per license | 25.0 | None | False | False |

## AWS License Manager User Subscriptions (AWS Service: license-manager-user-subscriptions)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Instance associations per user | 25.0 | None | True | False |
| User-based subscriptions for Visual Studio Enterprise | 30.0 | None | True | False |
| User-based subscriptions for Visual Studio Professional | 50.0 | None | True | False |

## Amazon Lightsail (AWS Service: lightsail)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Allowed cookies per cache behavior for a distribution | 10.0 | None | False | False |
| Allowed headers per cache behavior for a distribution | 10.0 | None | False | False |
| Allowed query strings per cache behavior for a distribution | 10.0 | None | False | False |
| Block storage disks per instance | 15.0 | None | False | False |
| Container service certificates | 4.0 | None | False | False |
| Container service custom domains | 4.0 | None | False | False |
| Container service deployment containers | 10.0 | None | False | False |
| Container service deployment versions | 50.0 | None | False | False |
| Container service logs storage days | 4.0 | None | False | False |
| Container service nodes | 20.0 | None | False | False |
| Container service stored container images | 150.0 | None | False | False |
| Container services | 100.0 | None | False | False |
| Custom domain names per distribution | 10.0 | None | False | False |
| DNS zones (or domains) | 3.0 | None | False | False |
| Data transfer rate per distribution | 150.0 | None | False | False |
| Databases | 40.0 | None | False | False |
| Default behaviors (default cache behavior) per distribution | 1.0 | None | False | False |
| Directory and file overrides per distribution | 25.0 | None | False | False |
| Distributions | 20.0 | None | False | False |
| Instances | 20.0 | None | True | False |
| Load balancers | 5.0 | None | False | False |
| Maximum active certificates | 10.0 | None | False | False |
| Maximum block storage disk space | 16000.0 | Gigabytes | False | False |
| Maximum buckets per account | 20.0 | None | False | False |
| Maximum certificates | 20.0 | None | False | False |
| Maximum keys per bucket | 2.0 | None | False | False |
| Minimum block storage disk space | 8.0 | Gigabytes | False | False |
| Origins per distribution | 1.0 | None | False | False |
| Parallel RDP connections using the browser-based RDP client | 1.0 | None | False | False |
| Parallel SSH connections using the browser-based SSH client | 5.0 | None | False | False |
| Response timeout per origin for a distribution | 60.0 | Seconds | False | False |
| Static IP addresses | 5.0 | None | True | False |
| Tags | 50.0 | None | False | False |
| Total attached block storage disk space | 20000.0 | Gigabytes | False | False |

## Amazon CloudWatch Logs (AWS Service: logs)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Active export task | 1.0 | None | False | False |
| AssociateKmsKey throttle limit in transactions per second | 5.0 | None | False | False |
| Batch size | 1.0 | Megabytes | False | False |
| CancelExportTask throttle limit in transactions per second | 5.0 | None | False | False |
| CreateExportTask throttle limit in transactions per second | 5.0 | None | False | False |
| CreateLogGroup throttle limit in transactions per second | 5.0 | None | True | False |
| CreateLogStream throttle limit in transactions per second | 50.0 | None | True | False |
| Data archiving | 5.0 | Gigabytes | False | False |
| DeleteDestination throttle limit in transactions per second | 5.0 | None | False | False |
| DeleteLogGroup throttle limit in transactions per second | 5.0 | None | True | False |
| DeleteLogStream throttle limit in transactions per second | 5.0 | None | False | False |
| DeleteMetricFilter throttle limit in transactions per second | 5.0 | None | False | False |
| DeleteRetentionPolicy throttle limit in transactions per second | 5.0 | None | False | False |
| DeleteSubscriptionFilter throttle limit in transactions per second | 5.0 | None | False | False |
| DescribeDestinations throttle limit in transactions per second | 5.0 | None | False | False |
| DescribeExportTasks throttle limit in transactions per second | 5.0 | None | False | False |
| DescribeLogGroups throttle limit in transactions per second | 5.0 | None | True | False |
| DescribeLogStreams throttle limit in transactions per second | 5.0 | None | True | False |
| DescribeMetricFilters throttle limit in transactions per second | 5.0 | None | False | False |
| DescribeSubscriptionFilters throttle limit in transactions per second | 5.0 | None | False | False |
| Event size | 256.0 | Kilobytes | False | False |
| FilterLogEvents throttle limit in transactions per second | 10.0 | None | False | False |
| GetLogEvents throttle limit in transactions per second | 25.0 | None | False | False |
| GetQueryResults  throttle limit in transactions per second | 5.0 | None | False | False |
| ListTagsLogGroup throttle limit in transactions per second | 5.0 | None | False | False |
| Log groups | 1000000.0 | None | True | False |
| Metrics filters per log group | 100.0 | None | False | False |
| PutDestination throttle limit in transactions per second | 5.0 | None | False | False |
| PutDestinationPolicy throttle limit in transactions per second | 5.0 | None | False | False |
| PutLogEvents throttle limit in transactions per second | 800.0 | None | True | False |
| PutMetricFilter throttle limit in transactions per second | 5.0 | None | False | False |
| PutRetentionPolicy throttle limit in transactions per second | 5.0 | None | False | False |
| PutSubscriptionFilter throttle limit in transactions per second | 5.0 | None | False | False |
| StartQuery throttle limit in transactions per second | 5.0 | None | False | False |
| Subscription filters per log group | 2.0 | None | False | False |
| TagLogGroup throttle limit in transactions per second | 5.0 | None | False | False |
| TestMetricFilter throttle limit in transactions per second | 5.0 | None | False | False |
| UntagLogGroup throttle limit in transactions per second | 5.0 | None | False | False |

## Amazon Macie (AWS Service: macie2)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Apache Avro container (.avro) file size | 8.0 | Gigabytes | False | False |
| Apache Parquet (.parquet) file size | 8.0 | Gigabytes | False | False |
| Custom data identifiers per account | 10000.0 | None | False | False |
| Custom data identifiers per sensitive data discovery job | 30.0 | None | False | False |
| Extracted archive bytes | 10.0 | Gigabytes | False | False |
| Extracted archive files | 1000000.0 | None | False | False |
| Findings rules | 1000.0 | None | False | False |
| Full names detected | 1000.0 | None | False | False |
| GNU Zip compressed archive (.gz or .gzip) file size | 8.0 | Gigabytes | False | False |
| Mailing addresses detected | 1000.0 | None | False | False |
| Member accounts by invitation | 1000.0 | None | False | False |
| Member accounts through AWS Organizations | 5000.0 | None | False | False |
| Microsoft Excel workbook (.xls or .xlsx) file size | 512.0 | Megabytes | False | False |
| Microsoft Word document (.doc or .docx) file size | 512.0 | Megabytes | False | False |
| Nested levels | 10.0 | None | False | False |
| Nested levels in structured data | 256.0 | None | False | False |
| Non-binary text file size | 20.0 | Gigabytes | False | False |
| Portable Document Format (.pdf) file size | 1024.0 | Megabytes | False | False |
| S3 buckets per sensitive data discovery job | 1000.0 | None | False | False |
| Sensitive data discovery occurrences | 1000.0 | None | False | False |
| Sensitive data discovery per month per account | 5.0 | Terabytes | True | False |
| Sensitive data finding occurrences | 15.0 | None | False | False |
| TAR archive (.tar) file size | 20.0 | Gigabytes | False | False |
| ZIP compressed archive (.zip) file size | 8.0 | Gigabytes | False | False |

## Amazon Managed Blockchain (AWS Service: managedblockchain)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Number of Hyperledger Fabric channels per Standard Edition network | 8.0 | None | True | False |
| Number of Hyperledger Fabric channels per Starter Edition network | 8.0 | None | True | False |
| Number of Standard Edition networks in which an AWS account can have a member | 6.0 | None | True | False |
| Number of starter Edition networks in which an AWS account can have a member | 6.0 | None | True | False |

## AWS Elemental MediaConnect (AWS Service: mediaconnect)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Entitlements | 50.0 | None | False | False |
| Flows | 20.0 | None | True | False |
| Outputs | 50.0 | None | False | False |

## AWS Elemental MediaConvert (AWS Service: mediaconvert)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Concurrent jobs across all on-demand queues, baseline | 20.0 | None | True | False |
| Concurrent jobs per on-demand queue, peak | 100.0 | None | True | False |
| Custom job templates | 100.0 | None | True | False |
| Custom output presets | 100.0 | None | True | False |
| Queues (on-demand) per Region, per account | 10.0 | None | True | False |
| Queues (reserved) per Region, per account | 30.0 | None | True | False |
| Request rate for API calls in aggregate | 2.0 | None | True | False |
| Request rate for API calls in aggregate, in a burst | 100.0 | None | True | False |
| Request rate for DescribeEndpoints | 0.01667 | None | False | False |
| Request rate for DescribeEndpoints, in a burst | 0.0 | None | False | False |

## AWS Elemental MediaLive (AWS Service: medialive)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| CDI Channels | 2.0 | None | True | False |
| Channels | 5.0 | None | True | False |
| Device Inputs | 100.0 | None | True | False |
| HEVC Channels | 5.0 | None | True | False |
| Input Security Groups | 5.0 | None | True | False |
| Multiplexes | 2.0 | None | True | False |
| Pull Inputs | 100.0 | None | True | False |
| Push Inputs | 5.0 | None | True | False |
| Reservations | 50.0 | None | True | False |
| UHD Channels | 1.0 | None | True | False |
| VPC Inputs | 50.0 | None | True | False |

## AWS Elemental MediaPackage (AWS Service: mediapackage)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Assets per packaging group | 10000.0 | None | True | False |
| Burst rate of REST API requests (Live) | 50.0 | None | False | False |
| Burst rate of REST API requests (VOD) | 50.0 | None | False | False |
| Channels | 30.0 | None | True | False |
| Concurrent harvest jobs | 10.0 | None | True | False |
| Content retention | 336.0 | None | False | False |
| Endpoints per channel | 10.0 | None | True | False |
| Ingest streams per asset | 20.0 | None | False | False |
| Ingest streams per channel | 20.0 | None | False | False |
| Live manifest length | 5.0 | None | True | False |
| Packaging configurations per packaging group | 10.0 | None | True | False |
| Packaging groups | 10.0 | None | True | False |
| Rate of REST API requests (Live) | 5.0 | None | False | False |
| Rate of REST API requests (VOD) | 5.0 | None | False | False |
| Rate of ingest requests per channel | 50.0 | None | False | False |
| Rate of manifest egress requests per asset | 1000.0 | None | False | False |
| Rate of manifest egress requests per origin endpoint | 5000.0 | None | False | False |
| Rate of segment egress requests per asset | 600.0 | None | False | False |
| Rate of segment egress requests per origin endpoint | 300.0 | None | False | False |
| Time-shifted manifest length | 24.0 | None | False | False |
| Tracks per ingest stream (Live) | 10.0 | None | False | False |
| Tracks per ingest stream (VOD) | 10.0 | None | False | False |

## AWS Elemental MediaStore (AWS Service: mediastore)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Containers | 100.0 | None | False | False |
| Folder levels | 10.0 | None | False | False |
| Object size | 25.0 | Megabytes | False | False |
| Rate of DeleteObject API requests | 100.0 | None | True | False |
| Rate of DescribeObject API requests | 1000.0 | None | True | False |
| Rate of GetObject API requests for standard upload availability | 1000.0 | None | True | False |
| Rate of GetObject API requests for streaming upload availability | 25.0 | None | True | False |
| Rate of ListItems API requests | 5.0 | None | True | False |
| Rate of PutObject API requests for chunked transfer encoding (also known as streaming upload availability) | 10.0 | None | True | False |
| Rate of PutObject API requests for standard upload availability | 100.0 | None | True | False |

## Application Migration (AWS Service: mgn)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Concurrent jobs in progress | 20.0 | None | False | False |
| Max Active Source Servers | 20.0 | None | True | False |
| Max Non-Archived Source Servers | 4000.0 | None | False | False |
| Max Source Servers in a single Job | 200.0 | None | False | False |
| Max Source Servers in all Jobs | 200.0 | None | False | False |
| Max Total Source Servers Per AWS Account | 50000.0 | None | False | False |
| Max concurrent Jobs per Source Server | 1.0 | None | False | False |

## Migration Hub Orchestrator (AWS Service: migrationhuborchestrator)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Maximum step groups per workflow | 15.0 | None | True | False |
| Maximum steps per step group | 15.0 | None | True | False |
| Maximum workflows | 50.0 | None | True | False |

## Migration Hub Strategy Recommendations (AWS Service: migrationhubstrategy)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Active Assessment Maximum | 1.0 | None | True | False |
| Active Import Maximum | 5.0 | None | True | False |
| Assessment Maximum | 50.0 | None | True | False |
| Maximum Server per Assessment | 300.0 | None | True | False |

## Amazon CloudWatch (AWS Service: monitoring)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Actions per CloudWatch alarm, per state | 5.0 | None | False | False |
| Canary limit | 200.0 | None | True | False |
| Data retention | 15.0 | None | False | False |
| Dimensions per metric | 10.0 | None | False | False |
| Groups limit | 20.0 | None | True | False |
| Metric data queries per GetMetricData request | 500.0 | None | False | False |
| MetricDatum items per PutMetricData request | 20.0 | None | False | False |
| Metrics per dashboard | 2500.0 | None | False | False |
| Metrics per dashboard widget | 500.0 | None | False | False |
| Minimum frequency | 60000.0 | Milliseconds | False | False |
| Number of Contributor Insights rules | 100.0 | None | True | False |
| Payload size for PutMetricData requests | 40.0 | None | False | False |
| Rate of DeleteAlarms requests | 3.0 | None | False | False |
| Rate of DeleteDashboards requests | 10.0 | None | True | False |
| Rate of DeleteInsightRules requests | 5.0 | None | False | False |
| Rate of DeleteMetricStream requests | 10.0 | None | True | False |
| Rate of DescribeAlarmHistory requests | 3.0 | None | False | False |
| Rate of DescribeAlarms requests | 9.0 | None | True | False |
| Rate of DescribeAlarmsForMetric requests | 3.0 | None | False | False |
| Rate of DescribeInsightRules requests | 20.0 | None | False | False |
| Rate of DisableAlarmActions requests | 3.0 | None | False | False |
| Rate of DisableInsightRules requests | 1.0 | None | False | False |
| Rate of EnableAlarmActions requests | 3.0 | None | False | False |
| Rate of EnableInsightRules requests | 1.0 | None | False | False |
| Rate of GetDashboard requests | 10.0 | None | True | False |
| Rate of GetInsightRuleReport requests | 20.0 | None | True | False |
| Rate of GetMetricData datapoints for metrics older than three hours | 396000.0 | None | False | False |
| Rate of GetMetricData datapoints for the last three hours of metrics | 180000.0 | None | False | False |
| Rate of GetMetricData requests | 50.0 | None | True | False |
| Rate of GetMetricStatistics requests | 400.0 | None | True | False |
| Rate of GetMetricStream requests | 10.0 | None | True | False |
| Rate of GetMetricWidgetImage requests | 20.0 | None | True | False |
| Rate of ListDashboards requests | 10.0 | None | True | False |
| Rate of ListMetricStreams requests | 10.0 | None | True | False |
| Rate of ListMetrics requests | 50.0 | None | True | False |
| Rate of ListTagsForResource requests | 10.0 | None | False | False |
| Rate of PutDashboard requests | 10.0 | None | True | False |
| Rate of PutInsightRule requests | 5.0 | None | False | False |
| Rate of PutMetricAlarm requests | 3.0 | None | True | False |
| Rate of PutMetricData requests | 500.0 | None | True | False |
| Rate of PutMetricStream requests | 10.0 | None | True | False |
| Rate of SetAlarmState requests | 3.0 | None | False | False |
| Rate of StartMetricStreams requests | 10.0 | None | True | False |
| Rate of StopMetricStreams requests | 10.0 | None | True | False |
| Rate of TagResource requests | 1.0 | None | False | False |
| Rate of UntagResource requests | 1.0 | None | False | False |

## Amazon MQ (AWS Service: mq)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| API burst limit | 100.0 | None | False | False |
| API rate limit | 15.0 | None | False | False |
| Destinations monitored in CloudWatch (ActiveMQ) | 200.0 | None | False | False |
| Destinations monitored in CloudWatch (RabbitMQ) | 500.0 | None | False | False |
| Groups per user (simple auth) | 20.0 | None | False | False |
| Job scheduler usage limit per broker backed by Amazon EBS | 50.0 | Gigabytes | False | False |
| Number of brokers, per region | 50.0 | None | True | False |
| Revisions per configuration | 300.0 | None | False | False |
| Security groups per broker | 5.0 | None | False | False |
| Storage capacity per larger broker | 200.0 | Gigabytes | False | False |
| Storage capacity per smaller broker | 20.0 | Gigabytes | False | False |
| Tags per broker | 50.0 | None | False | False |
| Temporary storage capacity per larger broker | 50.0 | Gigabytes | False | False |
| Temporary storage capacity per smaller broker | 5.0 | Gigabytes | False | False |
| Users per broker (simple auth) | 250.0 | None | False | False |
| Wire-level connections per larger broker | 1000.0 | None | True | False |
| Wire-level connections per smaller broker | 100.0 | None | True | False |

## Amazon Neptune (AWS Service: neptune)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Cluster endpoints per DB cluster | 5.0 | None | True | False |
| Cross-region snapshot copy requests | 5.0 | None | True | False |
| DB cluster Roles | 5.0 | None | True | False |
| DB cluster manuals snapshots | 100.0 | None | True | False |
| DB cluster parameter groups | 50.0 | None | True | False |
| DB clusters | 40.0 | None | True | False |
| DB instance parameter groups | 50.0 | None | True | False |
| DB instances | 40.0 | None | True | False |
| DB subnet groups | 50.0 | None | True | False |
| Event subscriptions | 20.0 | None | True | False |
| Read replicas per cluster | 15.0 | None | False | False |
| Reserved DB instances | 40.0 | None | True | False |
| Tags per resource | 50.0 | None | True | False |

## AWS Network Firewall (AWS Service: network-firewall)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Firewall policies | 20.0 | None | True | False |
| Firewalls | 5.0 | None | True | False |
| Stateful rulegroups | 50.0 | None | True | False |
| Stateless rulegroups | 50.0 | None | True | False |

## Network Insights (AWS Service: networkinsights)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Network Access Analyzer Access Scope Analyses | 10000.0 | None | True | False |
| Network Access Analyzer Access Scopes | 1000.0 | None | True | False |
| Network Access Analyzer Concurrent Access Scope Analyses | 25.0 | None | True | False |
| Reachability Analyzer Analyses | 1000.0 | None | True | False |
| Reachability Analyzer Paths | 100.0 | None | True | False |
| Reachability Analyzer concurrent Analyses | 6.0 | None | True | False |

## Amazon Nimble Studio (AWS Service: nimble)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Active Directory studio components per studio | 1.0 | None | False | False |
| Custom streaming images per studio | 10.0 | None | True | False |
| G5 streaming sessions per studio | 0.0 | None | True | False |
| Launch profiles per studio | 50.0 | None | True | False |
| Shared file system studio components per studio | 10.0 | None | True | False |
| Streaming sessions per studio | 2.0 | None | True | False |
| Studio components per studio | 50.0 | None | True | False |
| Studio creation per account | 1.0 | None | False | False |

## AWS OpsWorks Stacks (AWS Service: opsworks)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Apps per stack | 40.0 | None | True | False |
| Instances per stack | 40.0 | None | True | False |
| Layers per stack | 40.0 | None | True | False |
| Stacks | 40.0 | None | True | False |

## AWS Outposts (AWS Service: outposts)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Outpost sites | 100.0 | None | True | False |
| Outposts per site | 10.0 | None | True | False |

## Amazon Personalize (AWS Service: personalize)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Active campaigns | 20.0 | None | True | False |
| Active dataset groups | 500.0 | None | False | False |
| Active datasets | 500.0 | None | False | False |
| Active event trackers | 500.0 | None | False | False |
| Active filters | 10.0 | None | True | False |
| Active solutions | 500.0 | None | False | False |
| Amount of data for HRNN recipe | 100.0 | Gigabytes | False | False |
| Amount of data for Personalized-Ranking recipe | 100.0 | Gigabytes | False | False |
| Amount of data for Popularity-Count recipe | 100.0 | Gigabytes | False | False |
| Amount of data for SIMS recipe | 100.0 | Gigabytes | False | False |
| Amount of interactions data for HRNN-coldstart recipe | 100.0 | Gigabytes | False | False |
| Amount of interactions data for HRNN-metadata recipe | 100.0 | Gigabytes | False | False |
| Amount of users and items data combined for HRNN-coldstart recipe | 5.0 | Gigabytes | False | False |
| Amount of users and items data combined for HRNN-metadata recipe | 5.0 | Gigabytes | False | False |
| Event size | 10.0 | Kilobytes | False | False |
| Maximum number of recommenders per account | 15.0 | None | True | False |
| Minimum data points for model training | 1000.0 | None | False | False |
| Minimum unique users for model training | 25.0 | None | False | False |
| Number of events in PutEvents call | 10.0 | None | False | False |
| Number of interactions for model training | 500000000.0 | None | False | False |
| Number of items used in model training | 750000.0 | None | False | False |
| Number of schemas | 500.0 | None | False | False |
| Pending or In Progress batch inference jobs | 5.0 | None | True | False |
| Pending or In Progress solution versions | 20.0 | None | True | False |
| Rate of CreateCampaign requests | 1.0 | None | False | False |
| Rate of CreateDataset requests | 1.0 | None | False | False |
| Rate of CreateDatasetGroup requests | 1.0 | None | False | False |
| Rate of CreateDatasetImportJob requests | 1.0 | None | False | False |
| Rate of CreateEventTracker requests | 1.0 | None | False | False |
| Rate of CreateSchema requests | 1.0 | None | False | False |
| Rate of CreateSolution requests | 1.0 | None | False | False |
| Rate of CreateSolutionVersion requests | 1.0 | None | False | False |
| Rate of DeleteCampaign requests | 1.0 | None | False | False |
| Rate of DeleteDataset requests | 1.0 | None | False | False |
| Rate of DeleteDatasetGroup requests | 1.0 | None | False | False |
| Rate of DeleteDatasetImportJob requests | 1.0 | None | False | False |
| Rate of DeleteEventTracker requests | 1.0 | None | False | False |
| Rate of DeleteSchema requests | 1.0 | None | False | False |
| Rate of DeleteSolution requests | 1.0 | None | False | False |
| Rate of DescribeAlgorithm requests | 1.0 | None | False | False |
| Rate of DescribeCampaign requests | 1.0 | None | False | False |
| Rate of DescribeDataset requests | 1.0 | None | False | False |
| Rate of DescribeDatasetGroup requests | 1.0 | None | False | False |
| Rate of DescribeDatasetImportJob requests | 1.0 | None | False | False |
| Rate of DescribeEventTracker requests | 1.0 | None | False | False |
| Rate of DescribeFeatureTransformation requests | 1.0 | None | False | False |
| Rate of DescribeRecipe requests | 1.0 | None | False | False |
| Rate of DescribeSchema requests | 1.0 | None | False | False |
| Rate of DescribeSolution requests | 1.0 | None | False | False |
| Rate of GetPersonalizedRanking requests per campaign | 500.0 | None | False | False |
| Rate of GetRecommendations requests per campaign | 500.0 | None | False | False |
| Rate of GetSolutionMetrics requests | 1.0 | None | False | False |
| Rate of ListCampaigns requests | 1.0 | None | False | False |
| Rate of ListDatasetGroups requests | 1.0 | None | False | False |
| Rate of ListDatasetImportJobRuns requests | 1.0 | None | False | False |
| Rate of ListDatasetImportJobs requests | 1.0 | None | False | False |
| Rate of ListDatasets requests | 1.0 | None | False | False |
| Rate of ListEventTrackers requests | 1.0 | None | False | False |
| Rate of ListRecipes requests | 1.0 | None | False | False |
| Rate of ListSchemas requests | 1.0 | None | False | False |
| Rate of ListSolutionVersions requests | 1.0 | None | False | False |
| Rate of ListSolutions requests | 1.0 | None | False | False |
| Rate of PutEvents requests | 1000.0 | None | True | False |
| Rate of UpdateCampaign requests | 1.0 | None | False | False |
| Rate of UpdateDataset requests | 1.0 | None | False | False |
| Rate of transactions per account | 2500.0 | None | False | False |

## Amazon Pinpoint (AWS Service: pinpoint)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| APNs sandbox message payload size per message | 4.0 | Kilobytes | False | False |
| Active campaigns per account | 200.0 | None | True | False |
| All other operations burst quota | 300.0 | None | False | False |
| All other operations rate quota | 300.0 | None | False | False |
| Amazon Device Messaging (ADM) message payload size per message | 6.0 | Kilobytes | False | False |
| Apple Push Notification service (APNs) message payload size per message | 4.0 | Kilobytes | False | False |
| Attribute name length | 50.0 | None | False | False |
| Attribute value length | 100.0 | None | False | False |
| Baidu Cloud Push message payload size per message | 4.0 | Kilobytes | False | False |
| CreateCampaign operation burst quota | 25.0 | None | False | False |
| CreateCampaign operation rate quota | 25.0 | None | False | False |
| CreateSegment operation burst quota | 25.0 | None | False | False |
| CreateSegment operation rate quota | 25.0 | None | False | False |
| DeleteCampaign operation burst quota | 25.0 | None | False | False |
| DeleteCampaign operation rate quota | 25.0 | None | False | False |
| DeleteEndpoint operation burst quota | 1000.0 | None | False | False |
| DeleteEndpoint operation rate quota | 1000.0 | None | False | False |
| DeleteSegment operation burst quota | 25.0 | None | False | False |
| DeleteSegment operation rate quota | 25.0 | None | False | False |
| Firebase Cloud Messaging (FCM) message payload size per message | 4.0 | Kilobytes | False | False |
| GetEndpoint operation burst quota | 7000.0 | None | False | False |
| GetEndpoint operation rate quota | 7000.0 | None | False | False |
| Import size per import job | 1.0 | None | True | False |
| Invocation payload size | 7.0 | Megabytes | False | False |
| Maximum amount of time to wait for a Lambda function to process data | 15.0 | Seconds | False | False |
| Maximum message size, including attachments | 10.0 | Megabytes | False | False |
| Maximum number of active journeys per account | 50.0 | None | True | False |
| Maximum number of attempts to invoke a Lambda function | 3.0 | Seconds | False | False |
| Maximum number of attribute keys and metric keys for each event per request | 40.0 | None | False | False |
| Maximum number of characters for an event attribute name in a custom channel response | 128.0 | None | False | False |
| Maximum number of characters for an event attribute value in a custom channel response | 128.0 | None | False | False |
| Maximum number of characters in ADM-specific template parts of a push notification template | 4000.0 | None | False | False |
| Maximum number of characters in APN-specific template parts of a push notification template | 2000.0 | None | False | False |
| Maximum number of characters in Baidu-specific template parts of a push notification template | 4000.0 | None | False | False |
| Maximum number of characters in FCM-specific template parts of a push notification template | 4000.0 | None | False | False |
| Maximum number of characters in an SMS template | 1600.0 | None | False | False |
| Maximum number of characters in an email template | 500000.0 | None | False | False |
| Maximum number of characters in the default template parts of a push notification template | 2000.0 | None | False | False |
| Maximum number of characters per attribute key | 50.0 | None | False | False |
| Maximum number of characters per attribute value | 200.0 | None | False | False |
| Maximum number of custom attribute keys per app | 500.0 | None | False | False |
| Maximum number of custom attribute values per attribute key | 100000.0 | None | False | False |
| Maximum number of custom event types per app | 1500.0 | None | False | False |
| Maximum number of custom metric keys per app | 500.0 | None | False | False |
| Maximum number of dimensions that can be used to create a segment | 100.0 | None | False | False |
| Maximum number of event attributes per endpoint in a custom channel response | 5.0 | None | False | False |
| Maximum number of events in a request | 100.0 | None | False | False |
| Maximum number of journey activities per journey | 40.0 | None | True | False |
| Maximum number of message templates per account | 10000.0 | None | True | False |
| Maximum number of model configurations per account | 100.0 | None | False | False |
| Maximum number of model configurations per message template | 1.0 | None | False | False |
| Maximum number of push notifications that can be sent per second in a campaign | 25000.0 | None | True | False |
| Maximum number of versions per template | 5000.0 | None | False | False |
| Maximum segment size per campaign | 100000000.0 | None | False | False |
| Maximum segment size per journey | 100000000.0 | None | False | False |
| Maximum size of a request | 4.0 | Megabytes | False | False |
| Maximum size of an individual event | 1000.0 | Kilobytes | False | False |
| Maximum size of an invocation payload (request and response) for a Lambda function | 6.0 | Megabytes | False | False |
| Maximum size per endpoint | 15.0 | Kilobytes | False | False |
| Number of Amazon Pinpoint projects | 100.0 | None | False | False |
| Number of Amazon SNS topics for two-way SMS per account | 100000.0 | None | True | False |
| Number of EndpointBatchItem objects in an EndpointBatchRequest payload | 100.0 | None | False | False |
| Number of SMS messages that can be sent each second (sending rate) | 20.0 | None | True | False |
| Number of SMS messages that can be sent to a single recipient each second | 1.0 | None | False | False |
| Number of attributes assigned to the Attributes parameter | 250.0 | None | True | False |
| Number of attributes assigned to the Attributes, Metrics, and UserAttributes parameters collectively | 250.0 | None | True | False |
| Number of attributes assigned to the Metrics parameter | 250.0 | None | True | False |
| Number of attributes assigned to the UserAttributes parameter | 250.0 | None | True | False |
| Number of concurrent import jobs | 10.0 | None | True | False |
| Number of emails that can be sent each second (sending rate) | 1.0 | None | True | False |
| Number of emails that can be sent per 24-hour period (sending quota) | 200.0 | None | True | False |
| Number of endpoints with the same user ID | 10.0 | None | False | False |
| Number of event-based campaigns | 25.0 | None | True | False |
| Number of identities that you can verify | 10000.0 | None | False | False |
| Number of recipients per message | 50.0 | None | False | False |
| Number of values assigned to the Attributes parameter attributes per attribute | 50.0 | None | False | False |
| Number of values assigned to the UserAttributes parameter attributes per attribute | 50.0 | None | False | False |
| Number of verified identities | 10000.0 | None | False | False |
| PhoneNumberValidate operation burst quota | 20.0 | None | False | False |
| PhoneNumberValidate operation rate quota | 20.0 | None | False | False |
| PutEvents operation burst quota | 7000.0 | None | False | False |
| PutEvents operation rate quota | 7000.0 | None | False | False |
| SMS spending threshold | 1.0 | None | True | False |
| SendMessages operation burst quota | 4000.0 | None | False | False |
| SendMessages operation rate quota | 4000.0 | None | False | False |
| SendUsersMessages operation burst quota | 6000.0 | None | False | False |
| SendUsersMessages operation rate quota | 6000.0 | None | False | False |
| UpdateCampaign operation burst quota | 25.0 | None | False | False |
| UpdateCampaign operation rate quota | 25.0 | None | False | False |
| UpdateEndpoint operation burst quota | 5000.0 | None | False | False |
| UpdateEndpoint operation rate quota | 5000.0 | None | False | False |
| UpdateEndpointsBatch operation burst quota | 5000.0 | None | False | False |
| UpdateEndpointsBatch operation rate quota | 5000.0 | None | False | False |
| UpdateSegment operation burst quota | 25.0 | None | False | False |
| UpdateSegment operation rate quota | 25.0 | None | False | False |

## Amazon Polly (AWS Service: polly)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Concurrent connections | 90.0 | None | True | False |
| Lexicon count | 100.0 | None | False | False |
| Lexicon size | 4000.0 | None | False | False |
| Rate of GetSpeechSynthesisTask and ListSpeechSynthesisTasks requests | 10.0 | None | True | False |
| Rate of StartSpeechSynthesisTask (neural) requests | 1.0 | None | True | False |
| Rate of StartSpeechSynthesisTask (standard) requests | 10.0 | None | True | False |
| Rate of SynthesizeSpeech (neural) requests | 8.0 | None | True | False |
| Rate of SynthesizeSpeech (standard) requests | 80.0 | None | True | False |
| Rate of lexicon management requests | 2.0 | None | True | False |
| StartSpeechSynthesisTask billed characters count | 100000.0 | None | True | False |
| StartSpeechSynthesisTask lexicon count | 5.0 | None | False | False |
| StartSpeechSynthesisTask total characters limit | 200000.0 | None | True | False |
| SynthesizeSpeech billed character count | 3000.0 | None | True | False |
| SynthesizeSpeech lexicon count | 5.0 | None | False | False |
| SynthesizeSpeech total character count | 6000.0 | None | True | False |

## Amazon Connect Customer Profiles (AWS Service: profile)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Amazon Connect Customer Profiles domain count | 100.0 | None | True | False |
| Keys per object type | 10.0 | None | True | False |
| Maximum expiration in days | 1098.0 | None | True | False |
| Maximum number of integrations | 50.0 | None | True | False |
| Maximum size of all objects for a profile | 51200.0 | Kilobytes | True | False |
| Object and profile maximum size | 250.0 | Kilobytes | False | False |
| Object types per domain | 100.0 | None | True | False |
| Objects per profile | 1000.0 | None | True | False |

## Amazon QLDB (AWS Service: qldb)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Ledgers | 5.0 | None | True | False |
| QLDB exports per ledger | 2.0 | None | True | False |
| QLDB streams per ledger | 5.0 | None | True | False |

## Amazon QuickSight (AWS Service: quicksight)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| API_CREATE-INGESTION: Calls per 24 hour period from Enterprise edition | 32.0 | None | False | False |
| API_CREATE-INGESTION: Calls per 24 hour period from Standard edition | 8.0 | None | False | False |
| Calculated field expression length | 250000.0 | None | False | False |
| Custom action name length | 256.0 | None | False | False |
| Custom actions per visual | 10.0 | None | False | False |
| Data Prep: Fields per dataset | 2000.0 | None | False | False |
| Display items per sheet control | 10000.0 | None | False | False |
| Email aliases per group for email reports | 5000.0 | None | False | False |
| Maximum number of characters per specified Control values | 200000.0 | None | False | False |
| Query timeout for visuals | 120.0 | Seconds | False | False |
| The maximum amount of time to wait for a dataset preview | 45.0 | Seconds | False | False |
| URL action hyperlink length | 2048.0 | None | False | False |

## AWS Resource Access Manager (AWS Service: ram)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Number of pending invitations | 20.0 | None | True | False |
| Number of resource shares | 5000.0 | None | True | False |
| Number of shared resources | 5000.0 | None | True | False |

## Amazon Relational Database Service (Amazon RDS) (AWS Service: rds)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Authorizations per DB security group | 20.0 | None | False | False |
| Custom engine versions | 40.0 | None | True | False |
| DB cluster parameter groups | 50.0 | None | False | False |
| DB clusters | 40.0 | None | True | False |
| DB instances | 40.0 | None | True | False |
| DB subnet groups | 50.0 | None | True | False |
| Data API HTTP request body size | 4.0 | Megabytes | False | False |
| Data API maximum concurrent cluster-secret pairs | 30.0 | None | False | False |
| Data API maximum concurrent requests | 500.0 | None | False | False |
| Data API maximum result set size | 1.0 | Megabytes | False | False |
| Data API maximum size of JSON response string | 10.0 | Megabytes | False | False |
| Data API requests per second | 1000.0 | None | False | False |
| Event subscriptions | 20.0 | None | True | False |
| IAM roles per DB cluster | 5.0 | None | True | False |
| IAM roles per DB instance | 5.0 | None | True | False |
| Manual DB cluster snapshots | 100.0 | None | True | False |
| Manual DB instance snapshots | 100.0 | None | True | False |
| Option groups | 20.0 | None | True | False |
| Parameter groups | 50.0 | None | True | False |
| Proxies | 20.0 | None | True | False |
| Read replicas per master | 5.0 | None | True | False |
| Reserved DB instances | 40.0 | None | True | False |
| Rules per security group | 20.0 | None | False | False |
| Security groups | 25.0 | None | True | False |
| Security groups (VPC) | 5.0 | None | False | False |
| Subnets per DB subnet group | 20.0 | None | False | False |
| Tags per resource | 50.0 | None | False | False |
| Total storage for all DB instances | 100000.0 | Gigabytes | True | False |

## Amazon Redshift (AWS Service: redshift)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| AWS accounts you can authorize to restore a snapshot per AWS KMS key | 100.0 | None | False | False |
| AWS accounts you can authorize to restore a snapshot per snapshot | 20.0 | None | False | False |
| Allowed row object size per ION or JSON file when using Amazon Athena | 8.0 | Megabytes | True | False |
| Allowed string value size per ION or JSON file when using AWS Glue Data Catalog | 16.0 | Kilobytes | True | False |
| Allowed string value size per ION or JSON file when using Amazon Athena | 16.0 | Kilobytes | True | False |
| Cluster IAM roles for Amazon Redshift to access other AWS services | 10.0 | None | False | False |
| Column limit for external tables when using Amazon Athena or AWS Glue Data Catalog | 1600.0 | None | True | False |
| Column limit for external tables with pseudocolumns when using AWS Glue Data Catalog | 1598.0 | None | True | False |
| Column limit for external tables with pseudocolumns when using Amazon Athena | 1598.0 | None | True | False |
| Concurrency level for all user-defined queues | 50.0 | None | False | False |
| Concurrent user connections to a cluster | 500.0 | None | False | False |
| DC2 nodes in a cluster | 128.0 | None | True | False |
| DS2 nodes in a cluster | 128.0 | None | True | False |
| Databases in an account when using AWS Glue Data Catalog | 10000.0 | None | True | False |
| Databases in an account when using Amazon Athena | 10000.0 | None | True | False |
| Event subscriptions | 20.0 | None | True | False |
| Nodes | 200.0 | None | True | False |
| Nodes in a cluster | 128.0 | None | False | False |
| Parameter groups | 20.0 | None | False | False |
| Partitions in a table when using AWS Glue Data Catalog | 1000000.0 | None | True | False |
| Partitions in a table when using Amazon Athena | 1000000.0 | None | True | False |
| Partitions in an account when using AWS Glue Data Catalog | 10000000.0 | None | True | False |
| Partitions in an account when using Amazon Athena | 10000000.0 | None | True | False |
| RA3 nodes in a cluster | 128.0 | None | True | False |
| Reserved nodes | 200.0 | None | True | False |
| Schemas in each database per cluster | 9900.0 | None | False | False |
| Security groups | 20.0 | None | True | False |
| Single row size when loading by COPY | 4.0 | Megabytes | False | False |
| Snapshots | 20.0 | None | True | False |
| Stored procedures in a database | 10000.0 | None | False | False |
| Subnet groups | 20.0 | None | True | False |
| Subnets in a subnet group | 20.0 | None | True | False |
| Tables for 16xlarge cluster node type | 100000.0 | None | False | False |
| Tables for 4xlarge cluster node type | 100000.0 | None | False | False |
| Tables for 8xlarge cluster node type | 100000.0 | None | False | False |
| Tables for large cluster node type | 9900.0 | None | False | False |
| Tables for xlarge cluster node type | 9900.0 | None | False | False |
| Tables for xlplus cluster node type with a multiple-node cluster | 20000.0 | None | False | False |
| Tables for xlplus cluster node type with a single-node cluster | 9900.0 | None | False | False |
| Tables in a database when using AWS Glue Data Catalog | 100000.0 | None | True | False |
| Tables in a database when using Amazon Athena | 100000.0 | None | True | False |
| User-defined databases in a cluster | 60.0 | None | False | False |

## AWS Migration Hub Refactor Spaces (AWS Service: refactor-spaces)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Applications | 600.0 | None | True | False |
| Environments | 50.0 | None | True | False |
| Routes | 1000.0 | None | True | False |
| Services | 500.0 | None | True | False |

## Amazon Rekognition (AWS Service: rekognition)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Amazon Rekognition Custom Labels models per project | 100.0 | None | True | False |
| Amazon Rekognition Custom Labels projects per account | 100.0 | None | True | False |
| Concurrent Amazon Rekognition Custom Labels training jobs per account | 2.0 | None | True | False |
| Concurrent Amazon Rekognition Video stored video jobs per account | 20.0 | None | True | False |
| Concurrently running Amazon Rekognition Custom Labels models per account | 2.0 | None | True | False |
| Maximum inference units per running Amazon Rekognition Custom Labels model. | 5.0 | None | True | False |
| Maximum number of images per Amazon Rekognition Custom Labels detection test dataset | 7000.0 | None | False | False |
| Maximum number of images per Amazon Rekognition Custom Labels detection training dataset | 28000.0 | None | False | False |
| Transactions per second per account for individual Amazon Rekognition Custom Labels data plane operation DetectCustomLabels | 50.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Custom Labels operation CreateProject | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Custom Labels operation CreateProjectVersion | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Custom Labels operation DeleteProject | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Custom Labels operation DeleteProjectVersion | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Custom Labels operation DescribeProjectVersions | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Custom Labels operation DescribeProjects | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Custom Labels operation StartProjectVersion | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Custom Labels operation StopProjectVersion | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation CompareFaces | 25.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation CreateCollection | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation DeleteCollection | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation DeleteFaces | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation DescribeCollection | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation DetectFaces | 25.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation DetectLabels | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation DetectModerationLabels | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation DetectText | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation GetCelebrityInfo | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation IndexFaces | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation ListCollections | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation ListFaces | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation RecognizeCelebrities | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation SearchFaces | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image operation SearchFacesByImage | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Image personal protective equipment operation DetectProtectiveEquipment | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video get operation GetCelebrityRecognition | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video get operation GetContentModeration | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video get operation GetFaceDetection | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video get operation GetFaceSearch | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video get operation GetLabelDetection | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video get operation GetPersonTracking | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video get operation GetSegmentDetection | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video get operation GetTextDetection | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video start operation StartCelebrityRecognition | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video start operation StartContentModeration | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video start operation StartFaceDetection | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video start operation StartFaceSearch | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video start operation StartLabelDetection | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video start operation StartPersonTracking | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video start operation StartSegmentDetection | 5.0 | None | True | False |
| Transactions per second per account for the Amazon Rekognition Video stored video start operation StartTextDetection | 5.0 | None | True | False |

## AWS Resilience Hub (AWS Service: resiliencehub)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Number of Resiliency Policies | 10.0 | None | True | False |
| Number of application components per resource | 5.0 | None | False | False |
| Number of application components per template | 65.0 | None | False | False |
| Number of applications | 10.0 | None | True | False |
| Number of assessments per application per month | 200.0 | None | True | False |
| Number of concurrent assessments per account | 20.0 | None | False | False |
| Number of concurrent assessments per application | 1.0 | None | False | False |
| Number of concurrent recommendation templates per account | 100.0 | None | False | False |
| Number of concurrent recommendation templates per application | 1.0 | None | False | False |
| Number of recommendation templates per application per month | 100.0 | None | True | False |
| Number of resources per template | 100.0 | None | False | False |
| Number of stacks to import | 20.0 | None | False | False |
| Number of terraform state files to import | 20.0 | None | False | False |
| Retention period of past assessments/recommendations in days | 365.0 | None | False | False |
| Retention period of past recommendation templates in days | 365.0 | None | False | False |
| Template size in bytes | 51200.0 | None | False | False |
| Terraform state file maximum size | 4194305.0 | None | False | False |

## AWS Resource Groups (AWS Service: resource-groups)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Resource groups per account | 100.0 | None | True | False |

## IAM Roles Anywhere (AWS Service: rolesanywhere)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| CRLs per trust anchor | 2.0 | None | False | False |
| Certificates per trust anchor | 2.0 | None | False | False |
| Combined rate of CRL requests | 1.0 | None | True | False |
| Combined rate of profile requests | 1.0 | None | True | False |
| Combined rate of subject requests | 1.0 | None | True | False |
| Combined rate of tagging requests | 1.0 | None | True | False |
| Combined rate of trust anchor requests | 1.0 | None | True | False |
| Profiles | 250.0 | None | True | False |
| Rate of CreateSession requests | 10.0 | None | True | False |
| Trust anchors | 50.0 | None | True | False |

## Route 53 Resolver (AWS Service: route53resolver)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Associations between resolver rules and VPCs per AWS Region | 2000.0 | None | True | False |
| DNS Firewall rule group associations per VPC | 5.0 | None | False | False |
| DNS Firewall rules groups per Region | 1000.0 | None | True | False |
| Domain lists per account | 1000.0 | None | True | False |
| Domains in a file imported from S3 | 250000.0 | None | True | False |
| Domains per account | 100000.0 | None | True | False |
| IP addresses per resolver endpoint | 6.0 | None | True | False |
| Maximum number of resolver endpoints per AWS Region | 4.0 | None | True | False |
| Resolver rules per AWS Region | 1000.0 | None | True | False |
| Rules in a DNS Firewall rule group | 100.0 | None | True | False |
| Target IP addresses per resolver rule | 6.0 | None | False | False |

## Amazon CloudWatch RUM (AWS Service: rum)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| RUM AppMonitors | 20.0 | None | True | False |
| RUM Events per second per AWS Account | 50.0 | None | True | False |

## Amazon Simple Storage Service (Amazon S3) (AWS Service: s3)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Access Points | 10000.0 | None | True | False |
| Bucket policy | 20.0 | Kilobytes | False | False |
| Bucket tags | 50.0 | None | False | False |
| Buckets | 100.0 | None | True | False |
| CRR rules | 1000.0 | None | False | False |
| Event notifications | 100.0 | None | False | False |
| Lifecycle rules | 1000.0 | None | False | False |
| Maximum part size | 5.0 | Gigabytes | False | False |
| Minimum part size | 5.0 | Megabytes | False | False |
| Multi-Region Access Point Regions | 20.0 | None | False | False |
| Multi-Region Access Points | 100.0 | None | False | False |
| Object size | 5.0 | Terabytes | False | False |
| Object size (Console upload) | 160.0 | Gigabytes | False | False |
| Object tags | 10.0 | None | False | False |
| Parts | 10000.0 | None | False | False |
| Replication transfer rate | 1.0 | Gigabits | True | False |
| S3 Glacier: Number of random restore requests. | 35.0 | None | False | False |
| S3 Glacier: Provisioned capacity units | 2.0 | None | False | False |

## AWS S3 Outposts (AWS Service: s3-outposts)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Access Points | 10.0 | None | False | False |
| Buckets | 100.0 | None | False | False |

## Amazon SageMaker (AWS Service: sagemaker)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Longest run time for a processing job | 432000.0 | Seconds | False | False |
| Longest run time for a training job | 432000.0 | Seconds | False | False |
| Longest run time for an AutoML job, from creation to termination | 2592000.0 | Seconds | False | False |
| Maximum dataset size AutoML job can be run on | 100.0 | None | False | False |
| Maximum number of A2I flow definitions | 100.0 | None | True | False |
| Maximum number of A2I human task UIs | 100.0 | None | True | False |
| Maximum number of Ground Truth Streaming labeling jobs | 0.0 | None | True | False |
| Maximum number of Ground Truth labeling jobs | 1.0 | None | True | False |
| Maximum number of SageMaker Model Package Groups allowed per account | 250.0 | None | True | False |
| Maximum number of SageMaker Projects allowed per account | 500.0 | None | False | False |
| Maximum number of SageMakerImage images allowed per account | 250.0 | None | True | False |
| Maximum number of Studio user profiles per domain | 2.0 | None | True | False |
| Maximum number of concurrent AutoML Jobs | 1.0 | None | True | False |
| Maximum number of concurrent pipeline executions allowed per account | 20.0 | None | True | False |
| Maximum number of dataset objects per labeling job | 10000.0 | None | False | False |
| Maximum number of deployment plans that can be simultaneously created | 2.0 | None | True | False |
| Maximum number of device-fleets | 2.0 | None | True | False |
| Maximum number of devices | 400.0 | None | True | False |
| Maximum number of hyper parameter tuning jobs that can run at once in parallel | 4.0 | None | False | False |
| Maximum number of instances per endpoint | 4.0 | None | True | False |
| Maximum number of instances per processing job | 20.0 | None | False | False |
| Maximum number of instances per spot training job | 20.0 | None | False | False |
| Maximum number of instances per training job | 20.0 | None | False | False |
| Maximum number of parallel compilation jobs | 2.0 | None | True | False |
| Maximum number of parallel edge-deployments | 2.0 | None | True | False |
| Maximum number of parallel edge-packaging jobs | 2.0 | None | True | False |
| Maximum number of parameters allowed per pipeline | 200.0 | None | False | False |
| Maximum number of pipelines allowed per account | 500.0 | None | False | False |
| Maximum number of running Studio apps per domain | 20.0 | None | True | False |
| Maximum number of serverless endpoints | 5.0 | None | True | False |
| Maximum number of steps allowed per pipeline | 50.0 | None | False | False |
| Maximum number of training jobs each hyper parameter tuning job can run in parallel at once | 10.0 | None | False | False |
| Maximum number of training jobs that each hyperparameter tuning job can create | 750.0 | None | False | False |
| Maximum number of training jobs that each hyperparameter tuning job with Random search strategy can create | 750.0 | None | False | False |
| Maximum subsampled dataset size AutoML job can be run on | 5.0 | None | False | False |
| Maximum total concurrency that can be allocated across all serverless endpoints | 10.0 | None | True | False |
| Number of elastic inference accelerators across active endpoints | 0.0 | None | True | False |
| Number of elastic inference accelerators across all notebook instances | 0.0 | None | True | False |
| Number of instances across active endpoints | 4.0 | None | True | False |
| Number of instances across all processing jobs | 4.0 | None | True | False |
| Number of instances across all spot training jobs | 4.0 | None | True | False |
| Number of instances across all training jobs | 4.0 | None | True | False |
| Number of instances across all transform jobs | 4.0 | None | True | False |
| Number of workteams | 25.0 | None | False | False |
| RSessionGateway Apps running on ml.c5.12xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.c5.18xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.c5.24xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.c5.2xlarge instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.c5.4xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.c5.9xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.c5.large instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.c5.xlarge instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.g4dn.12xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.g4dn.16xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.g4dn.2xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.g4dn.4xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.g4dn.8xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.g4dn.xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.m5.12xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.m5.16xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.m5.24xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.m5.2xlarge instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.m5.4xlarge instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.m5.8xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.m5.large instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.m5.xlarge instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.m5d.12xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.m5d.16xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.m5d.24xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.m5d.2xlarge instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.m5d.4xlarge instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.m5d.8xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.m5d.large instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.m5d.xlarge instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.p3.16xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.p3.2xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.p3.8xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.p3dn.24xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.p4d.24xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.r5.12xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.r5.16xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.r5.24xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.r5.2xlarge instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.r5.4xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.r5.8xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.r5.large instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.r5.xlarge instance | 1.0 | None | True | False |
| RSessionGateway Apps running on ml.t3.2xlarge instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.t3.large instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.t3.medium instance | 2.0 | None | True | False |
| RSessionGateway Apps running on ml.t3.micro instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.t3.small instance | 0.0 | None | True | False |
| RSessionGateway Apps running on ml.t3.xlarge instance | 0.0 | None | True | False |
| RStudioServerPro Apps running on ml.c5.4xlarge instances | 0.0 | None | True | False |
| RStudioServerPro Apps running on ml.c5.9xlarge instances | 0.0 | None | True | False |
| Rate of CreateEndpoint requests | 1.0 | None | False | False |
| Rate of CreateEndpointConfig requests | 1.0 | None | False | False |
| Rate of CreateModel requests | 1.0 | None | False | False |
| Rate of CreateNotebookInstance requests | 1.0 | None | False | False |
| Rate of CreateNotebookInstanceLifecycleConfig requests | 1.0 | None | False | False |
| Rate of CreatePresignedNotebookInstanceUrl requests | 1.0 | None | False | False |
| Rate of CreateStudioLifecycleConfig requests | 1.0 | None | False | False |
| Rate of CreateTrainingJob requests | 1.0 | None | False | False |
| Rate of CreateTransformJob requests | 1.0 | None | False | False |
| Rate of DeleteEndpoint requests | 1.0 | None | False | False |
| Rate of DeleteEndpointConfig requests | 1.0 | None | False | False |
| Rate of DeleteModel requests | 1.0 | None | False | False |
| Rate of DeleteNotebookInstance requests | 1.0 | None | False | False |
| Rate of DeleteNotebookInstanceLifecycleConfig requests | 1.0 | None | False | False |
| Rate of DeleteStudioLifecycleConfig requests | 1.0 | None | False | False |
| Rate of DescribeEndpoint requests | 5.0 | None | False | False |
| Rate of DescribeEndpointConfig requests | 5.0 | None | False | False |
| Rate of DescribeModel requests | 5.0 | None | False | False |
| Rate of DescribeNotebookInstanceLifecycleConfig requests | 5.0 | None | False | False |
| Rate of DescribeStudioLifecycleConfig requests | 5.0 | None | False | False |
| Rate of DescribeTrainingJob requests | 5.0 | None | False | False |
| Rate of DescribeTransformJob requests | 5.0 | None | False | False |
| Rate of InvokeEndpoint requests | 10000.0 | None | False | False |
| Rate of ListEndpointConfigs requests | 2.0 | None | False | False |
| Rate of ListEndpoints requests | 2.0 | None | False | False |
| Rate of ListModels requests | 2.0 | None | False | False |
| Rate of ListNotebookInstanceLifecycleConfigs requests | 2.0 | None | False | False |
| Rate of ListNotebookInstances requests | 2.0 | None | False | False |
| Rate of ListStudioLifecycleConfigs requests | 2.0 | None | False | False |
| Rate of ListTrainingJobs requests | 2.0 | None | False | False |
| Rate of ListTransformJobs requests | 2.0 | None | False | False |
| Rate of StartNotebookInstance requests | 1.0 | None | False | False |
| Rate of StopNotebookInstance requests | 1.0 | None | False | False |
| Rate of StopTrainingJob requests | 1.0 | None | False | False |
| Rate of StopTransformJob requests | 1.0 | None | False | False |
| Rate of UpdateEndpoint requests | 1.0 | None | False | False |
| Rate of UpdateEndpointWeightsAndCapacities requests | 1.0 | None | False | False |
| Rate of UpdateNotebookInstance requests | 1.0 | None | False | False |
| Rate of UpdateNotebookInstanceLifecycleConfig requests | 1.0 | None | False | False |
| Rate of UpdateTrainingJob requests | 1.0 | None | False | False |
| Size of EBS volume for a transform job instance | 1024.0 | None | False | False |
| Size of EBS volume for an instance | 1024.0 | None | False | False |
| Size of EBS volume for an instance | 1024.0 | None | False | False |
| Studio Jupyter Apps running on system instances | 10.0 | None | True | False |
| Studio KernelGateway Apps running on ml.c5.12xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.c5.18xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.c5.24xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.c5.2xlarge instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.c5.4xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.c5.9xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.c5.large instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.c5.xlarge instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.g4dn.12xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.g4dn.16xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.g4dn.2xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.g4dn.4xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.g4dn.8xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.g4dn.xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5.12xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5.16xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5.24xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5.2xlarge instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5.4xlarge instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5.8xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5.large instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5.xlarge instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5d.12xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5d.16xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5d.24xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5d.2xlarge instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5d.4xlarge instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5d.8xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5d.large instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.m5d.xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.p3.16xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.p3.2xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.p3.8xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.p3dn.24xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.r5.12xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.r5.16xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.r5.24xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.r5.2xlarge instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.r5.4xlarge instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.r5.8xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.r5.large instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.r5.xlarge instance | 1.0 | None | True | False |
| Studio KernelGateway Apps running on ml.t3.2xlarge instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.t3.large instance | 0.0 | None | True | False |
| Studio KernelGateway Apps running on ml.t3.medium instance | 2.0 | None | True | False |
| Studio KernelGateway Apps running on ml.t3.xlarge instance | 0.0 | None | True | False |
| Time at which pipeline executions time out | 672.0 | None | False | False |
| Total EBS volume size in GB across all notebook instances | 102400.0 | None | False | False |
| Total number of experiments allowed, excluding those automatically created by SageMaker | 5000.0 | None | False | False |
| Total number of notebook instances | 4.0 | None | True | False |
| Total number of trial components allowed from a SageMaker context, excluding those automatically created by SageMaker | 20000.0 | None | False | False |
| Total number of trial components allowed in a single trial, excluding those automatically created by SageMaker | 50.0 | None | False | False |
| Total number of trials a single trial component can be associated to | 500.0 | None | False | False |
| Total number of trials allowed in a single experiment, excluding those automatically created by SageMaker | 300.0 | None | False | False |
| ml.c4.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c4.2xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.c4.2xlarge for processing job usage | 4.0 | None | True | False |
| ml.c4.2xlarge for spot training job usage | 4.0 | None | True | False |
| ml.c4.2xlarge for training job usage | 4.0 | None | True | False |
| ml.c4.2xlarge for transform job usage | 4.0 | None | True | False |
| ml.c4.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c4.4xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.c4.4xlarge for processing job usage | 2.0 | None | True | False |
| ml.c4.4xlarge for spot training job usage | 0.0 | None | True | False |
| ml.c4.4xlarge for training job usage | 0.0 | None | True | False |
| ml.c4.4xlarge for transform job usage | 4.0 | None | True | False |
| ml.c4.8xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c4.8xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.c4.8xlarge for processing job usage | 0.0 | None | True | False |
| ml.c4.8xlarge for spot training job usage | 0.0 | None | True | False |
| ml.c4.8xlarge for training job usage | 0.0 | None | True | False |
| ml.c4.8xlarge for transform job usage | 4.0 | None | True | False |
| ml.c4.large for endpoint usage | 0.0 | None | True | False |
| ml.c4.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c4.xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.c4.xlarge for processing job usage | 4.0 | None | True | False |
| ml.c4.xlarge for spot training job usage | 4.0 | None | True | False |
| ml.c4.xlarge for training job usage | 4.0 | None | True | False |
| ml.c4.xlarge for transform job usage | 4.0 | None | True | False |
| ml.c5.12xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5.18xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5.18xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.c5.18xlarge for processing job usage | 0.0 | None | True | False |
| ml.c5.18xlarge for spot training job usage | 0.0 | None | True | False |
| ml.c5.18xlarge for training job usage | 0.0 | None | True | False |
| ml.c5.18xlarge for transform job usage | 1.0 | None | True | False |
| ml.c5.24xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5.2xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.c5.2xlarge for processing job usage | 4.0 | None | True | False |
| ml.c5.2xlarge for spot training job usage | 4.0 | None | True | False |
| ml.c5.2xlarge for training job usage | 4.0 | None | True | False |
| ml.c5.2xlarge for transform job usage | 4.0 | None | True | False |
| ml.c5.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5.4xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.c5.4xlarge for processing job usage | 1.0 | None | True | False |
| ml.c5.4xlarge for spot training job usage | 1.0 | None | True | False |
| ml.c5.4xlarge for training job usage | 1.0 | None | True | False |
| ml.c5.4xlarge for transform job usage | 1.0 | None | True | False |
| ml.c5.9xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5.9xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.c5.9xlarge for processing job usage | 0.0 | None | True | False |
| ml.c5.9xlarge for spot training job usage | 0.0 | None | True | False |
| ml.c5.9xlarge for training job usage | 0.0 | None | True | False |
| ml.c5.9xlarge for transform job usage | 1.0 | None | True | False |
| ml.c5.large for endpoint usage | 0.0 | None | True | False |
| ml.c5.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5.xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.c5.xlarge for processing job usage | 4.0 | None | True | False |
| ml.c5.xlarge for spot training job usage | 4.0 | None | True | False |
| ml.c5.xlarge for training job usage | 4.0 | None | True | False |
| ml.c5.xlarge for transform job usage | 4.0 | None | True | False |
| ml.c5d.18xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5d.18xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.c5d.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5d.2xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.c5d.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5d.4xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.c5d.9xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5d.9xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.c5d.large for endpoint usage | 0.0 | None | True | False |
| ml.c5d.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5d.xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.c5n.18xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5n.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5n.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5n.9xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c5n.large for endpoint usage | 0.0 | None | True | False |
| ml.c5n.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c6i.12xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c6i.16xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c6i.24xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c6i.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c6i.32xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c6i.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c6i.8xlarge for endpoint usage | 0.0 | None | True | False |
| ml.c6i.large for endpoint usage | 0.0 | None | True | False |
| ml.c6i.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.eia1.large for endpoint usage | 0.0 | None | True | False |
| ml.eia1.large for notebook instance accelerator type usage | 0.0 | None | True | False |
| ml.eia1.medium for endpoint usage | 0.0 | None | True | False |
| ml.eia1.medium for notebook instance accelerator type usage | 0.0 | None | True | False |
| ml.eia1.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.eia1.xlarge for notebook instance accelerator type usage | 0.0 | None | True | False |
| ml.eia2.large for endpoint usage | 0.0 | None | True | False |
| ml.eia2.large for notebook instance accelerator type usage | 0.0 | None | True | False |
| ml.eia2.medium for endpoint usage | 0.0 | None | True | False |
| ml.eia2.medium for notebook instance accelerator type usage | 0.0 | None | True | False |
| ml.eia2.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.eia2.xlarge for notebook instance accelerator type usage | 0.0 | None | True | False |
| ml.g4dn.12xlarge for endpoint usage | 0.0 | None | True | False |
| ml.g4dn.12xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.g4dn.12xlarge for processing job usage | 0.0 | None | True | False |
| ml.g4dn.12xlarge for spot training job usage | 0.0 | None | True | False |
| ml.g4dn.12xlarge for training job usage | 0.0 | None | True | False |
| ml.g4dn.12xlarge for transform job usage | 0.0 | None | True | False |
| ml.g4dn.16xlarge for endpoint usage | 0.0 | None | True | False |
| ml.g4dn.16xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.g4dn.16xlarge for processing job usage | 0.0 | None | True | False |
| ml.g4dn.16xlarge for spot training job usage | 0.0 | None | True | False |
| ml.g4dn.16xlarge for training job usage | 0.0 | None | True | False |
| ml.g4dn.16xlarge for transform job usage | 0.0 | None | True | False |
| ml.g4dn.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.g4dn.2xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.g4dn.2xlarge for processing job usage | 0.0 | None | True | False |
| ml.g4dn.2xlarge for spot training job usage | 0.0 | None | True | False |
| ml.g4dn.2xlarge for training job usage | 0.0 | None | True | False |
| ml.g4dn.2xlarge for transform job usage | 0.0 | None | True | False |
| ml.g4dn.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.g4dn.4xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.g4dn.4xlarge for processing job usage | 0.0 | None | True | False |
| ml.g4dn.4xlarge for spot training job usage | 0.0 | None | True | False |
| ml.g4dn.4xlarge for training job usage | 0.0 | None | True | False |
| ml.g4dn.4xlarge for transform job usage | 0.0 | None | True | False |
| ml.g4dn.8xlarge for endpoint usage | 0.0 | None | True | False |
| ml.g4dn.8xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.g4dn.8xlarge for processing job usage | 0.0 | None | True | False |
| ml.g4dn.8xlarge for spot training job usage | 0.0 | None | True | False |
| ml.g4dn.8xlarge for training job usage | 0.0 | None | True | False |
| ml.g4dn.8xlarge for transform job usage | 0.0 | None | True | False |
| ml.g4dn.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.g4dn.xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.g4dn.xlarge for processing job usage | 0.0 | None | True | False |
| ml.g4dn.xlarge for spot training job usage | 0.0 | None | True | False |
| ml.g4dn.xlarge for training job usage | 0.0 | None | True | False |
| ml.g4dn.xlarge for transform job usage | 0.0 | None | True | False |
| ml.g5.12xlarge for endpoint usage | 0.0 | None | True | False |
| ml.g5.16xlarge for endpoint usage | 0.0 | None | True | False |
| ml.g5.24xlarge for endpoint usage | 0.0 | None | True | False |
| ml.g5.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.g5.48xlarge for endpoint usage | 0.0 | None | True | False |
| ml.g5.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.g5.8xlarge for endpoint usage | 0.0 | None | True | False |
| ml.g5.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.inf1.24xlarge for endpoint usage | 0.0 | None | True | False |
| ml.inf1.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.inf1.6xlarge for endpoint usage | 0.0 | None | True | False |
| ml.inf1.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m4.10xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m4.10xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.m4.10xlarge for processing job usage | 0.0 | None | True | False |
| ml.m4.10xlarge for spot training job usage | 0.0 | None | True | False |
| ml.m4.10xlarge for training job usage | 0.0 | None | True | False |
| ml.m4.10xlarge for transform job usage | 1.0 | None | True | False |
| ml.m4.16xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m4.16xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.m4.16xlarge for processing job usage | 0.0 | None | True | False |
| ml.m4.16xlarge for spot training job usage | 0.0 | None | True | False |
| ml.m4.16xlarge for training job usage | 0.0 | None | True | False |
| ml.m4.16xlarge for transform job usage | 1.0 | None | True | False |
| ml.m4.2xlarge for endpoint usage | 1.0 | None | True | False |
| ml.m4.2xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.m4.2xlarge for processing job usage | 4.0 | None | True | False |
| ml.m4.2xlarge for spot training job usage | 4.0 | None | True | False |
| ml.m4.2xlarge for training job usage | 4.0 | None | True | False |
| ml.m4.2xlarge for transform job usage | 4.0 | None | True | False |
| ml.m4.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m4.4xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.m4.4xlarge for processing job usage | 2.0 | None | True | False |
| ml.m4.4xlarge for spot training job usage | 2.0 | None | True | False |
| ml.m4.4xlarge for training job usage | 2.0 | None | True | False |
| ml.m4.4xlarge for transform job usage | 2.0 | None | True | False |
| ml.m4.xlarge for endpoint usage | 2.0 | None | True | False |
| ml.m4.xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.m4.xlarge for processing job usage | 4.0 | None | True | False |
| ml.m4.xlarge for spot training job usage | 4.0 | None | True | False |
| ml.m4.xlarge for training job usage | 4.0 | None | True | False |
| ml.m4.xlarge for transform job usage | 4.0 | None | True | False |
| ml.m5.12xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5.12xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.m5.12xlarge for processing job usage | 0.0 | None | True | False |
| ml.m5.12xlarge for spot training job usage | 0.0 | None | True | False |
| ml.m5.12xlarge for training job usage | 0.0 | None | True | False |
| ml.m5.12xlarge for transform job usage | 0.0 | None | True | False |
| ml.m5.16xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5.24xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5.24xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.m5.24xlarge for processing job usage | 0.0 | None | True | False |
| ml.m5.24xlarge for spot training job usage | 0.0 | None | True | False |
| ml.m5.24xlarge for training job usage | 0.0 | None | True | False |
| ml.m5.24xlarge for transform job usage | 0.0 | None | True | False |
| ml.m5.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5.2xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.m5.2xlarge for processing job usage | 4.0 | None | True | False |
| ml.m5.2xlarge for spot training job usage | 4.0 | None | True | False |
| ml.m5.2xlarge for training job usage | 4.0 | None | True | False |
| ml.m5.2xlarge for transform job usage | 4.0 | None | True | False |
| ml.m5.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5.4xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.m5.4xlarge for processing job usage | 2.0 | None | True | False |
| ml.m5.4xlarge for spot training job usage | 2.0 | None | True | False |
| ml.m5.4xlarge for training job usage | 2.0 | None | True | False |
| ml.m5.4xlarge for transform job usage | 2.0 | None | True | False |
| ml.m5.8xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5.large for endpoint usage | 2.0 | None | True | False |
| ml.m5.large for processing job usage | 4.0 | None | True | False |
| ml.m5.large for spot training job usage | 4.0 | None | True | False |
| ml.m5.large for training job usage | 4.0 | None | True | False |
| ml.m5.large for transform job usage | 4.0 | None | True | False |
| ml.m5.xlarge for endpoint usage | 1.0 | None | True | False |
| ml.m5.xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.m5.xlarge for processing job usage | 4.0 | None | True | False |
| ml.m5.xlarge for spot training job usage | 4.0 | None | True | False |
| ml.m5.xlarge for training job usage | 4.0 | None | True | False |
| ml.m5.xlarge for transform job usage | 4.0 | None | True | False |
| ml.m5d.12xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5d.12xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.m5d.16xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5d.16xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.m5d.24xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5d.24xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.m5d.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5d.2xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.m5d.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5d.4xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.m5d.8xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5d.8xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.m5d.large for endpoint usage | 0.0 | None | True | False |
| ml.m5d.large for notebook instance usage | 1.0 | None | True | False |
| ml.m5d.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5d.xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.m5dn.12xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5dn.16xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5dn.24xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5dn.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5dn.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5dn.8xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5dn.large for endpoint usage | 0.0 | None | True | False |
| ml.m5dn.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5n.12xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5n.16xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5n.24xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5n.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5n.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5n.8xlarge for endpoint usage | 0.0 | None | True | False |
| ml.m5n.large for endpoint usage | 0.0 | None | True | False |
| ml.m5n.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.p3.16xlarge for endpoint usage | 0.0 | None | True | False |
| ml.p3.16xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.p3.16xlarge for processing job usage | 0.0 | None | True | False |
| ml.p3.16xlarge for spot training job usage | 0.0 | None | True | False |
| ml.p3.16xlarge for training job usage | 0.0 | None | True | False |
| ml.p3.16xlarge for transform job usage | 0.0 | None | True | False |
| ml.p3.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.p3.2xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.p3.2xlarge for processing job usage | 0.0 | None | True | False |
| ml.p3.2xlarge for spot training job usage | 0.0 | None | True | False |
| ml.p3.2xlarge for training job usage | 0.0 | None | True | False |
| ml.p3.2xlarge for transform job usage | 0.0 | None | True | False |
| ml.p3.8xlarge for endpoint usage | 0.0 | None | True | False |
| ml.p3.8xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.p3.8xlarge for processing job usage | 0.0 | None | True | False |
| ml.p3.8xlarge for spot training job usage | 0.0 | None | True | False |
| ml.p3.8xlarge for training job usage | 0.0 | None | True | False |
| ml.p3.8xlarge for transform job usage | 0.0 | None | True | False |
| ml.p3dn.24xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.p3dn.24xlarge for spot training job usage | 0.0 | None | True | False |
| ml.p3dn.24xlarge for training job usage | 0.0 | None | True | False |
| ml.p4d.24xlarge for endpoint usage | 0.0 | None | True | False |
| ml.p4d.24xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.r5.12xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5.12xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.r5.12xlarge for processing job usage | 0.0 | None | True | False |
| ml.r5.16xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5.16xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.r5.16xlarge for processing job usage | 0.0 | None | True | False |
| ml.r5.24xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5.24xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.r5.24xlarge for processing job usage | 0.0 | None | True | False |
| ml.r5.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5.2xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.r5.2xlarge for processing job usage | 0.0 | None | True | False |
| ml.r5.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5.4xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.r5.4xlarge for processing job usage | 0.0 | None | True | False |
| ml.r5.8xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5.8xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.r5.8xlarge for processing job usage | 0.0 | None | True | False |
| ml.r5.large for endpoint usage | 0.0 | None | True | False |
| ml.r5.large for notebook instance usage | 1.0 | None | True | False |
| ml.r5.large for processing job usage | 0.0 | None | True | False |
| ml.r5.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5.xlarge for notebook instance usage | 1.0 | None | True | False |
| ml.r5.xlarge for processing job usage | 0.0 | None | True | False |
| ml.r5d.12xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5d.16xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5d.24xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5d.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5d.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5d.8xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5d.large for endpoint usage | 0.0 | None | True | False |
| ml.r5d.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5dn.12xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5dn.16xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5dn.24xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5dn.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5dn.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5dn.8xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5dn.large for endpoint usage | 0.0 | None | True | False |
| ml.r5dn.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5n.12xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5n.16xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5n.24xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5n.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5n.4xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5n.8xlarge for endpoint usage | 0.0 | None | True | False |
| ml.r5n.large for endpoint usage | 0.0 | None | True | False |
| ml.r5n.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.t2.2xlarge for endpoint usage | 0.0 | None | True | False |
| ml.t2.2xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.t2.large for endpoint usage | 0.0 | None | True | False |
| ml.t2.large for notebook instance usage | 0.0 | None | True | False |
| ml.t2.medium for endpoint usage | 2.0 | None | True | False |
| ml.t2.medium for notebook instance usage | 2.0 | None | True | False |
| ml.t2.xlarge for endpoint usage | 0.0 | None | True | False |
| ml.t2.xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.t3.2xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.t3.2xlarge for processing job usage | 0.0 | None | True | False |
| ml.t3.large for notebook instance usage | 0.0 | None | True | False |
| ml.t3.large for processing job usage | 4.0 | None | True | False |
| ml.t3.medium for notebook instance usage | 2.0 | None | True | False |
| ml.t3.medium for processing job usage | 4.0 | None | True | False |
| ml.t3.xlarge for notebook instance usage | 0.0 | None | True | False |
| ml.t3.xlarge for processing job usage | 2.0 | None | True | False |

## Amazon EventBridge Schema Registry (AWS Service: schemas)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| DiscoveredSchemas | 200.0 | None | True | False |
| Discoverers | 10.0 | None | True | False |
| Registries | 10.0 | None | True | False |
| SchemaVersions | 100.0 | None | True | False |
| Schemas | 100.0 | None | True | False |

## AWS Secrets Manager (AWS Service: secretsmanager)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Combined rate of DeleteResourcePolicy, GetResourcePolicy, PutResourcePolicy, and ValidateResourcePolicy API requests | 50.0 | None | False | False |
| Combined rate of DescribeSecret and GetSecretValue API requests | 5000.0 | None | False | False |
| Combined rate of ListSecrets and ListSecretVersionIds API requests | 50.0 | None | False | False |
| Combined rate of PutSecretValue, RemoveRegionsFromReplication, ReplicateSecretToRegion, StopReplicationToReplica, UpdateSecret, and UpdateSecretVersionStage API requests | 50.0 | None | False | False |
| Combined rate of RestoreSecret API requests | 50.0 | None | False | False |
| Combined rate of RotateSecret and CancelRotateSecret API requests | 50.0 | None | False | False |
| Combined rate of TagResource and UntagResource API requests | 50.0 | None | False | False |
| Rate of CreateSecret API requests | 50.0 | None | False | False |
| Rate of DeleteSecret API requests | 50.0 | None | False | False |
| Rate of GetRandomPassword API requests | 50.0 | None | False | False |
| Resource-based policy length | 20480.0 | None | False | False |
| Secret value size | 65536.0 | Bytes | False | False |
| Secrets | 500000.0 | None | False | False |
| Staging labels attached across all versions of a secret | 20.0 | None | False | False |
| Versions per secret | 100.0 | None | False | False |

## AWS Security Hub (AWS Service: securityhub)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Number of Security Hub member accounts | 5000.0 | None | False | False |
| Number of Security Hub outstanding invitations | 1000.0 | None | False | False |
| Number of custom actions | 50.0 | None | False | False |
| Number of custom insights | 100.0 | None | False | False |
| Number of insight results | 100.0 | None | False | False |
| Security Hub finding retention time | 90.0 | None | False | False |

## AWS Serverless Application Repository (AWS Service: serverlessrepo)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Application policy length | 6144.0 | None | False | False |
| Free Amazon S3 storage for code packages | 5.0 | Gigabytes | False | False |
| Public applications | 100.0 | None | True | False |

## AWS Service Catalog (AWS Service: servicecatalog)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Applications per attribute group | 1000.0 | None | True | False |
| Applications per region | 2000.0 | None | True | False |
| Attribute groups per application | 1000.0 | None | True | False |
| Attribute groups per region | 2000.0 | None | True | False |
| Delegated administrators per organization | 50.0 | None | False | False |
| Portfolios per region | 100.0 | None | True | False |
| Product versions per product | 100.0 | None | True | False |
| Products per portfolio | 150.0 | None | True | False |
| Products per region | 350.0 | None | True | False |
| Resources per application | 1000.0 | None | True | False |
| Service action associations per provisioning artifact | 25.0 | None | False | False |
| Service actions per region | 200.0 | None | False | False |
| Shared accounts per portfolio | 5000.0 | None | False | False |
| TagOptions per resource | 25.0 | None | False | False |
| Tags per portfolio | 20.0 | None | False | False |
| Tags per product | 20.0 | None | False | False |
| Tags per provisioned product | 50.0 | None | False | False |
| Users, groups, and roles per portfolio | 100.0 | None | True | False |
| Users, groups, and roles per product | 200.0 | None | True | False |
| Values per TagOption | 25.0 | None | False | False |

## Service Quotas (AWS Service: servicequotas)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Active requests per quota | 1.0 | None | False | False |
| Throttle rate for GetAWSDefaultServiceQuota | 5.0 | None | False | False |
| Throttle rate for GetRequestedServiceQuotaChange | 5.0 | None | False | False |
| Throttle rate for GetServiceQuota | 5.0 | None | False | False |
| Throttle rate for ListAWSDefaultServiceQuotas | 10.0 | None | False | False |
| Throttle rate for ListRequestedServiceQuotaChangeHistory | 5.0 | None | False | False |
| Throttle rate for ListRequestedServiceQuotaChangeHistoryByQuota | 5.0 | None | False | False |
| Throttle rate for ListServiceQuotas | 10.0 | None | False | False |
| Throttle rate for ListServices | 10.0 | None | False | False |
| Throttle rate for ListTagsForResource | 10.0 | None | False | False |
| Throttle rate for RequestServiceQuotaIncrease | 3.0 | None | False | False |
| Throttle rate for TagResource | 10.0 | None | False | False |
| Throttle rate for UntagResource | 10.0 | None | False | False |

## Amazon Simple Email Service(Amazon SES) (AWS Service: ses)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Sending quota | 200.0 | None | True | False |
| Sending rate | 1.0 | None | True | False |

## AWS Signer (AWS Service: signer)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| API calls per second | 25.0 | None | False | False |
| Rate of AddProfilePermission requests | 3.0 | None | True | False |
| Rate of CancelSigningProfile requests | 3.0 | None | True | False |
| Rate of DescribeSigningJob requests | 6.0 | None | True | False |
| Rate of GetSigningPlatform requests | 3.0 | None | True | False |
| Rate of GetSigningProfile requests | 3.0 | None | True | False |
| Rate of ListProfilePermissions requests | 6.0 | None | True | False |
| Rate of ListSigningJobs requests | 6.0 | None | True | False |
| Rate of ListSigningPlatforms requests | 6.0 | None | True | False |
| Rate of ListSigningProfiles requests | 6.0 | None | True | False |
| Rate of ListTagsForResource requests | 6.0 | None | True | False |
| Rate of PutSigningProfile requests | 3.0 | None | True | False |
| Rate of RemoveProfilePermission requests | 3.0 | None | True | False |
| Rate of RevokeSignature requests | 3.0 | None | True | False |
| Rate of RevokeSigningProfile requests | 3.0 | None | True | False |
| Rate of StartSigningJob requests | 3.0 | None | True | False |
| Rate of TagResource requests | 3.0 | None | True | False |
| Rate of UntagResource requests | 3.0 | None | True | False |

## AWS Server Migration Service (AWS Service: sms)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Concurrent VM migrations | 50.0 | None | True | False |
| Duration of service usage per VM in days | 90.0 | None | True | False |

## AWS Snow Family (AWS Service: snowball)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Snowball Edge devices | 1.0 | None | True | False |

## Amazon Simple Notification Service (Amazon SNS) (AWS Service: sns)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| AddPermission Transactions per Second | 10.0 | None | False | False |
| CheckIfPhoneNumberIsOptedOut Transactions per Second | 50.0 | None | False | False |
| ConfirmSubscription Transactions per Second | 30.0 | None | True | False |
| CreatePlatformApplication Transactions per Second | 30.0 | None | True | False |
| CreatePlatformEndpoint Transactions per Second | 30.0 | None | True | False |
| CreateSMSSandboxPhoneNumber Transactions per Second | 1.0 | None | False | False |
| CreateTopic Transactions per Second | 30.0 | None | True | False |
| DeleteEndpoint Transactions per Second | 30.0 | None | True | False |
| DeletePlatformApplication Transactions per Second | 30.0 | None | True | False |
| DeleteSMSSandboxPhoneNumber Transactions per Second | 1.0 | None | False | False |
| DeleteTopic Transactions per Second | 30.0 | None | True | False |
| Email Delivery Rate per Second | 10.0 | None | False | False |
| Filter Policies per Account | 200.0 | None | True | False |
| GetEndpointAttributes Transactions per Second | 30.0 | None | True | False |
| GetPlatformApplicationAttributes Transactions per Second | 30.0 | None | True | False |
| GetSMSAttributes Transactions per Second | 20.0 | None | False | False |
| GetSMSSandboxAccountStatus Transactions per Second | 10.0 | None | False | False |
| GetSubscriptionAttributes Transactions per Second | 30.0 | None | True | False |
| GetTopicAttributes Transactions per Second | 30.0 | None | True | False |
| ListEndpointsByPlatformApplication Transactions per Second | 30.0 | None | False | False |
| ListOriginationNumbers Transactions per Second | 1.0 | None | False | False |
| ListPhoneNumbersOptedOut Transactions per Second | 10.0 | None | False | False |
| ListPlatformApplications Transactions per Second | 15.0 | None | False | False |
| ListSMSSandboxPhoneNumbers Transactions per Second | 1.0 | None | False | False |
| ListSubscriptions Transactions per Second | 30.0 | None | False | False |
| ListSubscriptionsByTopic Transactions per Second | 30.0 | None | False | False |
| ListTagsForResource Transactions per Second | 10.0 | None | False | False |
| ListTopics Transactions per Second | 30.0 | None | False | False |
| Messages Published per Second | 300.0 | None | True | False |
| OptInPhoneNumber Transactions per Second | 20.0 | None | False | False |
| Pending Subscriptions per Account | 5000.0 | None | False | False |
| Promotional SMS Message Delivery Rate per Second | 20.0 | None | False | False |
| RemovePermission Transactions per Second | 10.0 | None | False | False |
| SMS Message Spending in USD | 1.0 | None | True | False |
| SetEndpointAttributes Transactions per Second | 30.0 | None | True | False |
| SetPlatformApplicationAttributes Transactions per Second | 30.0 | None | True | False |
| SetSMSAttributes Transactions per Second | 1.0 | None | False | False |
| SetSubscriptionAttributes Transactions per Second | 30.0 | None | True | False |
| SetTopicAttributes Transactions per Second | 30.0 | None | True | False |
| Subscribe Transactions per Second | 100.0 | None | False | False |
| Subscriptions per Topic | 12500000.0 | None | False | False |
| TagResource Transactions per Second | 10.0 | None | False | False |
| Topics per Account | 100000.0 | None | True | False |
| Transactional SMS Message Delivery Rate per Second | 20.0 | None | False | False |
| Unsubscribe Transactions per Second | 100.0 | None | False | False |
| UntagResource Transactions per Second | 10.0 | None | False | False |
| VerifySMSSandboxPhoneNumber Transactions per Second | 1.0 | None | False | False |

## Amazon Simple Queue Service (Amazon SQS) (AWS Service: sqs)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Actions per Queue Policy | 7.0 | None | False | False |
| Attributes per Message | 10.0 | None | False | False |
| Batched Message ID Length | 80.0 | None | False | False |
| Conditions per Queue Policy | 10.0 | None | False | False |
| In-Flight Messages per Standard Queue | 120000.0 | None | False | False |
| Message Invisibility Period | 0.0 | Seconds | False | False |
| Message Retention Time | 345600.0 | Seconds | False | False |
| Message Size | 256.0 | Kilobytes | False | False |
| Message Size in S3 Bucket | 2.0 | Gigabytes | False | False |
| Messages per Batch | 10.0 | None | False | False |
| Principals per Queue Policy | 50.0 | None | False | False |
| Queue Delivery Delay | 15.0 | None | False | False |
| Queue Name Length | 80.0 | None | False | False |
| Queue Policy Size | 8192.0 | Bytes | False | False |
| Statements per Queue Policy | 20.0 | None | False | False |
| Tags per Queue | 50.0 | None | False | False |
| UTF-8 Queue Tag Key Length | 128.0 | None | False | False |
| UTF-8 Queue Tag Value Length | 256.0 | None | False | False |

## AWS Systems Manager (AWS Service: ssm)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Additional Automation executions that can be queued | 5000.0 | None | True | False |
| Additional rate control automation executions that can be queued | 1000.0 | None | True | False |
| Concurrent State Manager associations per region | 2000.0 | None | True | False |
| Concurrently executing Automations | 100.0 | None | True | False |
| Concurrently executing rate control automation | 25.0 | None | True | False |
| Custom inventory type attributes | 50.0 | None | False | False |
| Custom inventory types | 20.0 | None | True | False |
| Instances per target | 50.0 | None | False | False |
| Inventory data retention period | 30.0 | None | False | False |
| Inventory data size per request | 1024.0 | Kilobytes | True | False |
| Inventory item data size per day | 5000.0 | Kilobytes | True | False |
| Maintenance Window concurrent executions | 5.0 | None | True | False |
| Maintenance Window execution history retention | 30.0 | None | False | False |
| Maintenance Windows | 50.0 | None | True | False |
| Number of levels of nested automation | 5.0 | None | False | False |
| OpsItems per month | 10000.0 | None | True | False |
| Patch baselines | 50.0 | None | True | False |
| Patch groups per patch baseline | 25.0 | None | True | False |
| Run Command execution history retention in seconds | 2592000.0 | Seconds | False | False |
| Single Maintenance Window concurrent executions | 1.0 | None | False | False |
| Target groups per Maintenance Window target or task | 5.0 | None | False | False |
| Targets per Maintenance Window | 100.0 | None | True | False |
| Tasks per Maintenance Window | 20.0 | None | True | False |
| Total OpsItems | 500000.0 | None | True | False |

## AWS Systems Manager Incident Manager Contacts (AWS Service: ssm-contacts)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| AcceptPage API throttle quota | 20.0 | None | True | False |
| All other operations API throttle quota | 1.0 | None | True | False |
| Contact channels per stage | 10.0 | None | True | False |
| Contacts per account | 1000.0 | None | True | False |
| DescribeEngagement API throttle quota | 5.0 | None | True | False |
| DescribePage API throttle quota | 5.0 | None | True | False |
| Email engagement throttle quota | 0.05 | None | False | False |
| ListEngagements API throttle quota | 2.0 | None | True | False |
| ListPageReceipts API throttle quota | 1.0 | None | True | False |
| ListPagesByContact API throttle quota | 1.0 | None | True | False |
| ListPagesByEngagement API throttle quota | 2.0 | None | True | False |
| SMS engagement throttle quota | 0.05 | None | False | False |
| Stages per plan | 5.0 | None | False | False |
| StartEngagement API throttle quota | 20.0 | None | True | False |
| StopEngagement API throttle quota | 10.0 | None | True | False |
| Voice engagement throttle quota | 0.01 | None | False | False |

## AWS Systems Manager GUI Connect (AWS Service: ssm-guiconnect)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Concurrent Remote Desktop connections | 5.0 | None | True | False |

## AWS Systems Manager Incident Manager (AWS Service: ssm-incidents)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| All other operations requests per second | 10.0 | None | True | False |
| CreateReplicationSet requests per second | 1.0 | None | True | False |
| CreateResponsePlan requests per second | 5.0 | None | True | False |
| CreateTimelineEvent requests per second | 5.0 | None | True | False |
| DeleteIncidentRecord requests per second | 5.0 | None | True | False |
| DeleteReplicationSet requests per second | 1.0 | None | True | False |
| DeleteResourcePolicy requests per second | 5.0 | None | True | False |
| DeleteResponsePlan requests per second | 5.0 | None | True | False |
| DeleteTimelineEvent requests per second | 5.0 | None | True | False |
| Incidents per response plan per month | 200.0 | None | True | False |
| PutResourcePolicy requests per second | 5.0 | None | True | False |
| Regions per replication set | 3.0 | None | False | False |
| Related items per incident | 50.0 | None | True | False |
| Replication sets per account | 1.0 | None | False | False |
| StartIncident requests per second | 5.0 | None | True | False |
| TagResource requests per second | 5.0 | None | True | False |
| Timeline events per incident | 1000.0 | None | True | False |
| UntagResource requests per second | 5.0 | None | True | False |
| UpdateDeleteProtection requests per second | 1.0 | None | True | False |
| UpdateIncidentRecord requests per second | 5.0 | None | True | False |
| UpdateRelatedItems requests per second | 5.0 | None | True | False |
| UpdateReplicationSet requests per second | 1.0 | None | True | False |
| UpdateResponsePlan requests per second | 5.0 | None | True | False |
| UpdateTimelineEvent requests per second | 5.0 | None | True | False |

## AWS IAM Identity Center (successor to AWS Single Sign-On) (AWS Service: sso)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| File size of service provider SAML certificates (in PEM format) | 2.0 | Kilobytes | False | False |
| Number of groups supported in IAM Identity Center | 10000.0 | None | False | False |
| Number of permission sets allowed in IAM Identity Center | 500.0 | None | True | False |
| Number of permission sets allowed per AWS account | 50.0 | None | True | False |
| Number of unique directory groups that can be assigned | 2500.0 | None | True | False |
| Number of unique groups that can be used to evaluate the permissions for a user | 500.0 | None | False | False |
| Number of users supported in IAM Identity Center | 50000.0 | None | False | False |
| Total number of AWS accounts or applications that can be configured | 500.0 | None | True | False |

## AWS Step Functions (AWS Service: states)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Activity pollers per ARN | 1000.0 | None | False | False |
| CreateActivity throttle token bucket size | 100.0 | None | True | False |
| CreateActivity throttle token refill rate per second | 1.0 | None | True | False |
| CreateStateMachine throttle token bucket size | 100.0 | None | True | False |
| CreateStateMachine throttle token refill rate per second | 1.0 | None | True | False |
| DeleteActivity throttle token bucket size | 100.0 | None | True | False |
| DeleteActivity throttle token refill rate per second | 1.0 | None | True | False |
| DeleteStateMachine throttle token bucket size | 100.0 | None | True | False |
| DeleteStateMachine throttle token refill rate per second | 1.0 | None | True | False |
| DescribeActivity throttle token bucket size | 200.0 | None | True | False |
| DescribeActivity throttle token refill rate per second | 1.0 | None | True | False |
| DescribeExecution throttle token bucket size | 250.0 | None | True | False |
| DescribeExecution throttle token refill rate per second | 10.0 | None | True | False |
| DescribeStateMachine throttle token bucket size | 200.0 | None | True | False |
| DescribeStateMachine throttle token refill rate per second | 20.0 | None | True | False |
| DescribeStateMachineForExecution throttle token bucket size | 200.0 | None | True | False |
| DescribeStateMachineForExecution throttle token refill rate per second | 1.0 | None | True | False |
| Events in execution history size | 25000.0 | None | False | False |
| Execution history retention time in days | 90.0 | None | False | False |
| Execution idle time in years | 1.0 | None | False | False |
| Execution time in years | 1.0 | None | False | False |
| Executions displayed in Step Functions console | 1000.0 | None | False | False |
| GetActivityTask throttle token bucket size | 1500.0 | None | True | False |
| GetActivityTask throttle token refill rate per second | 300.0 | None | True | False |
| GetExecutionHistory throttle token bucket size | 400.0 | None | True | False |
| GetExecutionHistory throttle token refill rate per second | 20.0 | None | True | False |
| Input or result data size in task state or execution | 262144.0 | Bytes | False | False |
| ListActivities throttle token bucket size | 100.0 | None | True | False |
| ListActivities throttle token refill rate per second | 5.0 | None | True | False |
| ListExecutions throttle token bucket size | 100.0 | None | True | False |
| ListExecutions throttle token refill rate per second | 2.0 | None | True | False |
| ListStateMachines throttle token bucket size | 100.0 | None | True | False |
| ListStateMachines throttle token refill rate per second | 5.0 | None | True | False |
| ListTagsForResource throttle token bucket size | 100.0 | None | True | False |
| ListTagsForResource throttle token refill rate per second | 1.0 | None | True | False |
| Open executions | 1000000.0 | None | True | False |
| Registered activities | 10000.0 | None | True | False |
| Registered state machines | 10000.0 | None | True | False |
| Resource name length | 80.0 | None | False | False |
| SendTaskFailure throttle token bucket size | 1500.0 | None | True | False |
| SendTaskFailure throttle token refill rate per second | 300.0 | None | True | False |
| SendTaskHeartbeat throttle token bucket size | 1500.0 | None | True | False |
| SendTaskHeartbeat throttle token refill rate per second | 300.0 | None | True | False |
| SendTaskSuccess throttle token bucket size | 1500.0 | None | True | False |
| SendTaskSuccess throttle token refill rate per second | 300.0 | None | True | False |
| Size per API request | 1.0 | Megabytes | False | False |
| StartExecution throttle token bucket size | 800.0 | None | True | False |
| StartExecution throttle token refill rate per second | 150.0 | None | True | False |
| StateTransition throttle token bucket size | 800.0 | None | True | False |
| StateTransition throttle token refill rate per second | 500.0 | None | True | False |
| Step Functions task in queue in year | 1.0 | None | False | False |
| StopExecution throttle token bucket size | 500.0 | None | True | False |
| StopExecution throttle token refill rate per second | 25.0 | None | True | False |
| TagResource throttle token bucket size | 200.0 | None | True | False |
| TagResource throttle token refill rate per second | 1.0 | None | True | False |
| Task execution time in year | 1.0 | None | False | False |
| UntagResource throttle token bucket size | 200.0 | None | True | False |
| UntagResource throttle token refill rate per second | 1.0 | None | True | False |
| UpdateStateMachine throttle token bucket size | 100.0 | None | True | False |
| UpdateStateMachine throttle token refill rate per second | 1.0 | None | False | False |

## AWS Storage Gateway (AWS Service: storagegateway)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Cached volume gateway Cache Maximum in TiB | 16.0 | None | False | False |
| Cached volume gateway Cache Minimum in GiB | 150.0 | None | False | False |
| Cached volume gateway Upload Buffer Maximum in TiB | 2.0 | None | False | False |
| Cached volume gateway Upload Buffer Minimum in GiB | 150.0 | None | False | False |
| Cached volume size in TiB | 32.0 | None | False | False |
| Cached volumes per gateway | 32.0 | None | False | False |
| File gateway Cache Maximum in TiB | 16.0 | None | False | False |
| File gateway Cache Minimum in GiB | 150.0 | None | False | False |
| File shares per S3 bucket | 1.0 | None | False | False |
| File shares per gateway | 10.0 | None | False | False |
| File size | 5.0 | Terabytes | False | False |
| Max size of a virtual tape in TiB | 5.0 | None | False | False |
| Max virtual tapes in a VTL | 1500.0 | None | False | False |
| Minimum size of a virtual tape in GiB | 100.0 | None | False | False |
| Path length | 1024.0 | Bytes | False | False |
| Size of all cached volumes per gateway in TiB | 1024.0 | None | False | False |
| Size of all stored volumes per gateway in TiB | 512.0 | None | False | False |
| Stored volume gateway Upload Buffer Maximum in TiB | 2.0 | None | False | False |
| Stored volume gateway Upload Buffer Minimum in GiB | 150.0 | None | False | False |
| Stored volume size in TiB | 16.0 | None | False | False |
| Stored volumes per gateway | 32.0 | None | False | False |
| Tape gateway Cache Maximum in TiB | 16.0 | None | False | False |
| Tape gateway Cache Minimum in GiB | 150.0 | None | False | False |
| Tape gateway Upload Buffer Maximum in TiB | 2.0 | None | False | False |
| Tape gateway Upload Buffer Minimum in GiB | 150.0 | None | False | False |
| Total size of tapes in a virtual tape library in PiB | 1.0 | None | False | False |

## Amazon Sumerian (AWS Service: sumerian)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Model file size | 50.0 | Megabytes | False | False |
| Projects | 1000.0 | None | False | False |
| Scenes | 10000.0 | None | False | False |
| Script file size | 1.0 | Megabytes | False | False |
| Sound file size | 10.0 | Megabytes | False | False |
| Texture file size | 20.0 | Megabytes | False | False |
| ZIP file size | 200.0 | Megabytes | False | False |

## Amazon Simple Workflow Service (AWS Service: swf)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| CountClosedWorkflowExecutions throttle burst limit in transactions per second | 2000.0 | None | True | False |
| CountClosedWorkflowExecutions throttle refill limit in transactions per second | 6.0 | None | True | False |
| CountOpenWorkflowExecutions throttle burst limit in transactions per second | 2000.0 | None | True | False |
| CountOpenWorkflowExecutions throttle refill limit in transactions per second | 6.0 | None | True | False |
| CountPendingActivityTasks throttle burst limit in transactions per second | 200.0 | None | True | False |
| CountPendingActivityTasks throttle refill limit in transactions per second | 6.0 | None | True | False |
| CountPendingDecisionTasks throttle burst limit in transactions per second | 200.0 | None | True | False |
| CountPendingDecisionTasks throttle refill limit in transactions per second | 6.0 | None | True | False |
| DeprecateActivityType throttle burst limit in transactions per second | 200.0 | None | True | False |
| DeprecateActivityType throttle refill limit in transactions per second | 6.0 | None | True | False |
| DeprecateDomain throttle burst limit in transactions per second | 200.0 | None | True | False |
| DeprecateDomain throttle refill limit in transactions per second | 6.0 | None | True | False |
| DeprecateWorkflowType throttle burst limit in transactions per second | 200.0 | None | True | False |
| DeprecateWorkflowType throttle refill limit in transactions per second | 6.0 | None | True | False |
| DescribeActivityType throttle burst limit in transactions per second | 2000.0 | None | True | False |
| DescribeActivityType throttle refill limit in transactions per second | 6.0 | None | True | False |
| DescribeDomain throttle burst limit in transactions per second | 200.0 | None | True | False |
| DescribeDomain throttle refill limit in transactions per second | 6.0 | None | True | False |
| DescribeWorkflowExecution throttle burst limit in transactions per second | 2000.0 | None | True | False |
| DescribeWorkflowExecution throttle refill limit in transactions per second | 6.0 | None | True | False |
| DescribeWorkflowType throttle burst limit in transactions per second | 2000.0 | None | True | False |
| DescribeWorkflowType throttle refill limit in transactions per second | 6.0 | None | True | False |
| Events in Workflow execution history | 25000.0 | None | False | False |
| GetWorkflowExecutionHistory throttle burst limit in transactions per second | 2000.0 | None | True | False |
| GetWorkflowExecutionHistory throttle refill limit in transactions per second | 60.0 | None | True | False |
| Input / result data size | 32768.0 | None | False | False |
| ListActivityTypes throttle burst limit in transactions per second | 200.0 | None | True | False |
| ListActivityTypes throttle refill limit in transactions per second | 6.0 | None | True | False |
| ListClosedWorkflowExecutions throttle burst limit in transactions per second | 200.0 | None | True | False |
| ListClosedWorkflowExecutions throttle refill limit in transactions per second | 6.0 | None | True | False |
| ListDomains throttle burst limit in transactions per second | 100.0 | None | True | False |
| ListDomains throttle refill limit in transactions per second | 6.0 | None | True | False |
| ListOpenWorkflowExecutions throttle burst limit in transactions per second | 200.0 | None | True | False |
| ListOpenWorkflowExecutions throttle refill limit in transactions per second | 48.0 | None | True | False |
| ListWorkflowTypes throttle burst limit in transactions per second | 200.0 | None | True | False |
| ListWorkflowTypes throttle refill limit in transactions per second | 6.0 | None | True | False |
| Maximum workflow and activity types per domain | 10000.0 | None | True | False |
| Open activity tasks per workflow execution | 1000.0 | None | False | False |
| Open child workflow executions | 1000.0 | None | False | False |
| Open timers per workflow execution | 1000.0 | None | False | False |
| Open workflow executions per domain | 100000.0 | None | True | False |
| PollForActivityTask throttle burst limit in transactions per second | 2000.0 | None | True | False |
| PollForActivityTask throttle refill limit in transactions per second | 200.0 | None | True | False |
| PollForDecisionTask throttle burst limit in transactions per second | 2000.0 | None | True | False |
| PollForDecisionTask throttle refill limit in transactions per second | 200.0 | None | True | False |
| Pollers per task list | 1000.0 | None | False | False |
| RecordActivityTaskHeartbeat throttle burst limit in transactions per second | 2000.0 | None | True | False |
| RecordActivityTaskHeartbeat throttle refill limit in transactions per second | 160.0 | None | True | False |
| RegisterActivityType throttle burst limit in transactions per second | 200.0 | None | True | False |
| RegisterActivityType throttle refill limit in transactions per second | 60.0 | None | True | False |
| RegisterDomain throttle burst limit in transactions per second | 100.0 | None | True | False |
| RegisterDomain throttle refill limit in transactions per second | 6.0 | None | True | False |
| RegisterWorkflowType throttle burst limit in transactions per second | 200.0 | None | True | False |
| RegisterWorkflowType throttle refill limit in transactions per second | 60.0 | None | True | False |
| Registered domains | 100.0 | None | True | False |
| Request size | 1.0 | Megabytes | False | False |
| RequestCancelExternalWorkflowExecution throttle burst limit in transactions per second | 1200.0 | None | True | False |
| RequestCancelExternalWorkflowExecution throttle refill limit in transactions per second | 120.0 | None | True | False |
| RequestCancelWorkflowExecution throttle burst limit in transactions per second | 2000.0 | None | True | False |
| RequestCancelWorkflowExecution throttle refill limit in transactions per second | 30.0 | None | True | False |
| RespondActivityTaskCanceled throttle burst limit in transactions per second | 2000.0 | None | True | False |
| RespondActivityTaskCanceled throttle refill limit in transactions per second | 200.0 | None | True | False |
| RespondActivityTaskCompleted throttle burst limit in transactions per second | 2000.0 | None | True | False |
| RespondActivityTaskCompleted throttle refill limit in transactions per second | 200.0 | None | True | False |
| RespondActivityTaskFailed throttle burst limit in transactions per second | 2000.0 | None | True | False |
| RespondActivityTaskFailed throttle refill limit in transactions per second | 200.0 | None | True | False |
| RespondDecisionTaskCompleted throttle burst limit in transactions per second | 2000.0 | None | True | False |
| RespondDecisionTaskCompleted throttle refill limit in transactions per second | 200.0 | None | True | False |
| SWF task in queue in year | 1.0 | None | False | False |
| ScheduleActivityTask throttle burst limit in transactions per second | 1000.0 | None | True | False |
| ScheduleActivityTask throttle refill limit in transactions per second | 200.0 | None | True | False |
| SignalExternalWorkflowExecution throttle burst limit in transactions per second | 1200.0 | None | True | False |
| SignalExternalWorkflowExecution throttle refill limit in transactions per second | 120.0 | None | True | False |
| SignalWorkflowExecution throttle burst limit in transactions per second | 2000.0 | None | True | False |
| SignalWorkflowExecution throttle refill limit in transactions per second | 30.0 | None | True | False |
| StartChildWorkflowExecution throttle burst limit in transactions per second | 500.0 | None | True | False |
| StartChildWorkflowExecution throttle refill limit in transactions per second | 12.0 | None | True | False |
| StartTimer throttle burst limit in transactions per second | 2000.0 | None | True | False |
| StartTimer throttle refill limit in transactions per second | 200.0 | None | True | False |
| StartWorkflowExecution throttle burst limit in transactions per second | 2000.0 | None | True | False |
| StartWorkflowExecution throttle refill limit in transactions per second | 200.0 | None | True | False |
| Task execution time in year | 1.0 | None | False | False |
| TerminateWorkflowExecution throttle burst limit in transactions per second | 2000.0 | None | True | False |
| TerminateWorkflowExecution throttle refill limit in transactions per second | 60.0 | None | True | False |
| Workflow execution idle time limit in years | 1.0 | None | True | False |
| Workflow execution time in years | 1.0 | None | False | False |
| Workflow retention time in days | 90.0 | None | True | False |

## Amazon Textract (AWS Service: textract)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| AnalyzeDocument throttle limit in transactions per second | 1.0 | None | True | False |
| AnalyzeExpense throttle limit in transactions per second | 1.0 | None | True | False |
| AnalyzeID throttle limit in transactions per second | 1.0 | None | True | False |
| Async AnalyzeExpense throttle limit for max number of concurrent jobs | 100.0 | None | True | False |
| Async DocumentAnalysis throttle limit for max number of concurrent jobs | 100.0 | None | True | False |
| Async DocumentTextDetection throttle limit for max number of concurrent jobs | 100.0 | None | True | False |
| DetectDocumentText throttle limit in transactions per second | 1.0 | None | True | False |
| GetDocumentAnalysis throttle limit in transactions per second | 1.0 | None | True | False |
| GetDocumentTextDetection throttle limit in transactions per second | 1.0 | None | True | False |
| GetExpenseAnalysis throttle limit in transactions per second | 1.0 | None | True | False |
| StartDocumentAnalysis throttle limit in transactions per second | 2.0 | None | True | False |
| StartDocumentTextDetection throttle limit in transactions per second | 1.0 | None | True | False |
| StartExpenseAnalysis throttle limit in transactions per second | 1.0 | None | True | False |

## Amazon Transcribe (AWS Service: transcribe)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Job queue bandwidth ratio | 0.9 | None | True | False |
| Maximum audio file length | 14400.0 | Seconds | False | False |
| Maximum audio file length (Medical) | 14400.0 | Seconds | False | False |
| Maximum audio file length for Call Analytics batch jobs | 14400.0 | Seconds | False | False |
| Maximum audio file size | 2.0 | Gigabytes | False | False |
| Maximum audio file size (Medical) | 2.0 | Gigabytes | False | False |
| Maximum audio file size for Call Analytics batch jobs | 500.0 | Megabytes | False | False |
| Maximum length of a custom vocabulary phrase | 256.0 | None | False | False |
| Maximum number of categories for Call Analytics batch jobs | 200.0 | None | True | False |
| Maximum number of rules per category for Call Analytics batch jobs | 20.0 | None | True | False |
| Maximum number of targets allowed per category for Call Analytics batch jobs | 100.0 | None | True | False |
| Maximum number of vocabulary filters | 100.0 | None | False | False |
| Maximum size of a custom vocabulary | 50.0 | Kilobytes | False | False |
| Maximum size of a vocabulary filter | 50.0 | Kilobytes | False | False |
| Minimum audio file duration | 500.0 | Milliseconds | False | False |
| Minimum audio file duration (Medical) | 500.0 | Milliseconds | False | False |
| Minimum audio file duration for Call Analytics batch jobs | 500.0 | Milliseconds | False | False |
| Number of StartMedicalStreamTranscription Websocket requests | 25.0 | None | True | False |
| Number of channels for channel identification | 2.0 | None | True | False |
| Number of channels for channel identification (Medical) | 2.0 | None | False | False |
| Number of channels for channel identification for Call Analytics batch jobs | 2.0 | None | False | False |
| Number of concurrent Call Analytics batch jobs | 100.0 | None | True | False |
| Number of concurrent batch transcription jobs | 250.0 | None | True | False |
| Number of concurrent medical batch transcription jobs | 250.0 | None | True | False |
| Number of concurrently training custom language models | 3.0 | None | True | False |
| Number of days that job records are retained | 90.0 | None | False | False |
| Number of days that job records are retained (Medical) | 90.0 | None | False | False |
| Number of days that job records are retained for Call Analytics batch jobs | 90.0 | None | False | False |
| Number of pending medical vocabularies | 10.0 | None | True | False |
| Number of pending vocabularies | 10.0 | None | True | False |
| Total number of custom language models per account | 10.0 | None | True | False |
| Total number of medical vocabularies per account | 100.0 | None | True | False |
| Total number of vocabularies per account | 100.0 | None | True | False |
| Transactions per second, CreateCallAnalyticsCategory operation | 10.0 | None | True | False |
| Transactions per second, CreateVocabulary operation | 10.0 | None | True | False |
| Transactions per second, DeleteCallAnalyticsCategory operation | 5.0 | None | True | False |
| Transactions per second, DeleteCallAnalyticsJob operation | 5.0 | None | True | False |
| Transactions per second, DeleteMedicalTranscriptionJob operation | 5.0 | None | True | False |
| Transactions per second, DeleteMedicalVocabulary operation | 5.0 | None | True | False |
| Transactions per second, DeleteTranscriptionJob operation | 5.0 | None | True | False |
| Transactions per second, DeleteVocabulary operation | 5.0 | None | True | False |
| Transactions per second, GetCallAnalyticsCategory operation | 20.0 | None | True | False |
| Transactions per second, GetCallAnalyticsJob operation | 20.0 | None | True | False |
| Transactions per second, GetMedicalTranscriptionJob operation | 30.0 | None | True | False |
| Transactions per second, GetMedicalVocabulary operation | 20.0 | None | True | False |
| Transactions per second, GetTranscriptionJob operation | 30.0 | None | True | False |
| Transactions per second, GetVocabulary operation | 20.0 | None | True | False |
| Transactions per second, ListCallAnalyticsCategories operation | 5.0 | None | True | False |
| Transactions per second, ListCallAnalyticsJobs operation | 5.0 | None | True | False |
| Transactions per second, ListMedicalTranscriptionJobs operation | 5.0 | None | True | False |
| Transactions per second, ListMedicalVocabularies operation | 5.0 | None | True | False |
| Transactions per second, ListTranscriptionJobs operation | 5.0 | None | True | False |
| Transactions per second, ListVocabularies operation | 5.0 | None | True | False |
| Transactions per second, StartCallAnalyticsJob operation | 10.0 | None | True | False |
| Transactions per second, StartMedicalStreamTranscription operation | 25.0 | None | True | False |
| Transactions per second, StartMedicalTranscriptionJob operation | 25.0 | None | True | False |
| Transactions per second, StartTranscriptionJob operation | 25.0 | None | True | False |
| Transactions per second, UpdateCallAnalyticsCategory operation | 10.0 | None | True | False |
| Transactions per second, UpdateMedicalVocabulary operation | 10.0 | None | True | False |
| Transactions per second, UpdateVocabulary operation | 10.0 | None | True | False |

## AWS Transfer Family (AWS Service: transfer)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Concurrent sessions per server | 10000.0 | None | False | False |
| File size | 5.0 | Terabytes | False | False |
| Idle connection timeout | 1800.0 | Seconds | False | False |
| Maximum number of AD Groups for access | 20.0 | None | True | False |
| Maximum number of new executions per workflow | 100.0 | None | False | False |
| New executions refill rate per workflow per second | 1.0 | None | False | False |
| Number of Service Managed users per server | 10000.0 | None | True | False |
| Number of authentication requests per user per second | 2.0 | None | False | False |
| SSH keys per Service Managed user | 50.0 | None | True | False |
| Servers per account | 50.0 | None | True | False |
| VPC_ENDPOINT servers per account | 10.0 | None | False | False |
| Workflows per account | 10.0 | None | True | False |

## Amazon Translate (AWS Service: translate)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Concurrent batch translation jobs | 10.0 | None | True | False |
| Custom terminology files | 100.0 | None | True | False |

## EC2 VM Import/Export (AWS Service: vmimportexport)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Concurrent task limit for ImportImage, ImportSnapshot, and ExportImage | 20.0 | None | True | False |
| Concurrent task limit for ImportInstance, ImportVolume, and CreateInstanceExportTask | 5.0 | None | True | False |

## Amazon Virtual Private Cloud (Amazon VPC) (AWS Service: vpc)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Active VPC peering connections per VPC | 50.0 | None | True | False |
| Characters per VPC endpoint policy | 20480.0 | None | False | False |
| Egress-only internet gateways per Region | 5.0 | None | True | False |
| Gateway VPC endpoints per Region | 20.0 | None | True | False |
| IPv4 CIDR blocks per VPC | 5.0 | None | True | False |
| IPv6 CIDR blocks per VPC | 5.0 | None | False | False |
| Inbound or outbound rules per security group | 60.0 | None | True | False |
| Interface VPC endpoints per VPC | 50.0 | None | True | False |
| Internet gateways per Region | 5.0 | None | True | False |
| NAT gateways per Availability Zone | 5.0 | None | True | False |
| Network ACLs per VPC | 200.0 | None | True | False |
| Network interfaces per Region | 5000.0 | None | True | False |
| Outstanding VPC peering connection requests | 25.0 | None | True | False |
| Participant accounts per VPC | 100.0 | None | True | False |
| Route tables per VPC | 200.0 | None | True | False |
| Routes per route table | 50.0 | None | True | False |
| Rules per network ACL | 20.0 | None | True | False |
| Security groups per network interface | 5.0 | None | True | False |
| Subnets per VPC | 200.0 | None | True | False |
| Subnets that can be shared with an account | 100.0 | None | True | False |
| VPC peering connection request expiry hours | 168.0 | None | False | False |
| VPC security groups per Region | 2500.0 | None | True | False |
| VPCs per Region | 5.0 | None | True | False |

## AWS WAF Classic (Regional) (AWS Service: waf-regional)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Conditions per rule | 10.0 | None | False | False |
| Filters per SQL injection match condition | 10.0 | None | False | False |
| Filters per cross-site scripting match condition | 10.0 | None | False | False |
| Filters per size constraint condition | 10.0 | None | False | False |
| Filters per string match condition | 10.0 | None | False | False |
| GeoMatchSets | 50.0 | None | False | False |
| HTTP header name length | 40.0 | None | False | False |
| IP address ranges per IP set match condition | 10000.0 | None | False | False |
| IP addresses blocked per rate-based rule | 10000.0 | None | False | False |
| Locations per GeoMatchSet | 50.0 | None | False | False |
| Logging destination configurations per web ACL | 1.0 | None | False | False |
| Pattern sets per regex match condition | 1.0 | None | False | False |
| Patterns per pattern set | 10.0 | None | False | False |
| Rate of requests | 10000.0 | None | True | False |
| Rate-based rule rate | 2000.0 | None | False | False |
| Rate-based rules | 5.0 | None | True | False |
| Regex pattern length | 70.0 | None | False | False |
| Regex pattern sets | 5.0 | None | False | False |
| Rules | 100.0 | None | True | False |
| Rules per web ACL | 10.0 | None | False | False |
| Search length | 50.0 | None | False | False |
| Web ACLs | 50.0 | None | True | False |

## AWS WAF (AWS Service: wafv2)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Maximum IP sets per account in WAF for regional | 100.0 | None | False | False |
| Maximum number of IP addresses in an IP set in WAF for regional | 10000.0 | None | False | False |
| Maximum number of bytes in a string match (byte match) string in WAF for regional | 200.0 | None | False | False |
| Maximum number of characters allowed in a regex pattern per account in WAF for regional | 200.0 | None | False | False |
| Maximum number of log destination configs per web ACL in WAF for regional | 1.0 | None | False | False |
| Maximum number of patterns in a regex pattern set per account in WAF for regional | 10.0 | None | False | False |
| Maximum number of rate-based statements per web ACL in WAF for Cloudfront | 10.0 | None | True | False |
| Maximum number of referenced statements per rule group or web ACL in WAF for regional | 50.0 | None | False | False |
| Maximum number of web ACL capacity units in a rule group in WAF for regional | 1500.0 | None | True | False |
| Maximum number of web ACL capacity units in a web ACL in WAF for regional | 1500.0 | None | True | False |
| Maximum regex pattern sets per account in WAF for regional | 10.0 | None | False | False |
| Maximum rule groups per account in WAF for regional | 100.0 | None | True | False |
| Maximum web ACLs per account in WAF for regional | 100.0 | None | True | False |
| Number of CloudWatch Logs log streams per web ACL for regional | 35.0 | None | True | False |

## AWS Well-Architected Tool (AWS Service: wellarchitected)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Choices per question | 15.0 | None | False | False |
| Lens size | 500.0 | Kilobytes | False | False |
| Lenses per account per Region | 15.0 | None | False | False |
| Lenses per workload | 20.0 | None | False | False |
| Milestones per workload | 100.0 | None | False | False |
| Pillars per lens | 10.0 | None | False | False |
| Questions per pillar | 20.0 | None | False | False |
| Shares per lens | 300.0 | None | False | False |
| Shares per workload | 20.0 | None | False | False |
| Versions per lens | 100.0 | None | False | False |
| Workloads per account per Region | 1000.0 | None | False | False |

## Amazon Connect Wisdom (AWS Service: wisdom)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Amazon Wisdom assistant count | 5.0 | None | False | False |
| Amazon Wisdom knowledge base count | 10.0 | None | False | False |
| Assistant association | 1.0 | None | False | False |
| Content per knowledge base | 5000.0 | None | False | False |
| Content size | 1.0 | Megabytes | False | False |
| Rate of API requests | 10.0 | None | False | False |

## Amazon WorkSpaces (AWS Service: workspaces)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Bundles | 50.0 | None | False | False |
| Connection aliases | 20.0 | None | False | False |
| Directories | 50.0 | None | False | False |
| Graphics.g4dn WorkSpaces | 0.0 | None | True | False |
| GraphicsPro.g4dn WorkSpaces | 0.0 | None | True | False |
| IP access control groups | 100.0 | None | False | False |
| IP access control groups per directory | 25.0 | None | False | False |
| Images | 40.0 | None | True | False |
| Rules per IP access control group | 10.0 | None | False | False |
| WorkSpaces | 1.0 | None | True | False |

## Amazon WorkSpaces Web (AWS Service: workspaces-web)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Number of BrowserSettings | 3.0 | None | True | False |
| Number of Certificates per TrustStore | 100.0 | None | True | False |
| Number of IdentityProviders per Portal | 1.0 | None | True | False |
| Number of Maximum Concurrent Sessions per Portal | 25.0 | None | True | False |
| Number of NetworkSettings | 3.0 | None | True | False |
| Number of TrustStores | 3.0 | None | True | False |
| Number of UserSettings | 3.0 | None | True | False |
| Number of Web Portals | 1.0 | None | True | False |
| Rate of AssociateBrowserSettings requests | 1.0 | None | True | False |
| Rate of AssociateNetworkSettings requests | 1.0 | None | True | False |
| Rate of AssociateTrustStore requests | 1.0 | None | True | False |
| Rate of AssociateUserSettings requests | 1.0 | None | True | False |
| Rate of CreateBrowserSettings requests | 1.0 | None | True | False |
| Rate of CreateIdentityProvider requests | 1.0 | None | True | False |
| Rate of CreateNetworkSettings requests | 1.0 | None | True | False |
| Rate of CreatePortal requests | 1.0 | None | True | False |
| Rate of CreateTrustStore requests | 1.0 | None | True | False |
| Rate of CreateUserSettings requests | 1.0 | None | True | False |
| Rate of DeleteBrowserSettings requests | 1.0 | None | True | False |
| Rate of DeleteIdentityProvider requests | 1.0 | None | True | False |
| Rate of DeleteNetworkSettings requests | 1.0 | None | True | False |
| Rate of DeletePortal requests | 1.0 | None | True | False |
| Rate of DeleteTrustStore requests | 1.0 | None | True | False |
| Rate of DeleteUserSettings requests | 1.0 | None | True | False |
| Rate of DisassociateBrowserSettings requests | 1.0 | None | True | False |
| Rate of DisassociateNetworkSettings requests | 1.0 | None | True | False |
| Rate of DisassociateTrustStore requests | 1.0 | None | True | False |
| Rate of DisassociateUserSettings requests | 1.0 | None | True | False |
| Rate of GetBrowserSettings requests | 4.0 | None | True | False |
| Rate of GetIdentityProvider requests | 4.0 | None | True | False |
| Rate of GetNetworkSettings requests | 4.0 | None | True | False |
| Rate of GetPortal requests | 1.0 | None | True | False |
| Rate of GetUserSettings requests | 4.0 | None | True | False |
| Rate of ListBrowserSettings requests | 4.0 | None | True | False |
| Rate of ListIdentityProviders requests | 4.0 | None | True | False |
| Rate of ListNetworkSettings requests | 4.0 | None | True | False |
| Rate of ListPortals requests | 1.0 | None | True | False |
| Rate of ListTagsForResource requests | 4.0 | None | True | False |
| Rate of ListTrustStoreCertificates requests | 4.0 | None | True | False |
| Rate of ListTrustStores requests | 4.0 | None | True | False |
| Rate of ListUserSettings requests | 4.0 | None | True | False |
| Rate of TagResource requests | 1.0 | None | True | False |
| Rate of UntagResource requests | 1.0 | None | True | False |
| Rate of UpdateBrowserSettings requests | 1.0 | None | True | False |
| Rate of UpdateIdentityProvider requests | 1.0 | None | True | False |
| Rate of UpdateNetworkSettings requests | 1.0 | None | True | False |
| Rate of UpdatePortal requests | 1.0 | None | True | False |
| Rate of UpdateTrustStore requests | 1.0 | None | True | False |
| Rate of UpdateUserSettings requests | 1.0 | None | True | False |

## AWS X-Ray (AWS Service: xray)

| Property | Limit | Unit | Adjustable | Global |
|---|---|---|---|---|
| Custom sampling rules per region | 25.0 | None | True | False |
| Groups in an account | 25.0 | None | False | False |
| Indexed annotations per trace | 50.0 | None | False | False |
| Segment document size | 64.0 | Kilobytes | False | False |
| Tags per custom sampling rule | 50.0 | None | False | False |
| Tags per group | 50.0 | None | False | False |
| Trace and service graph retention in days | 30.0 | None | False | False |
| Trace data modification period in days | 7.0 | None | False | False |
| Trace document size (dynamic upper limit) | 500.0 | Kilobytes | False | False |
| Trace document size (lower limit) | 100.0 | Kilobytes | False | False |

