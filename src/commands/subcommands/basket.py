import logging
import click
from typing import Optional

logger = logging.getLogger(__name__)

@click.group(name="basket")
def basket():
    """Basket commands"""


@basket.command()
def show():
    """Show the current "config.yaml" file."""
    logger.info()
    click.echo("Showing configuration...")


@basket.command()
@click.option(
    "--path", required=False, help="Absolute or relative path to load 'basket.yaml'"
)
def load(path:Optional[str]):
    """Load a 'config.yaml' file, apply and serialize it."""
    if path is None:
        path = "."

    click.echo(f'Loading basket from {path}')


if __name__ == "__main__":
    load(".")
    show()