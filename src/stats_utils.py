# src/stats_utils.py

def median(numbers):
    """
    Returns the median of a list of numbers.
    Returns None if the list is empty.
    """

    if not numbers:
        return None

    numbers = sorted(numbers)
    if len(numbers) %2==0:
        mid=len(numbers)//2
        average=(numbers[mid]+numbers[mid-1])/2
        return average

    else:
        mid = len(numbers) // 2
        return numbers[mid]

    