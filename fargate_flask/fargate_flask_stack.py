from aws_cdk import core as cdk
from aws_cdk import aws_ec2
from aws_cdk import aws_ecs
from aws_cdk import aws_ecs_patterns

from fargate_flask.config import config


class FargateFlaskStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.vpc = aws_ec2.Vpc(
            self,
            'FargateVPC',
            cidr='172.31.0.0/16',
        )
        self.cluster = aws_ecs.Cluster(
            self,
            'FlaskCluster',
            vpc=self.vpc
        )
        self.application_image = aws_ecs.ContainerImage.from_asset(
            'fargate_flask/flask/'
        )
        self.fargate_service = aws_ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            'FargateFlaskApp',
            cluster=self.cluster,
            cpu=1024,
            desired_count=1,
            task_image_options=aws_ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=self.application_image,
            ),
            memory_limit_mib=1024,
            public_load_balancer=True,
        )
