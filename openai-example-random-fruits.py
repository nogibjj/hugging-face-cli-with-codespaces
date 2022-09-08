"""
Write a function that randomly picks fruit from a list of 10 fruits
"""

import random


def random_fruit():
    fruits = [
        "apple",
        "banana",
        "orange",
        "strawberry",
        "kiwi",
        "grapes",
        "blueberry",
        "melon",
        "pear",
        "pineapple",
    ]
    return random.choice(fruits)


print(random_fruit())
