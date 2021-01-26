from pathlib import Path

import click

from ccmlutils import version


class CLIError(BaseException):
    pass


@click.group()
@click.version_option(version, "--version", "-V", help="Show version and exit")
def cli():
    pass


@click.command(name="init")
@click.option(
    "--config",
    "-c",
    type=click.Path(exists=True),
    help="Non-interactive mode, using a configuration yaml file.",
)
@click.option(
    "--directory",
    "-dir",
    "directory",
    help="Project directory",
    default=Path.cwd()
)
def init(config, directory):
    click.echo(f'INIT: {config} {directory}')
    _init_poetry()
    _init_kedro(config)


@click.command(name="info")
def info():
    click.echo('INFO')


def _init_poetry():
    """

    Returns:

    """
    print(f"init poetry")
    pass


def _init_kedro(config_file: str = None):
    """

    Returns:

    """
    import subprocess
    print(f"init kedro")
    if config_file is None:
        subprocess.run(["kedro", "new"])
    else:
        subprocess.run(["kedro", "new", "--config", config_file])
    pass


cli.add_command(init)
cli.add_command(info)

if __name__ == '__main__':
    cli()
