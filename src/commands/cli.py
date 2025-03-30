import click

from commands.subcommands.basket import basket
from commands.subcommands.config import config
from commands.subcommands.model import model

@click.group()
@click.version_option(version="1.0.0")
def cli():
    """My CLI application with commands in multiple files."""
    pass

# Register commands
cli.add_command(basket)
cli.add_command(config)
cli.add_command(model)

if __name__ == "__main__":
    cli()