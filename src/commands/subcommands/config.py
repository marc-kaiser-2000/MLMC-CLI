import click

@click.group(name="config")
def config():
    """Config commands"""
    pass

@config.command()
def show():
    """Show the current configuration."""
    click.echo("Showing configuration...")

@config.command()
@click.option("--key", required=True, help="Configuration key")
@click.option("--value", required=True, help="Configuration value")
def set(key, value):
    """Set a configuration value."""
    click.echo(f"Setting {key}={value}")