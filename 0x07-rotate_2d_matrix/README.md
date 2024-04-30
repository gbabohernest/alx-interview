# 0x07. Rotate 2D Matrix
`Algorithm` `Python`

### Description
This module provides a function `rotate_2d_matrix(matrix)` to rotate an n x n 2D matrix
degree clockwise in-place.


### Logic Explanation
The rotation of a matrix by 90 degree clockwise involves two steps:

1. **Transpose the Matrix**: Swap the elements across the main 
diagonal(top-left to bottom-right diagonal)
2. **Reverse Each Row**: After transposing, reverse each row of the matrix.


### Algorithm

1. **Transpose the Matrix**
   - Iterate through the matrix rows and colunms.
   - Swap the element at `(i, j)` with the element at `(j, i)` for each pair `(i, j)`
   where `i < j`.

2. **Reverse Each Row**
   - Iterate through each row of the matrix.
   - Reverse the elements of each row.


### Example

Consider the following matrix.


    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

After rotating it 90 degree clockwise:

    [[7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]]


### Usage
```python
import matrix_rotation

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matrix_rotation.ratate_2d_matrix(matrix)

for row in matrix:
    print(row)
```


### Output

    [7, 4, 1]
    [8, 5, 2]
    [9, 6, 3]