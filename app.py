#!/usr/bin/env python


""""
Gradio docs are here: https://gradio.app/docs

"""

from transformers import pipeline
import gradio as gr
import wikipedia


# write a function that parses a wikipedia page and then summarizes it
def get_page(text):
    try:
        page = wikipedia.page(text)
        print(f"Page title: {page.title} parsed with length {len(page.content)}")
        return page.content
    except wikipedia.exceptions.PageError:
        return "Page not found"
    except wikipedia.exceptions.DisambiguationError:
        return "Ambiguous search"


model = pipeline("summarization")

# write a function that uses hugging face to return a summary
def process(text):
    summarizer = pipeline("summarization", model="t5-small")
    result = summarizer(text, max_length=180)
    return result[0]["summary_text"]


# use gradio to create a web interface take a wikipedia page and summarize it
iface = gr.Interface(
    fn=process,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Enter wikipedia page like...House_of_the_Dragon",
    ),
    outputs="text",
)


if __name__ == "__main__":
    iface.launch()

# with gr.Blocks() as demo:
#    textbox = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
#    gr.Interface(fn=predict, inputs=textbox, outputs="text")

# demo.launch()
