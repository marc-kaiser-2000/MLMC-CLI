import click

from commands.subcommands.basket import basket
from commands.subcommands.config import config
from commands.subcommands.model import model


@click.group()
def cli():
    """Monte Carlo Learning CLI."""


# Register commands
cli.add_command(basket)
cli.add_command(config)
cli.add_command(model)

if __name__ == "__main__":
    cli()
