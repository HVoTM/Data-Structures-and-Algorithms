# A variation to the Fibonacci sequences
# used in coding interview

# A sequence of numbers where each term is the sum of the preceding 
# 3 terms (counting from the fourth one)
# given the first 3 values are 0, 1, 1

" Naive method: using recursive"
def naive(n: int) -> int:
    if n <= 1:
        return n
    if n == 2:
        return 2
    else:
        return naive(n-1) + naive(n-2) + naive(n-3)
    
# TIME COMPLEXITY: exponential 

"Dynamic Programming: Top-down - Memoization"
# utilizing a hashmap, or dictionary, to store previous result
def topdown(n: int, trib: dict[int]) -> int:
    if n <= 1:
        return n

    # check if current index is in dictionary
    if n not in trib:
        trib[n] = topdown(n-1, trib) + topdown(n-2, trib) + topdown(n-3, trib)
    
    return trib[n]

"Dynamic Programming: Bottom-up - Tabulation"
# working on the smaller values of the sequence and build up from them
def bottomup(n: int) -> int:
    # base case check
    if n < 2:
        return n
    if n == 2:
        return 1
    first, second, third = 0, 1, 1
    for i in range(n-2):
        next_seq = first + second + third
        first = second
        second = third
        third = next_seq
    return next_seq 
# Time complexity: linear
# space complexity: O(1), saved as we are using swap and pointer method
# Another less efficient method is using list to store the result
"""
dp = [0] * n
dp[0] = dp[1] = 0;
dp[2] = 1
 
for i in range(3,n) :
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
"""

if __name__ == '__main__':
    try:
        assert bottomup(9) == 81
    except AssertionError:
        print("Test case failed!")