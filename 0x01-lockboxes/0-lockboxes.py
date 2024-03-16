#!/usr/bin/python3

"""
    A script that determines if all boxes can be
    opened from n number of locked boxes.

"""

from typing import List


def canUnlockAll(boxes: List[List]) -> bool:
    """
        A function that determines if all boxes can be opened.
        :param boxes: List of lists.
        :return: True if all boxes can be opened, otherwise False.

        Description:
            : A key with the same number as a box opens that box
            : All keys will be positive integers
                     : There can be keys that do not have boxes
            : The first box boxes[0] is unlocked
     """

    if not boxes:
        return True

    visited_boxes = set()
    # stack_of_boxes: List[int] = [0]  #PEP8 not allowed
    stack_of_boxes = [0]

    visited_boxes.add(0)

    while stack_of_boxes:
        current_box = stack_of_boxes.pop()
        # visited_boxes.add(current_box)
        # keys_list: List[int] = boxes[current_box]  # PEP not allowed
        keys_list = boxes[current_box]  # list of keys [1, 4, 6]

        for key in keys_list:
            if key not in visited_boxes and key < len(boxes):
                stack_of_boxes.append(key)
                visited_boxes.add(key)

    return len(visited_boxes) == len(boxes)
