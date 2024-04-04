# 0x04. UTF-8 Validation
`Algorithm` `Python`

### Problem Description

The task is to implement a method `validUTF8(data)` that
checks if a given data set represents a valid UTF-8 encoding.
The data set is represented by a list of integers, where each
integer represents one byte of data (8 least significant bits).

### Requirements
- A character in UTF-8 can be 1 to 4 bytes long.
- The method should return `True` if the data is a
valid UTF-8 encoding, otherwise `False`.


### Algorithm
### Overview

1. Iterate through each byte in the data set.
2. Determine the number of bytes for each character based on the first byte.
3. Check if the subsequent bytes (if any) are valid continuation bytes.
4. If any byte or byte sequence is invalid, return `False`; otherwise, return `True`.


### Detailed steps
1. Create a helper function`is_continuation(byte)`to check if a byte is a 
valid UTF-8 continuation byte. A continuation byte in UTF-8 always starts 
with the bit pattern `10`.

    ```Python
    def is_continuation(byte):
        return byte & 0b11000000 == 0b10000000


2. Iterate through each byte in the data set using a while loop and an index `count`.
    ```Python
   count = 0
   while i < len(data):
     byte = data[count]

3. Determine the number of bytes for the character based on the first byte's bit pattern:

    - If the first byte starts with `0`, it's a 1-byte character.
    - If it starts with `110`, it's a 2-byte character.
    - If it starts with `1110`, it's a 3-byte character.
    - If it starts with `11110`, it's a 4-byte character.
   
   ```Python
   if byte & 0b10000000 == 0:  # 1-byte character
            count += 1

        elif byte & 0b11100000 == 0b11000000:  # 2-byte character
            if count + 1 >= len(data) or not is_continuation(data[count + 1]):
                return False
            count += 2

        elif byte & 0b11110000 == 0b11100000:  # 3-byte character
            if count + 2 >= len(data) or not is_continuation(data[count + 1]) \
                    or not is_continuation(data[count + 2]):
                return False
            count += 3

        elif byte & 0b11111000 == 0b11110000:  # 4-byte character
            if count + 3 >= len(data) or not is_continuation(data[count + 1]) \
                    or not is_continuation(data[count + 2]) \
                    or not is_continuation(data[count + 3]):
                return False
            count += 4
        else:
            return False  # Invalid byte sequence

4. Check if the subsequent bytes (if any) are valid continuation bytes by
calling the helper function `is_continuation(byte)`.
5. If any byte or byte sequence is invalid (e.g., not a valid UTF-8 start byte,
missing continuation bytes, etc.), return `False`. Otherwise, continue to the
next byte until the end of the data set is reached.

6. If the loop completes without encountering any invalid sequences, return `True`,
indicating that the data set represents a valid UTF-8 encoding.

   
### Example Usage
- In the example usage below, the first two data sets represent valid UTF-8 encodings,
while the third data set is invalid due to the out-of-range byte value 256.

   ```Python
   data = [65]
   print(validUTF8(data))  # Output: True

   data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
   print(validUTF8(data))  # Output: True

   data = [229, 65, 127, 256]
   print(validUTF8(data))  # Output: False
