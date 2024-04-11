#!/usr/bin/python3
"""A program that solves the N queens problem
"""

import sys
# from typing import List


# def is_safe(board: List[int], row: int, col: int) -> bool:
def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at the
    given position (row, col) on the board.

    Args:
         board (List[int]): The current state of the board,
                            where board[i] represent the column
                            of the queen in row i.
         row (int): The row to check for placing the queen.
         col (int): The column to check for placing the queen.

    Returns:
        bool: True if it's safe to place a queen at a given position,
              otherwise False.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    for i, j in enumerate(range(row - 1, -1, -1)):
        if board[j] == col - i - 1:
            return False

    # Check upper-right diagonal
    for i, j in enumerate(range(row - 1, -1, -1)):
        if board[j] == col + i + 1:
            return False

    return True


# def solve_nqueens(board: List[int], row: int, n: int) -> None:
def solve_nqueens(board, row, n):
    """
    Recursively solve the N Queens problem
    and print every possible solution.

    Args:
        board: List[int]: The current state of the board,
               where board[i] represent the column
               of the queen in row i.

        row (int): The current row being considered.
        n (int): The size of the board and the number of queens
                 to place.

    Returns:
        None
    """
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def main() -> None:
    """
    Entry point to the program.
    Main function parse command-line arguments and solve
    the N Queens problem.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    main()
