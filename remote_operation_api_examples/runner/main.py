import pkgutil
from inspect import getmembers, isfunction

import click

from remote_operation_api_examples import examples
from remote_operation_api_examples.config import Config

TERAKI_URL = "https://api-remote-operations.test.teraki.com/"


@click.group()
def cli():
    pass


@click.option(
    "--password",
    prompt="Your password",
)
@click.option("-u", "--username", type=str, prompt="Your username")
@click.option("-p", "--platform_url", type=str, default=TERAKI_URL)
@cli.command()
def all(username, password, platform_url):
    click.echo("Executing all examples\n" + "*" * 80)
    prefix = examples.__name__ + "."
    config = Config(username, password, platform_url)
    for importer, modname, ispkg in pkgutil.iter_modules(examples.__path__, prefix):
        module = __import__(modname, fromlist="dummy")
        for func_name, func in getmembers(module, isfunction):
            if callable(func) and func.__module__ == modname:
                click.echo(f"Executing {func_name} in module {modname}\n" + "." * 80)
                func(config)
                click.echo("-" * 80)


if __name__ == "__main__":
    cli()
