#!/usr/bin/env python
import click
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re
import pathlib
import time

tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")


def summarize_file(file):
    """Summarize a file and return the result"""

    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    batch = tokenizer([text], truncation=True, padding="longest", return_tensors="pt")
    translated = model.generate(**batch)
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return tgt_text[0]


# write the summary to a file
def summarize_file_write(file):
    """Summarize a file and write the result to a file"""

    summarized_text = summarize_file(file)
    summarized_file = f"{file}.paragraph-summarized.txt"
    with open(summarized_file, "w", encoding="utf-8") as f:
        f.write(summarized_text)
    return summarized_text


def get_files(directory, pattern, ignore=None, action=None):
    """Get a list of files from a directory"""

    if pattern is None:
        # create a regex pattern that matches transcribed files
        pattern = re.compile(r".*\.transcribed\.txt$")
    files = [
        str(p) for p in pathlib.Path(directory).rglob("*") if pattern.match(str(p))
    ]
    if ignore is not None:
        files = [f for f in files if not ignore in f]
    if action is not None:
        files = [action(f) for f in files]
    return files


# click group
@click.group()
def cli():
    """Summarizes files"""


# discover files
@cli.command("discover")
@click.argument("directory", type=click.Path(exists=True))
def discover(directory):
    """Discover transcribed files"""

    print("Discovering files")
    files = get_files(directory, None, None, None)
    print(files)


# summarize files or a directory
@cli.command("summarize")
@click.option("--file", type=click.Path(exists=True))
@click.option("--directory", "-d", type=click.Path(exists=True))
def summarize(file, directory):
    """Summarize a file and return the result"""

    if directory is not None:
        start = time.time()
        files = get_files(directory, None, None, None)
        for f in files:
            sum_time = time.time()
            summarize_file_write(f)
            print(f"Summarized {f} in {time.time() - sum_time} seconds")
        end = time.time()
        print(f"Summarized total {len(files)} in {end - start} seconds")
    if file is not None:
        print(f"Attempting paragraph summarize: {file}")
        summary = summarize_file(file)
        print(summary)


if __name__ == "__main__":
    cli()
