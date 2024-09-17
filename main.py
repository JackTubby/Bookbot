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
    """
    Return a dictionary with character frequencies.
    """
    lowercase_string = words.lower()
    letters = {}
    for char in lowercase_string:
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters


def report(book, count, char):
    """
    Print a report with word count and sorted character frequencies.
    Sort first by frequency (descending), then by alphabetical order.
    """
    print(f"--- Begin report of {book} ---")
    print(f"{count} words found in the document\n")

    # Sort the dictionary by frequency first, then alphabetically by character
    sorted_chars = sorted(char.items(), key=lambda x: (-x[1], x[0]))

    for key, value in sorted_chars:
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")


with open("books/frankenstein.txt", encoding='utf-8') as f:
    file_contents = f.read()
    file_name = f.name
    word_count = count_words(file_contents)
    char_amount = count_char(file_contents)
    report(file_name, word_count, char_amount)
