def is_palindrome(text):
    """
    Returns True if the text is a palindrome.
    Otherwise returns False.
    """

    cleaned = text.lower()
    cleaned="".join(w for w in cleaned if w.isalnum())
    return cleaned == cleaned[::-1]