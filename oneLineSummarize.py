#!/usr/bin/env python
import click
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import pathlib
import re

tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-xsum")


def summarize_file(file):
    """Summarize a file and return the result"""

    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    batch = tokenizer([text], truncation=True, padding="longest", return_tensors="pt")
    translated = model.generate(**batch)
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return tgt_text[0]

def summarize_file_write(file):
    """Summarize a file and write the result to a file"""

    summarized_text = summarize_file(file)
    summarized_file = f"{file}.one-line-summarized.txt"
    with open(summarized_file, "w", encoding="utf-8") as f:
        f.write(summarized_text)
    return summarized_text

def get_files(directory, pattern, ignore=None, action=None):
    """Get a list of files from a directory"""

    if pattern is None:
        #create a regex pattern that matches transcribed files
        pattern = re.compile(r".*\.transcribed\.txt$")
    files = [
        str(p) for p in pathlib.Path(directory).rglob("*") if pattern.match(str(p))
    ]
    if ignore is not None:
        files = [f for f in files if not ignore in f]
    if action is not None:
        files = [action(f) for f in files]
    return files

@click.group()
def cli():
    """Summarizes files"""

@cli.command("one-line-summarize")
@click.argument("file", type=click.Path(exists=True))
def one_line_summarize(file):
    """Summarizes a file"""

    print(summarize_file(file))
    summarize_file_write(file)

@cli.command("one-line-summarize-dir")
@click.argument("directory", type=click.Path(exists=True))
@click.option("--pattern", default=None, help="Regex pattern to match files")
def one_line_summarize_dir(directory, pattern):
    """Summarizes a directory of files"""

    files = get_files(directory, pattern)
    for file in files:
        print(file)
        summarize_file_write(file)

if __name__ == "__main__":
    cli()
