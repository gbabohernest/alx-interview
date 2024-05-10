# 0x09. Island Perimeter
`Algorithm` `Python`

### Problem Description
Given a grid representing an island surrounded by water, calculate the perimeter of the island.
Each cell in the grid can either be land (represented by 1) or water (represented by 0). Cells
are connected horizontally and vertically (not diagonally). The grid is rectangular with its width
and height not exceeding 100, and it is completely surrounded by water. There is only one island
(or nothing), and the island does not have “lakes” (water inside that isn’t connected to the water
surrounding the island).


### Algorithm
The algorithm for calculating the perimeter of the island involves iterating through each cell in
the grid and counting the number of edges where land meets water.

#### **Step-by-step breakdown of the algorithm:** ####

 - **Initialize the perimeter to zero(0):**
 First create a variable called **`perimeter`** to keep track of the total perimeter of the island.


 - **Iterate through each cell in the grid:**
Using nested loop technique, iterate through each cell in the grid. The outer loop iterates over rows,
and the inner loop iterates over columns.


 - **Check if the current cell is Land:**
For each cell, we check if its value is 1, indicating land. If it is, we proceed with calculating the
edges and adding to the perimeter.


 - **Count horizontal edges:**
Check the adjacent cells (left and right) of the current land cell. If an adjacent cell is water (0),
it contributes to the horizontal edge count. We increment the perimeter count by 1 for each horizontal edge.


 - **Count vertical edges:**
Similarly, we check the cells above and below the current land cell. If these adjacent cells are water,
they contribute to the vertical edge count. We increment the perimeter count by 1 for each vertical edge.


 - **Return the total perimeter:**
After iterating through all land cells and counting the edges, return the total perimeter calculated.


### Usage

```python
from island_perimeter import island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

perimeter = island_perimeter(grid)
print(perimeter)  # Output: 12
```
