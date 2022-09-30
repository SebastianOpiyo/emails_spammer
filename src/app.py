import click

from flask import Flask, render_template, request
from gophish import Gophish, models, api
from gophish.models import *


@click.group()
def main():
    """Running the Email Spammer Application"""


@click.command()
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=5000, type=int)
def web(host: str, port: int):
    from web import app
    app.run(host=host, port=port)


@click.command()
def testapi():
    from api_points import test_api
    test_api()


if __name__ == "__main__":
    main()
