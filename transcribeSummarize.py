#!/usr/bin/env python

""""
Transcribes and summarizes a directory of audio or video files
"""
import pathlib
import re
import click


# build a function to return all files matching a pattern in a directory recursively
def get_files_recursive(directory, pattern=None):
    """Return a list of files matching a pattern in a directory recursively"""

    if pattern is None:
        pattern = re.compile(r".*\.(wav|mp3|mp4|avi|mov|flv|mkv|wmv)$")
    return [str(p) for p in pathlib.Path(directory).rglob("*") if pattern.match(str(p))]


# click group
@click.group()
def cli():
    """Transcribe and summarize a directory of audio or video files"""


# click command
@cli.command("discover")
@click.option("--directory", default=".", help="Directory to search for files")
@click.option("--pattern", default=None, help="Pattern to match files")
def discover(directory, pattern):
    """Discover files in a directory matching a pattern"""
    files = get_files_recursive(directory, pattern)
    for f in files:
        print(f)


if __name__ == "__main__":
    cli()
