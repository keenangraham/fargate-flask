from aws_cdk import core as cdk
from aws_cdk import aws_ec2
from aws_cdk import aws_ecs
from aws_cdk import aws_ecs_patterns

from fargate_flask.config import config


class FargateFlaskStack(cdk.Stack):

    def __init__(self, scope, construct_id, existing_resources, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        self.existing_resources = existing_resources
        self.application_image = aws_ecs.ContainerImage.from_asset(
            'fargate_flask/flask/'
        )
        self.fargate_service = aws_ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            'FargateFlaskApp',
            vpc=self.existing_resources.internal_network.vpc,
            cpu=1024,
            desired_count=1,
            task_image_options=aws_ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=self.application_image,
            ),
            memory_limit_mib=2048,
            public_load_balancer=True,
            certificate=self.existing_resources.encode_api_domain.domain_certificate,
            domain_name=f'rnaget.{self.existing_resources.encode_api_domain.domain_name}',
            domain_zone=self.existing_resources.encode_api_domain.hosted_zone,
            security_groups=[self.existing_resources.internal_network.security_group],
            assign_public_ip=True,
        )
        self.fargate_service.target_group.configure_health_check(
            interval=cdk.Duration.seconds(60),
        )
        self.scalable_task = self.fargate_service.service(
            max_capacity=4,
        )
        self.scalable_task.scale_on_request_count(
            'RequestCountScaling',
            requests_per_target=4,
            target_group=self.fargate_service.target_group,
            scale_in_cooldown=cdk.Duration.seconds(60),
            scale_out_cooldown=cdk.Duration.seconds(60),
        )
