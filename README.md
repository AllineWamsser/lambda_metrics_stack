## AWS Lambda Metrics Collector (CDK Project)

This project demonstrates a *basic AWS Lambda integration with Kubernetes (simulated)* using the *AWS Cloud Development Kit (CDK)*.
It is designed as a *Junior-level portfolio project* to showcase basic understanding of *AWS CDK, Lambda, IAM, and CloudWatch*.

---

## Features

* *AWS Lambda* function (Python 3.9)  
* IAM Role* with minimal permissions  
* CloudWatch Event Rule* to trigger Lambda every 5 minutes  
* Inline Lambda code* (no external dependencies)  

---

## Requirements

* Python 3.9+  
* AWS CLI configured (⁠ aws configure ⁠ or ⁠ aws sso login ⁠
* AWS CDK v2 installed  
---
## Architecture Diagram
,,,
mermaid

flowchart TD
    CW[CloudWatch Event Rule<br>(rate: 5 min)] -->|Trigger| L[KubernetesMetricsFunction<br>(Lambda)]
    L -->|HTTP Request| E[External Metrics Endpoint]
    L -->|Logs| CWL[CloudWatch Logs]
,,,
---
## Features

* AWS Lambda (Python 3.9 runtime)
* Cloudwatch Event Rule (daily trigger at 12:00 UTC)
* Simulated Kubernetes metrics collection
* Infrastructure as Code with AWS CDK (Python)
---
## Features

1. Install CDK and dependences
 ```bash 
npm install -g aws-cdk
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt`
```
2. Bootstrap CDK (first time only)
```bash 
cdk bootstrap
```
3. Synthesize the CloudFormation template
````bash
cdk synth
````
4. Deploy the stack
````bash
cdk deploy
````
---
## Example lambda Output

When triggered (via CloudWatch Event or manual test), the lambda logs somethin like:

````bash
{
  "status": "success",
  "cluster": "demo-cluster",
  "metrics": {
    "cpu_usage": "25%",
    "memory_usage": "1.2Gi"
  }
}
````
## Notes

* This project simulates Kubernetes metrics.
* In a production scenario, you would: 
* * Use the AWS SDK (boto3) or the official Kubernetes Python cliente
* * Configure IAM roles and EKS cluster access IRSA.
* Here, we keep it simple and educational, suitable for a GitHub portfolio.