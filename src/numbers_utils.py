def second_largest(numbers):
    """
    Returns the second largest number in the list.
    Returns None if it doesn't exist.
    """

    if len(numbers) < 2:
        return None

    unique = list(set(numbers))
    unique.sort()

    if len(unique) < 2:
        return None

    return unique[-2]