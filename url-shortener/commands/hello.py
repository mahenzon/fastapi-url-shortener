__all__ = ("app",)

from typing import Annotated

import typer
from rich import print

app = typer.Typer(
    no_args_is_help=True,
    rich_markup_mode="rich",
)


@app.command(help="Greet user by [bold]name[/bold].")
def hello(
    name: Annotated[
        str,
        typer.Argument(help="Name to greet"),
    ],
) -> None:
    print(f"[bold]Hello, [green]{name}[/green]![/bold]")
