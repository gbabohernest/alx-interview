#!/usr/bin/python3
"""
This module contains functions to determine the winner
of a prime number game played between Maria and Ben.
"""


def is_prime(num):
    """
    Check if a number is prime.
    Args:
        num (int): The number to check.

    Returns:
        bool: True if num is prime, False otherwise.
    """
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def get_primes(n):
    """
    Generate a list of prime numbers.

    Args:
        n (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of prime numbers up to n.
    """
    primes = []

    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)

    return primes


def isWinner(x, nums):
    """
    Determine the winner of the prime number game.

    Args:
        x (int): Number of rounds
        nums (list): List of integers representing the values
                    of n for each round.

    Returns:
        str or None: Name of the player who won the most rounds,
                    or None if winner cannot be determined.

    """
    ben_wins = 0
    maria_wins = 0

    for n in nums:
        primes = get_primes(n)

        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'

    elif ben_wins > maria_wins:
        return 'Ben'

    else:
        return None
