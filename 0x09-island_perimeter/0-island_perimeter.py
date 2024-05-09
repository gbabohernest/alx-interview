#!/usr/bin/python3
"""
  Calculates the perimeter of an island represented by a grid.

  Parameters:
  - grid (list of lists of integers): Represents the island where:
      - 0 represents water
      - 1 represents land
      - Each cell is square with a side length of 1
      - Cells are connected horizontally/vertically (not diagonally)
      - grid is rectangular with width and height not exceeding 100
      - The grid is completely surrounded by water
      - There is only one island (or nothing)
      - The island doesn’t have “lakes” (water inside that isn’t connected
        to the water surrounding the island)

  Returns:
  - perimeter (integer): The perimeter of the island

  Example Usage:
  >>> grid = [
  ...     [0, 0, 0, 0, 0, 0],
  ...     [0, 1, 0, 0, 0, 0],
  ...     [0, 1, 0, 0, 0, 0],
  ...     [0, 1, 1, 1, 0, 0],
  ...     [0, 0, 0, 0, 0, 0]
  ... ]
  >>> island_perimeter(grid)
  12
  """


def island_perimeter(grid):
    """Calculates the perimeter of an island based on the given grid."""
    perimeter = 0

    # iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # check if the current cell is land
            if grid[i][j] == 1:
                # found land, check adjacent cell
                # (up, down, left, right) for water
                # up
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # down
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

                # left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                # right
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
