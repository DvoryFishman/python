# -*- coding: utf-8 -*-
import click
from unicodedata import name

from FolderAndFile import first_word, second_word, third_word
from add_step import add_func
from checkout_step import checkout_func
from commit_step import commit_func
from init_step import init_func
from status_step import status_func


# @click.command("hello")
# @click.version_option("0.1.0", prog_name="hello")
# def hello():
#     click.echo("Hello, World!")
#
#
# if __name__ == "__init__":
#     hello()
@click.command()
@click.option('--name', prompt='Enter your name', help='The name of the user.')


def click_main(name):
    path = "C:\דבורי\שנה ב\פייתון\בדיקה של הפריקט"
    # user_input = input("enter string: ")
    full_string = name
    user_input = second_word(full_string)
    if user_input is not None:
        if user_input == "init":
            error_message = init_func(path)
            if error_message:
                click.secho(error_message, fg='red', bold=True)
            else:
                click.secho("Initialization completed successfully.", fg='green')
        else:
            if user_input == "add":
                name = third_word(full_string)
                if name is not None:
                    error_message2 = add_func(path, name)
                    if error_message2:
                        click.secho(error_message2, fg='red', bold=True)
                    else:
                        click.secho("add file successfully", fg='green')
                else:
                    click.secho("There is no name for the add", fg='red', bold=True)
            else:
                if user_input == "commit":
                    name_commit = third_word(full_string)
                    if name_commit is not None:
                        error_message3 = commit_func(path, name_commit)
                        if error_message3:
                            click.secho(error_message3, fg='red', bold=True)
                        else:
                            click.secho("The commit worked successfully.", fg='green')
                    else:
                        click.secho("There is no name for the commit", fg='red', bold=True)
                else:
                    if user_input == "checkout":
                        name_commit = third_word(full_string)
                        if name_commit is not None:
                            error_message4 = checkout_func(path, name_commit)
                            if error_message4:
                                click.secho(error_message4, fg='red', bold=True)
                            else:
                                click.secho("The checkout worked successfully", fg='green')
                        else:
                            click.secho("There is no name of commit", fg='red', bold=True)
                    else:
                        if user_input == "status":
                            click.echo(status_func(path))
    else:
        click.secho("the input is none", fg='red', bold=True)

if __name__ == '__main__':
    click_main()
