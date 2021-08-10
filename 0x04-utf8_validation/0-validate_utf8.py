#!/usr/bin/python3


def validUTF8(data):
    """Determines if given data represents valid UTF-8 encoding
    Args:
        data: list of integers
    Returns:
        True if valid UTF-8 encoding, otherwise False
    """

    """
    A valid UTF-8 character can be 1 - 4 bytes long.
    For a 1-byte character, the first bit is a 0, followed by its unicode.
    For a n-bytes character (up to 4 bytes), the first n-bits are all ones,
    the n+1 bit is 0, followed by n-1 bytes, most significant 2 bits being 10.
    The input given would be an array of integers containing the data.
    Return true if the data in the array represents a valid UTF-8 encoding.
    The array doesn't contain data for just a single character.
    The array can contain data for multiple characters,
    all of which can be valid UTF-8 characters
    and hence the charset represented by the array is valid.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0
    # For each integer in the data array.
    for each in data:
        # Get the binary representation of the least significant 8 bits
        # for any given number.
        bin_rep = format(each, '#010b')[-8:]

        # If this is the case then start processing a new UTF-8 character.
        if n_bytes == 0:
            # Get the number of 1s in the beginning of the string.
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1
            # 1 byte characters
            if n_bytes == 0:
                continue
            # Invalid scenarios according to the rules of the problem.
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Else, process integers which are a part of
            # a UTF-8 character. The pattern is `10xxxxxx`.
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
        # We reduce the number of bytes to process by 1 after each integer.
        n_bytes -= 1
    # This is for the case where we might not have the complete data for
    # a particular UTF-8 character.
    return n_bytes == 0
