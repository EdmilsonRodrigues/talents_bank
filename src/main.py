import typer

from helpers import blue, clear_screen


app = typer.Typer()


def main_menu():
    typer.echo(blue("[1] [A]") + "dd a new person to the talent bank")
    typer.echo(blue("[2] [S]") + "earch for talents in the talent bank")
    typer.echo(blue("[2] [G]") + "et a specific person in the talent bank")
    typer.echo(blue("[3] [E]") + "dit a person from the talent bank")
    typer.echo(blue("[4] [D]") + "elete a person from the talent bank")


@app.callback(invoke_without_command=True)
def start(ctx: typer.Context):
    clear_screen()
    main_menu()
    option = typer.prompt("Select an option")
    typer.echo(option)


@app.command()
def add_talent(ctx: typer.Context):
    


if __name__ == "__main__":
    app()
