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
@click.option("-f", "--filter", type=str, default=None)
@cli.command()
def all(username, password, platform_url, filter):
    click.echo("Executing all examples\n" + "*" * 80)
    prefix = examples.__name__ + "."
    config = Config(username, password, platform_url)
    for importer, mod_name, ispkg in pkgutil.iter_modules(examples.__path__, prefix):
        module = __import__(mod_name, fromlist="dummy")
        for func_name, func in getmembers(module, isfunction):
            if (
                callable(func)
                and func.__module__ == mod_name
                and (not filter or (filter in func_name or filter in mod_name))
            ):
                click.echo(f"Executing {func_name} in module {mod_name}\n" + "." * 80)
                click.echo(func.__doc__)
                click.echo("." * 80)
                func(config)
                click.echo("/\\" * 40)


if __name__ == "__main__":
    cli()
