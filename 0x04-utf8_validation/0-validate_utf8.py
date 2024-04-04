#!/usr/bin/python3
"""Write a method that determines if a given data
set represents a valid UTF-8 encoding.

    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to
    handle the 8 least significant bits of each integer.
"""


def validUTF8(data):
    """A function that determines if a
        given data set represent a valid UTF-8 encoding

        :param: data: List of integers
        :return: True if data is valid UTF-8 encoding, else False
    """

    def is_continuation(byte):
        """Helper function to check if a byte is
        a valid UTF-8 continuation byte
        """
        return byte & 0b11000000 == 0b10000000

    # track number of bytes in the current UTF-8 character
    count = 0

    while count < len(data):
        byte = data[count]

        # Determine the number of bytes for this
        # character based on the first byte

        if byte & 0b10000000 == 0:  # 1-byte character
            count += 1

        elif byte & 0b11100000 == 0b11000000:  # 2-byte character
            if count + 1 >= len(data) or not is_continuation(data[count + 1]):
                return False
            count += 2

        elif byte & 0b11110000 == 0b11100000:  # 3-byte character
            if (count + 2 >= len(data) or not is_continuation(data[count + 1])
                    or not is_continuation(data[count + 2])):
                return False
            count += 3

        elif byte & 0b11111000 == 0b11110000:  # 4-byte character
            if (count + 3 >= len(data) or not is_continuation(data[count + 1])
                    or not is_continuation(data[count + 2]) or
                    not is_continuation(data[count + 3])):
                return False
            count += 4
        else:
            return False  # Invalid byte sequence

    return True
    
