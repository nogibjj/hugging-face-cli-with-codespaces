#!/usr/bin/env python

"""
Fine Tuning Example with HuggingFace

Based on official tutorial
"""

from transformers import AutoTokenizer
from datasets import load_dataset
from transformers import AutoModelForSequenceClassification

# Load the dataset
dataset = load_dataset("yelp_review_full")
dataset["train"][100]
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Load the model
model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased", num_labels=5)

