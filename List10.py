def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    a0 = 0
    a1 = 0
    i = 0
    b = a0, a1

    while i < len(list1):
        if list1[i] == 0:
            a0 += 1
        if list1[i] == 1:
            a1 += 1
        i += 1
    return b.split()