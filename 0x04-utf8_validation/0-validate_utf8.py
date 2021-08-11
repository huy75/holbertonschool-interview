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

    # Mask to check if the most significant bit is set or not
    mask1 = 1 << 7

    # Mask to check if the second most significant bit is set or not
    mask2 = 1 << 6
    for num in data:

        # Get the number of set most significant bits in the byte if
        # this is the starting byte of an UTF-8 character.
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios according to the rules of the problem.
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # If this byte is a part of an existing UTF-8 character, then we
            # simply have to look at the two most significant bits and we make
            # use of the masks we defined before.
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
