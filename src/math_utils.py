# src/math_utils.py

def average(numbers):
    """
    Return the average of a list of numbers.

    Returns 0 if the list is empty.
    """

    if not numbers:
        return 0

    total = 0
    for n in numbers:
        total += n
    
    if len(numbers)==1:
        raise ValueError("the number is be itself")

    return total / (len(numbers))