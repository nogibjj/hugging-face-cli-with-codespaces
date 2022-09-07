#!/usr/bin/env python
import click
from transformers import pipeline
import urllib.request
from bs4 import BeautifulSoup
import wikipedia

# make a function that extracts text from a url
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


# write a function that uses hugging face to return a summary
def process(text):
    summarizer = pipeline("summarization", model="t5-small")
    result = summarizer(text, max_length=180)
    click.echo("Summarization process complete!")
    click.echo("=" * 80)
    return result[0]["summary_text"]


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


# write a click group
@click.group()
def cli():
    pass


# write a subcommand that summarizes a url
@cli.command("url-summarize")
@click.argument("url")
def url_summarize(url):
    """Summarize text from a URL.

    Example:
    ./hfCLI url-summarize https://en.wikipedia.org/wiki/Python_(programming_language)
    """

    text = extract_from_url(url)
    summary = process(text)
    click.echo(summary)


# write a subcommand that summarizes a wikipedia page
@cli.command("wiki-summarize")
@click.argument("wikipage")
def wiki_summarize(wikipage):
    """Summarize text from a Wikipedia page.

    Example:
    ./hfCLI.py wiki-summarize "Python_(programming_language)"
    """

    text = get_page(wikipage)
    summary = process(text)
    click.echo(summary)


# run the cli
if __name__ == "__main__":
    cli()
