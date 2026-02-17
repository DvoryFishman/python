#!/usr/bin/env python
# -*- coding: utf-8 -*-


import click

from add_step import add_func
from checkout_step import checkout_func
from commit_step import commit_func
from init_step import init_func
from status_step import status_func
from pathlib import Path

REPO_PATH = Path(r'C:\דבורי\שנה ב\פייתון\בדיקה של הפריקט')


@click.group()
def cli():
    pass


@cli.command()
def init():

    error_message = init_func(REPO_PATH)
    if error_message:
        click.secho(error_message, fg='red', bold=True)
    else:
        click.secho('Initialization completed successfully.', fg='green')


@cli.command()
@click.argument('name')
def add(name):

    error_message = add_func(REPO_PATH, name)
    if error_message:
        click.secho(error_message, fg='red', bold=True)
    else:
        click.secho('Add file successfully', fg='green')


@cli.command()
@click.argument('message', nargs=-1, required=True)
def commit(message):

    commit_name = ' '.join(message).strip()
    error_message = commit_func(REPO_PATH, commit_name)
    if error_message:
        click.secho(error_message, fg='red', bold=True)
    else:
        click.secho('The commit worked successfully.', fg='green')


@cli.command()
@click.argument('commit_id')
def checkout(commit_id):

    error_message = checkout_func(REPO_PATH, commit_id)
    if error_message:
        click.secho(error_message, fg='red', bold=True)
    else:
        click.secho('The checkout worked successfully', fg='green')


@cli.command()
def status():

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


if __name__ == '__main__':
    cli()
