import gradio as gr

iface = gr.Interface.load(
    "huggingface/Helsinki-NLP/opus-mt-en-es", examples=[["Hello! My name is Noah"]]
)

iface.launch()
