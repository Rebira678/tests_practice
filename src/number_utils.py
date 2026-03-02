# src/number_utils.py

def find_max(numbers):
    """
    Returns the largest number in a list.
    Returns None if the list is empty.
    """

    if not numbers:
        return None

    maximum = float("-inf")

    for n in numbers:
        if n > maximum:
            maximum = n

    return maximum