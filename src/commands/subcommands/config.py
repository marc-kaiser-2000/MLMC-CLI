import click


@click.group(name="config")
def config():
    """Config commands"""


@config.command()
def show():
    """Show the current "config.yaml" configuration."""
    click.echo("Showing configuration...")


@config.command()
@click.option(
    "--path", required=False, help="Absolute or relative path to load 'config.yaml'"
)
def load(path):
    """Load a configuration file, apply and serialize it."""
    click.echo("Loading configuration")

if __name__ == "__main__":
    load(".")
    show()