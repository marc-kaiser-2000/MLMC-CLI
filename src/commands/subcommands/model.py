import click


@click.group(name="model")
def model():
    """Model commands"""


@model.command()
def train():
    """Training the model"""
    click.echo("Showing configuration...")


@model.command()
def test():
    """Testing the model"""
    click.echo("Loading configuration")


@model.command()
@click.option(
    "--path", required=False, help="Absolute or relative path to load samples."
)
def predict(path):
    """Predict samples using the model"""
    click.echo("Predicting samples")

if __name__ == "__main__":
    train()
    test()
