#!/usr/bin/env python

import click
from transformers import BartTokenizer, BartForConditionalGeneration
import urllib.request
from bs4 import BeautifulSoup
import wikipedia
from newspaper import Article
from newspaper import Config


# mute tensorflow complaints
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


def extract_from_url(url):
    text = ""
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
        },
    )
    html = urllib.request.urlopen(req)
    parser = BeautifulSoup(html, "html.parser")
    for paragraph in parser.find_all("p"):
        print(paragraph.text)
        text += paragraph.text

    return text


# write a function that uses wikipedia to return a page
def get_page(text):
    try:
        page = wikipedia.page(text)
        print(f"Page title: {page.title} parsed with length {len(page.content)}")
        return page.content
    except wikipedia.exceptions.PageError:
        return "Page not found"
    except wikipedia.exceptions.DisambiguationError:
        return "Ambiguous search"


def extract_text(url):
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0"
    config = Config()
    config.browser_user_agent = USER_AGENT
    config.request_timeout = 10
    article = Article(url, config=config)
    article.download()
    article.parse()
    text = article.text
    return text


# clean text from a file so it can be summarized
def clean_text(text):
    return (
        text.replace("\n", " ").replace("\r", " ").replace("\t", " ").replace("  ", " ")
    )


def process(text, model, max_length, truncation):
    text = clean_text(text)
    init_model = BartForConditionalGeneration.from_pretrained(model)
    tokenizer = BartTokenizer.from_pretrained(model)
    inputs = tokenizer(
        text, max_length=1024, return_tensors="pt", truncation=truncation
    )
    summary_ids = init_model.generate(
        inputs["input_ids"],
        num_beams=4,
        min_length=max_length,
        max_length=500,
        early_stopping=True,
    )
    result = tokenizer.batch_decode(
        summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )[0]
    click.echo("Summarization process complete!")
    click.echo("=" * 80)
    return result


@click.group()
def cli():
    """Summarize text from a file or URL"""


@cli.command("encode")
@click.option("--text", "-t", type=str, help="Text to summarize")
@click.option("--file", "-f", type=str, help="File to summarize")
def encode(text, file):
    """Summarize text from a file or URL"""
    if text:
        click.echo(text)
    elif file:
        with open(file, "r", encoding="utf-8") as f:
            click.echo(f.read())


@cli.command("summarize")
@click.option(
    "model", "--model", default="facebook/bart-large-cnn", help="Model to use"
)
@click.option("--url")
@click.option("--file")
@click.option("--wikipage")
@click.option("--news")
@click.option("--max_length", default=400, help="Max length of summary")
@click.option("--truncation", default=True)
def main(url, file, wikipage, news, model, max_length, truncation):
    """Summarize text from a URL, file, or Wikipedia page.

    Examples:
        ./main.py --url https://en.wikipedia.org/wiki/Python_(programming_language)
        ./main.py --file ./data.txt
        ./main.py --wikipage "Python_(programming_language)"
    """

    text = ""
    if url:
        text = extract_from_url(url)
    if wikipage:
        text = get_page(wikipage)
    if news:
        text = extract_text(news)
    elif file:
        with open(file, "r", encoding="utf-8") as _f:
            text = _f.read()
    click.echo(f"Summarized text from -> {url or file or wikipage}")
    click.echo(
        process(
            text=text,
            model=model,
            max_length=max_length,
            truncation=truncation,
        )
    )


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    cli()
