"""
This does stuff
"""


def count_words(words):
    """
    Return word count
    """
    split_words = words.split()
    return len(split_words)


def count_char(words):
    "Return char count"
    lowercase_string = words.lower()
    letters = {}
    for i in lowercase_string:
        if i in letters.keys():
            letters[i] += 1
        else:
            letters[i] = 1
    return letters


with open("books/frankenstein.txt", encoding='utf-8') as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    count_char(file_contents)
