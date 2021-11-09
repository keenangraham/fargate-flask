#!/usr/bin/env python3
import os

from aws_cdk import core as cdk


from fargate_flask.config import config
from fargate_flask.fargate_flask_stack import FargateFlaskStack


ENVIRONMENT = cdk.Environment(
    account=config['account'],
    region=config['region'],
)


app = cdk.App()


FargateFlaskStack(
    app,
    'FargateFlaskStack',
    env=ENVIRONMENT,
)


app.synth()
