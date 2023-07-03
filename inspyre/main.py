import textwrap
import click
import requests

API_URL = 'https://en.wikipedia.org/api/rest_v1/page/random/summary'

@click.command()
def main():
    """The hypermodern Python project."""
    with requests.get(API_URL, timeout=1000) as response:
        response.raise_for_status()
        data = response.json()

    title = data['title']
    extract = data['extract']

    click.secho(title, fg='green')
    click.echo(textwrap.fill(extract))
