#!/usr/bin/env python3
import os

from aws_cdk import core as cdk


from fargate_flask.config import config
from fargate_flask.resources.existing import ExistingResources
from fargate_flask.fargate_flask_stack import FargateFlaskStack


ENVIRONMENT = cdk.Environment(
    account=config['account'],
    region=config['region'],
)

app = cdk.App()

existing_resources = ExistingResources(
    app,
    'ExistingResources',
    env=ENVIRONMENT,
)

fargate_service = FargateFlaskStack(
    app,
    'FargateFlaskStack',
    existing_resources=existing_resources,
    env=ENVIRONMENT,
)

app.synth()
