import aws_cdk as cdk
from aws_cdk import (
    aws_lambda as lambda_,
    aws_events as events,
    aws_events_targets as targets
)
from constructs import Construct

class LambdaKubernetesStack(cdk.Stack):
    """
    A simple example stack that deploys a Lambda function
    which simulates Kubernetes metrics collection.
    """

    def _init_(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super()._init_(scope, construct_id, **kwargs)

        # Define the Lambda function
        lambda_function = lambda_.Function(
            self, "KubernetesMetricsLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="handler.main",  # points to handler.py -> main()
            code=lambda_.Code.from_asset("lambda"),
            timeout=cdk.Duration.seconds(30),
            environment={
                "CLUSTER_NAME": "demo-cluster"
            }
        )

        # Schedule the Lambda to run every day at 12:00 UTC
        schedule_rule = events.Rule(
            self, "MetricsScheduleRule",
            schedule=events.Schedule.cron(minute="0", hour="12"),
            targets=[targets.LambdaFunction(lambda_function)]
        )