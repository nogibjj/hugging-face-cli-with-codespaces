#!/usr/bin/env python

""""
Transcribes and summarizes a directory of audio or video files
"""
import pathlib
import re
import click
import whisper


# build a function to transcribe a file
def transcribe_file(file_path, model_type="base", language="en-US"):
    """Transcribes a file and saves the transcript"""

    if not check_transcript_exists(file_path)[0]:

        model = whisper.load_model(model_type, language)
        print(f"Transcribing {file_path}")
        transcript = model.transcribe(file_path, language=language)
        file_name = pathlib.Path(file_path).stem
        directory = pathlib.Path(file_path).parent
        transcript_file = directory / f"{file_name}.transcript.txt"
        with open(transcript_file, "w", encoding="utf-8") as f:
            f.write(transcript)
    else:
        print(f"Transcript exists for {file_path}")


def get_files_recursive(directory, pattern=None):
    """Return a list of files matching a pattern in a directory recursively"""

    if pattern is None:
        pattern = re.compile(r".*\.(wav|mp3|mp4|avi|mov|flv|mkv|wmv)$")
    return [str(p) for p in pathlib.Path(directory).rglob("*") if pattern.match(str(p))]


def check_transcript_exists(
    file_path, summary_pattern="*.summary.txt", transcript_pattern="*.transcript.txt"
):
    """Checks if a transcript exists for a given file"""

    # get the file name
    file_name = pathlib.Path(file_path).stem

    # get the directory
    directory = pathlib.Path(file_path).parent

    # get the list of files that match the summary pattern
    summary_files = get_files_recursive(directory, re.compile(summary_pattern))

    # get the list of files that match the transcript pattern
    transcript_files = get_files_recursive(directory, re.compile(transcript_pattern))

    # check if the transcript file exists
    transcript_exists = any([file_name in f for f in transcript_files])

    # check if the summary file exists
    summary_exists = any([file_name in f for f in summary_files])
    return transcript_exists, summary_exists


# click group
@click.group()
def cli():
    """Transcribe and summarize a directory of audio or video files"""


@cli.command("transcribe")
@click.option("--model", default="base", help="Model to use for transcription")
@click.option("--language", default="en-US", help="Language to use for transcription")
@click.option("--directory", default=".", help="Directory to transcribe")
def transcribe(model, language, directory):
    """ "Transcribes a directory of audio or video files"""
    files = get_files_recursive(directory)
    for file in files:
        print(f"Transcribing {file}")
        transcribe_file(file, model, language)


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
