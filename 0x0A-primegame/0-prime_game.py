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


def can_make_move(primes, remaining_nums):
    """
    Check if a move can be made in the prime
    number game.

    Args:
        primes (list): List of prime numbers.
        remaining_nums (list): List of remaining numbers in the game.

    Returns:
        bool: True if a move can be made, False otherwise.

    """
    for prime in primes:
        if prime in remaining_nums:
            return True

    return False


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
    winners = {'Maria': 0, 'Ben': 0}

    for n in nums:
        primes = get_primes(n)
        remaining_nums = list(range(1, n + 1))
        turn = 'Maria'

        while can_make_move(primes, remaining_nums):
            if turn == 'Maria':
                for prime in primes:
                    if prime in remaining_nums:
                        for num in range(prime, n + 1, prime):
                            if num in remaining_nums:
                                remaining_nums.remove(num)
                        break
                turn = 'Ben'

            else:
                for prime in primes:
                    if prime in remaining_nums:
                        for num in range(prime, n + 1, prime):
                            if num in remaining_nums:
                                remaining_nums.remove(num)
                        break
                turn = 'Maria'

        if turn == 'Ben':
            winners['Ben'] += 1
        else:
            winners['Maria'] += 1

    max_wins = max(winners.values())
    if list(winners.values()).count(max_wins) == 1:
        return max(winners, key=winners.get)
    else:
        return None
