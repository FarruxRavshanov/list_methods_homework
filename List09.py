def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    a = 0
    i = 0
    
    while i < len(fruits):
        if fruits[i] == 'apple':
            a += 1 and fruits.index()
        i += 1
    return fruits