#!/usr/bin/env python3
import aws_cdk as cdk
from lambda_k8s_stack import LambdaKubernetesStack

# Entry point of the CDK application
app = cdk.App()

LambdaKubernetesStack(
    app, "LambdaKubernetesStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region=os.getenv("CDK_DEFAULT_REGION", "us-east-1")
    )
)

app.synth()