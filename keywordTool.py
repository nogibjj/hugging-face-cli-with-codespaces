import yake
import click
import pathlib

#build a function that extract keyswords from text file
def extract_keywords(text_file):
    #load the text file
    with open(text_file, 'r') as f:
        text = f.read()
    #extract keywords
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(text)
    #print the keywords
    for kw in keywords:
        print(kw)

#build a function that extract keyswords from text file and writes to a file with keyword in the name
def extract_keywords_write(text_file):
    #load the text file
    with open(text_file, 'r') as f:
        text = f.read()
    #extract keywords
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(text)
    #write the keywords to a file
    with open(text_file + '.keywords', 'w') as f:
        for kw in keywords:
            f.write(str(kw) + '')

#build a click group
@click.group()
def cli():
    """A command line tool for extracting keywords from text files"""

#build a click command for extracting keywords from text file
@cli.command("keywords")
@click.argument('text_file', type=click.Path(exists=True)) 
def keywords(text_file):
    """Extract keywords from a text file"""
    
    extract_keywords(text_file)

#if the script is run from the command line, run the cli
if __name__ == '__main__':
    cli()