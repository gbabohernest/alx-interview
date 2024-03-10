# 0x00. Pascal's Triangle
```Algorithm``` ```Python```


### Pascal Triangle
 Pascal's triangle is a triangular array of numbers where each number is the sum
 of the two numbers directly above it. The first and last numbers in each row are always 1.
 
### Problem Statement
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer


### Solution Overview
The `pascal_triangle` function generates Pascal's triangle with `n` rows. This function takes
an integer `n` as input and return a list of lists of integers representing Pascal's triangle.


### Algorithm Explanation
1. Base Case Handling:
   - if `n` is less then or equal to 0, the function returns an empty list, as Pascal's triangle
     cannot have negative or zero rows.

2. Constructing the Triangle:
   - Initialize the `triangle` list with the top row `[1]`.
   - For each row from the second row to the `n`th  row:
     - Start building the row with `[1]`.
     - Iterate over each element in the current row, expect the first and last elements.
       - Obtain the diagonal values from the row directly above.
       - Sum the diagonal values to get the current element.
       - Append the sum to the current row.
     - End the with `1`.
     - Append the completed row to the `triangle` list.


### Logic Breakdown:
- The inner loop iterates over each element in a row, except the first and last elements, to calculate the values based on the sum of the diagonal elements from the row above.
- The diagonal elements to the left (diagonal_left) and right (diagonal_right) of the current position are obtained from the previous row.
- These diagonal elements are summed to compute the value of the current position.
- The resulting row is then appended to the triangle list.

### Example Usage
    triangle = pascal_triangle(5)
    print(triangle)

This will generate the Print Pascal's triangle with 5 rows
```[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]```
