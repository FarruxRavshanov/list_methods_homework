def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i = 0
    s = []
    while i < len(fruits):
        if fruits[i] != 'apple':
            fruits.append(s)
        i -= 1
        i += 1
    return s