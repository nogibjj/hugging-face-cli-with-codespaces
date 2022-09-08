#!/usr/bin/env python

from huggingface_hub.inference_api import InferenceApi
import os
import click

API_TOKEN = os.environ["API_TOKEN"]
INFERENCE = InferenceApi(repo_id="deepset/xlm-roberta-base-squad2", token=API_TOKEN)

#
# QA_input = {
#    'question': 'Why is model conversion important?',
#    'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
# }
# res = inference(QA_input)
# print(res)
# model = AutoModelForQuestionAnswering.from_pretrained("deepset/xlm-roberta-base-squad2")

# build a function to answer questions
def answer_question(question, context):
    QA_input = {"question": question, "context": context}
    res = INFERENCE(QA_input)
    return res


# use click to build a command line interface
@click.command()
@click.option(
    "--question", prompt="Your question", help="The question you want to ask."
)
@click.option(
    "--context",
    prompt="Your context",
    help="The context in which you want to ask the question.",
)
def main(question, context):
    """ "Question Answering with Hugging Face

    Example:
        ./question_answer_hugging_face.py --question "Why is model conversion important?" --context "The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks."
    """

    print(answer_question(question, context))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
