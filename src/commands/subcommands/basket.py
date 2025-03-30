import click


@click.group(name="basket")
def basket():
    """Basket commands"""


@basket.command()
def show():
    """Show the current "config.yaml" file."""
    click.echo("Showing configuration...")


@basket.command()
@click.option(
    "--path", required=False, help="Absolute or relative path to load 'basket.yaml'"
)
def load(path):
    """Load a 'config.yaml' file, apply and serialize it."""
    click.echo("Loading basket...")


if __name__ == "__main__":
    load(".")
    show()