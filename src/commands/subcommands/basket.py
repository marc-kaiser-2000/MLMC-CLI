import click

@click.group(name="basket")
@click.option("--name", default="World", help="Name to greet")
def basket(name):
    """Basket commands"""
    pass