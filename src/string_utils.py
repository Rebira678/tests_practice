# src/string_utils.py

def reverse_string(text):
    """
    Returns the reversed version of the string.
    """

    if not text:
        return ""

    reversed_text = ""
    for i in range(len(text)-1,-1,-1):
        reversed_text += text[i]  

    return reversed_text
