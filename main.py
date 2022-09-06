#!/usr/bin/env python

##Something is broken with wikipedia.page()
##I'm not sure what the problem is
##W tensorflow/core/framework/cpu_allocator_impl.cc:82] Allocation of 10689559328 exceeds 10% of free system memory.
#Killed

import click
from transformers import pipeline
import urllib.request
from bs4 import BeautifulSoup
import wikipedia


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



#write a function that uses wikipedia to return a page
def get_page(text):
    try:
        page = wikipedia.page(text)
        return page.content
    except wikipedia.exceptions.PageError:
        return "Page not found"
    except wikipedia.exceptions.DisambiguationError:
        return "Ambiguous search"

def process(text):
    summarizer = pipeline("summarization", model="t5-small")
    result = summarizer(text, max_length=180)
    click.echo("Summarization process complete!")
    click.echo("=" * 80)
    return result[0]["summary_text"]


@click.command()
@click.option("--url")
@click.option("--file")
@click.option("--wikipage")
def main(url, file, wikipage):
    """Summarize text from a URL, file, or Wikipedia page.
    
    Examples:
        ./main.py --url https://en.wikipedia.org/wiki/Python_(programming_language)
    """


    if url:
        text = extract_from_url(url)
    if wikipage:
        text = get_page(wikipage)
    elif file:
        with open(file, "r", encoding="utf-8") as _f:
            text = _f.read()
    click.echo(f"Summarized text from -> {url or file or wikipage}")
    click.echo(process(text))

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()