"""
Write a function fib(n) that takes in a number as an argument 
The function should return the n-th number of the Fibonnaci sequence

FURTHER INFO ON FIBONACCI SEQUENCE:
https://en.wikipedia.org/wiki/Fibonacci_sequence
- The Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones.
Starting from 0 and 1, the sequence goes like:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,...
"""

# Naive method
def naive_fib(n):
    if n <= 1:
        return n
    return naive_fib(n-1) + naive_fib(n-2)

# Top-down (Memoization method):
# We will work down recursively and save any unencountered solution to a memo
# and utilize them onto sequential problem (work on overlapping sub-problems)
def topdown_fib(n, fib_seq={}): # add a function keyword fib_seq to initialize a default dictionary argument
    if n <= 1:
        return n
    # check if the index is in the dictionary
    if n not in fib_seq:
        # since there is no key yet, we add it with recursive call on smaller sub-problems
        # solve the smaller sub-problems and saved it to the memo (or dictionary here in Python)
        # until we see the solution to the preceding pending sub-problems
        fib_seq[n] = topdown_fib(n-1, fib_seq) + topdown_fib(n-2, fib_seq)

    return fib_seq[n]

# Bottom-up (Tabulation method):
# We will be working on calculating the smaller values of the fibonacci sequence, and build
# larger values from them
# this is just basically how we would do as human, we start from 0 and 1
# then we add up those numbers in an iterative sequence
# In other words, we just work on smaller sub-problems and build up to the larger
def bottomup_fib(n):
    if n == 0:
        return 0
    else:           
        prev_fib, current_fib = 0, 1 # initialize the first 2 numbers
        # Iterate over the required nth sequence
        for i in range(n-1):
            # Utilize the formula: f(n) = f(n-1) + f(n-2)
            new_fib = prev_fib + current_fib
            prev_fib = current_fib
            current_fib = new_fib
        return new_fib

# Driver code:
print(naive_fib(7))
print(topdown_fib(50))
print(bottomup_fib(50))