# 0x01. Lockboxes
```Algorithm``` ```Python```

## Objective
This Python script solves the problem of determining if all boxes can be opened from a list of locked boxes.

### Overview
The script provides a function `canUnlockAll(boxes: List[List]) -> bool` that takes a list of lists
representing locked boxes as input and returns `True` if all boxes can be opened or `False` otherwise.
Each box contains keys that can open other boxes, and the script simulates unlocking the boxes
to check if they can all be opened starting from the first box (`boxes[0]`).


### Problem statement
You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1`
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers 
  - There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`


### Algorithm Explanation
1. **Initialize Variables**:
    - `visited_boxes`: A set to keep track of visited boxes.
    - `stack_of_boxes`: A stack (implemented as a list) to perform depth-first search (DFS).

2. **DFS Traversal**:
   - Start by adding the first box (`boxes[0]`) to the stack_of_boxes and mark it as visited.
   - While the `stack_of_boxes` is not empty:
     - Pop a box (`current_box`) from the top of the `stack_of_boxes`.
     - Get the keys in the `current_box`.
     - For each key in the keys list:
       - If the key corresponds to an unvisited box and is a valid box number, add that box to
         the `stack_of_boxes` and mark it as visited.

3. **Check if All Boxes Can Be Opened**:
   - After completing the DFS traversal, check if the number of visited boxes (`len(visited_boxes)`) is equal to the total number of boxes (`len(boxes)`).
   - if yes, return `True`; otherwise, return `False`.

### Function Parameters
- `boxes` : List of lists representing locked boxes. Each inner list contains keys that can open other boxes.


### Assumptions and Constraints
- A key with the same number as a box opens that box.
- All keys are positive integers.
- There can be keys that do not have corresponding boxes.
- The first box (`boxes[0]`) is initially unlocked.

### Usage
```Python
boxes = [[1], [2], [3], []]
result = canUnlockAll(boxes)
print(result)  # Output: True (all boxes can be opened)
