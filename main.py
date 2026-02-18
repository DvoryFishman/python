from pathlib import Path

import click
import os

from FolderAndFile import second_word, third_word
from add_step import add_func
from checkout_step import checkout_func
from commit_step import commit_func
from init_step import init_func
from status_step import status_func

REPO_PATH = os.getcwd()


@click.command()
@click.option('--command', 'command', prompt='Enter the command', help='The command to run.')
def main(command):

    cmd = (command or '').strip()
    subcommand = second_word(cmd)
    if subcommand is None:
        click.secho('The input is empty.', fg='red', bold=True)
        return

    if subcommand == 'init':
        error_message = init_func(REPO_PATH)
        if error_message:
            click.secho(error_message, fg='red', bold=True)
        else:
            click.secho('Initialization completed successfully.', fg='green')

    elif subcommand == 'add':
        arg = third_word(cmd)
        if arg is None:
            click.secho('There is no name for the add', fg='red', bold=True)
        else:
            error_message = add_func(REPO_PATH, arg)
            if error_message:
                click.secho(error_message, fg='red', bold=True)
            else:
                click.secho('Add file successfully', fg='green')

    elif subcommand == 'commit':
        commit_name = third_word(cmd)
        if commit_name is None:
            click.secho('There is no name for the commit', fg='red', bold=True)
        else:
            error_message = commit_func(REPO_PATH, commit_name)
            if error_message:
                click.secho(error_message, fg='red', bold=True)
            else:
                click.secho('The commit worked successfully.', fg='green')

    elif subcommand == 'checkout':
        commit_name = third_word(cmd)
        if commit_name is None:
            click.secho('No commit name provided', fg='red', bold=True)
        else:
            error_message = checkout_func(REPO_PATH, commit_name)
            if error_message:
                click.secho(error_message, fg='red', bold=True)
            else:
                click.secho('The checkout worked successfully', fg='green')

    elif subcommand == 'status':
        untracked, modified, staged = status_func(REPO_PATH)

        click.echo("\n=== Repository Status ===\n")

        click.echo("Untracked files:")
        if untracked:
            for file in untracked:
                click.echo(f"  {file}")
        else:
            click.echo("  (none)")

        click.echo("\nModified (not staged):")
        if modified:
            for file in modified:
                click.echo(f"  {file}")
        else:
            click.echo("  (none)")

        click.echo("\nStaged (not committed):")
        if staged:
            for file in staged:
                click.echo(f"  {file}")
        else:
            click.echo("  (none)")

        click.echo()

    else:
        click.secho(f'Unknown command: {subcommand}', fg='red', bold=True)


if __name__ == '__main__':
    main()
