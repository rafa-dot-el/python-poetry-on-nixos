#!/usr/bin/env python3
import click
from loguru import logger as log


@click.command()
@click.option("--name", prompt="Your name", help="Your name")
def hello(name):
    log.info("Hello {name}", name=name)


if __name__ == "__main__":
    hello()
