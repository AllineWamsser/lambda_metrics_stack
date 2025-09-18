import aws_cdk as cdk
from aws_cdk import (
    aws_lambda as lambda_,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam
)
from constructs import Construct

class LambdaKubernetesStack(cdk.Stack):
    """
    A simple example stack that deploys a Lambda function
    which simulates Kubernetes metrics collection.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function
        lambda_function = lambda_.Function(
            self, "KubernetesMetricsLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="handler.main",  # points to lambda/handler.py -> main()
            code=lambda_.Code.from_asset("lambda"),
            timeout=cdk.Duration.seconds(30),
            environment={
                "CLUSTER_NAME": "demo-cluster"
            }
        )

        # Add a simple IAM permission (symbolic, for demo purposes)
        lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["ec2:DescribeInstances"],
                resources=["*"]
            )
        )

        # Schedule the Lambda to run every day at 12:00 UTC
        schedule_rule = events.Rule(
            self, "MetricsScheduleRule",
            schedule=events.Schedule.cron(minute="0", hour="12"),
            targets=[targets.LambdaFunction(lambda_function)]
        )