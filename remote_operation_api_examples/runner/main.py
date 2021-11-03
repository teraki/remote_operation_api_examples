import pkgutil

import click
from remote_operation_api_examples import examples


@click.group()
def cli():
    pass

@cli.command()
def all():
    click.echo("Executing all examples\n"+"*"*80)
    prefix = examples.__name__ + "."
    for importer, modname, ispkg in pkgutil.iter_modules(examples.__path__, prefix):
        module = __import__(modname, fromlist="dummy")
        for func_name, func in module.__dict__.items():
            if callable(func):
                click.echo(f"Executing {func_name} in module {modname}\n"+"."*80)
                func()
                click.echo("-"*80)

if __name__ == '__main__':
    cli()

