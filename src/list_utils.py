# src/list_utils.py

def remove_duplicates(items):
    """
    Remove duplicate items from a list
    while preserving order.
    """
    seen=set()
    result=[]

    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result