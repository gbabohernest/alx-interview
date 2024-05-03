#!/usr/bin/python3
"""
This module provides a function for calculating the
fewest number of coins needed to meet a given total
amount, using a dynamic programming approach.
"""


def makeChange(coins, total):
    """

    Args:
        coins: List of integers representing the values
               of the coins available for use. The values
               are assumed to be greater than 0.

        total: Integer representing the total amount to be
               met using the available coins

    Returns:
        Integer: The fewest number of coins needed to meet
                 the total amount.

                 0 if the total amount is 0 or less.
                -1 if the total amount cannot be met by any
                 combination of coins.

    """
    if total <= 0:
        return 0

    min_coins_needed = [float('inf')] * (total + 1)
    min_coins_needed[0] = 0

    for current_total in range(1, total + 1):
        for coin_value in coins:
            if coin_value <= current_total:
                min_coins_needed[current_total] = min(
                    min_coins_needed[current_total],
                    min_coins_needed[current_total - coin_value] + 1)

    if min_coins_needed[total] == float('inf'):
        return -1
    else:
        return min_coins_needed[total]
