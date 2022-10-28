def main(list01):
    """
    A list of zeros and ones is given. Find how many zeros are involved and return.
    Args:
        list01(list): parameter
    Returns:
        int: return answer
    """
    b = 0
    i = 0

    while i < len(list01):
        if list01[i] == 0:
            b += 1
        i += 1
    return b