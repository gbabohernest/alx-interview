# 0x05-nqueens
`Algorithm` `Python`


### Overview
The N Queens problem is a classic chess problem that involves placing N queens
on an N×N chessboard such that no two queens threaten each other. In chess, a
queen can attack horizontally, vertically, and diagonally. The challenge is to
find all possible arrangements of N queens on the board where none of them can
attack each other.

### Algorithm
The solution to the N Queens problem is typically implemented using a backtracking
algorithm.
The algorithm works as follows:

1. **Initialize the Board**: Start with an empty NxN chessboard, where each cell 
represents a potential position for a queen. Initially, all cells are empty.

2. **Place Queens One by One**: Begin placing queens one by one, starting from
the first row and moving row by row. For each row, try placing a queen in each
column of that row.

3. **Check if Placement is Safe**: Before placing a queen in a particular cell, check
if it's safe to do so. Safety means the queen will not be threatened by any other queens
already placed on the board. This involves checking if there are no other queens in the
same column, same row, or diagonally attacking the current cell.

4. **Backtrack if Placement is Unsafe**: If placing a queen in a cell leads to an unsafe
configuration, backtrack and try placing the queen in a different cell in the same row.
If no safe cell is found in the current row, backtrack to the previous row and try different
placements.

5. **Repeat Until All Queens are Placed**: Continue this process of placing queens and backtracking
until all N queens are successfully placed on the board without threatening each other.

6. Print Solutions: Whenever a valid arrangement of queens is found, print the positions of the 
queens on the board as a solution.


### Concepts

 #### Backtracking
Backtracking is a technique used in algorithm design to systematically search for solutions to
problems, especially those involving combinatorial choices or constraints. It is based on recursion
and tries all possible options but abandons a branch of the search tree as soon as it realizes
the current path cannot lead to a valid solution.

In the N Queens problem, backtracking allows us to explore different combinations of queen
placements while ensuring that no two queens attack each other. If we reach a point where 
a safe placement is not possible, we backtrack and try alternative placements.


 #### Recursion
Recursion plays a crucial role in solving the N Queens problem. The recursive function
`solve_nqueens` is responsible for placing queens row by row. It recursively explores
all possible placements in each row while maintaining the safety constraints imposed by
the problem.


 #### Safety Checks
The `is_safe` function is used to determine whether it's safe to place a queen in a specific cell
on the board. It checks for conflicts in the same column, same row, and diagonals.
This safety checking ensures that queens do not threaten each other, as per the rules of chess.



### Usage
To use the `0x05-nqueens`

1. Ensure you have python installed n your system.
2. Run the `0-nqueens.py` script from the command line with the desired value of N (number of queens).

**Example**

    python 0-nqueens.py 4


**Output**

    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]

Each solution represents the positions of queens on the chessboard,
where each pair   `[row. col`] indicates the row and column of a queen.
