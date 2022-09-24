#!/usr/bin/env python

""""
Transcribes and summarizes a directory of audio or video files
"""
import pathlib
import re
import click
import whisper



def get_files_recursive(directory, pattern=None, action=None):
    """Return a list of files matching a pattern in a directory recursively"""

    if pattern is None:
        pattern = re.compile(r".*\.(wav|mp3|mp4|avi|mov|flv|mkv|wmv)$")
    files = [str(p) for p in pathlib.Path(directory).rglob("*") if pattern.match(str(p))]
    if action is not None:
        files = [action(f) for f in files]
    return files


def transcribe_file(file):
    """Transcribe a file and return the result"""

    print("Attempting {}".format(file))
    transcribed_file = f"{file}.transcribed.txt"
    #if the file has already been transcribed, skip it
    if pathlib.Path(transcribed_file).exists():
        print("Skipping {}".format(file))
        return transcribed_file
    else:
        print("Confirmed Transcribing {}".format(file))
        model = whisper.load_model("base")
        result = model.transcribe(file)
        with open(transcribed_file, "w") as f:
            f.write(result)
        return transcribed_file

# click group
@click.group()
def cli():
    """Transcribe and summarize a directory of audio or video files"""


@cli.command("transcribe")
@click.option("--directory", default=".", help="Directory to transcribe")
def transcribe(directory):
    """ "Transcribes a directory of audio or video files"""
    files = get_files_recursive(directory)
    for file in files:
        print(f"Transcribing {file}")
        transcribe_file(file)


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
