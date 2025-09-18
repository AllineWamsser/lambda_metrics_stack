#!/usr/bin/env python3
import aws_cdk as cdk
from lambda_k8s_stack import LambdaKubernetesStack

#Entry point or the CDK application
app = cdk.App()
LambdaKubernetesStack(app, "LambdaKubernetesStack")
app.synth()