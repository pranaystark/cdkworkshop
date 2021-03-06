#!/usr/bin/env python3

from aws_cdk import core

from cdkworkshop.cdkworkshop_stack import CdkworkshopStack


app = core.App()
CdkworkshopStack(app, "cdkworkshop", env={'region':'us-east-1'})

app.synth()
