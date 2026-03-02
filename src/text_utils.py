# src/text_utils.py

def word_count(text):
    """
    Count occurrences of each word in a string.

    - Case insensitive
    - Words are separated by whitespace
    - Returns a dictionary {word: count}
    """

    if not text:
        return {}

    words = text.lower().split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts