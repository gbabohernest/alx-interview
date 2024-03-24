# 0x02-minimum_operations

`Dynamic Programming`

## Problem Statement

In a text file, there is a single character `'H'`. Your text editor can execute only two
operations in this file:`Copy All and Paste`. Given a number `n`, write a method that calculates
the fewest number of operations needed to result in exactly `n` `'H'` characters in the file.


## Algorithm and Concepts

### Prime Factorization Approach
The solution to this problem is based on the prime factorization of the
given number `n`. Here are the key concepts and steps involved in the algorithm:

1. Initialization
   - Initialize the total number of operations (`operations`) to 0.
   - Start with the smallest prime factor (`factor`) as 2.

2. Factorization Loop
   - Loop while the square of the current factor (`factor * factor`) is less than or equal to `n`.
   - Check if the current factor divides `n` evenly:
     - If true, update `n` by dividing it by the factor (`n //= factor`) and increment
       `operations` by factor.
     - If false, increment `factor` by 1 to check the next factor.

3. Remaining Prime Factor
   - After the loop, if `n` is still greater than 1, add it to `operations` since it's a prime factor.

4. Return Operations
   - Return the total number of operations (`operations`), which represents the fewest
     operations needed to achieve `n` `'H'` characters.

   ### Example Run
    For `n = 9`:

   - Initialize `operations = 0`, `factor = 2`
   - Loop iterations:
     - Factor 2 divides 9, so update `n` to 4 and `operations` to 2 (2 operations: Copy All and Paste).
     - Factor 2 does not divide 4, so increment `factor` to 3.
     - Factor 3 divides 4, so update `n` to 1 and `operations` to 5 (3 operations: Copy All, Paste, and Paste).
     - Factor 3 does not divide 1, so loop ends.
   - Remaining prime factor 3 is added to `operations`.
   - Return `operations = 6`, which is the fewest operations needed to achieve 9 `'H'` characters.

## Usage
```Python
n = 9
operations_needed = minOperations(n)
print("Min num of operations to reach {} char: {}".format(n, minOperations(n)))  # Output: Min num of operations to reach 9 char: 6
