#!/usr/bin/python3
"""
This module provides a function for calculating the
fewest number of coins needed to meet a given total
amount, using a dynamic programming approach (memoization).
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

    memo = {}

    def cal_min_num_of_coin_recursively(amount):
        """Recursively calculates the minimum
           number of coins needed for each amount
           using memoization for optimization.
        """
        if amount in memo:
            return memo[amount]

        if amount < 0:
            return float('inf')

        if amount == 0:
            return 0

        min_coins = float('inf')
        for coin in coins:
            if amount - coin >= 0:
                min_coins = min(min_coins, cal_min_num_of_coin_recursively(
                    amount - coin) + 1
                                )
        memo[amount] = min_coins
        return min_coins

    result = cal_min_num_of_coin_recursively(total)
    return result if result != float('inf') else -1
