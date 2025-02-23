# LEETCODE 338:  Counting Bits
# Topics: Bit Manipulation, Dynamic Programming

from typing import List

class Solution:
    def countBits_NeetCode(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        # Creating an offset which is to flag if the number of bits required
        # for a binary number expands (from 4 bit, e.g. 1111, to 5 bits, e.g. 10000)
        # we will check the new digit with this offset
        offset = 1

        # Iterate through the numbers from 1 to n
        for i in range(1, n+1):
            # Checking the offset * 2
            # The offset will work from 1, 2, 4, 8, 16, ...
            # this sequence represents the numbers that signifies the expansion of the numbers
            # It works in a binary formula so you can fact check that
            if offset * 2 == i:
                # Set the new offset to the current value
                offset = i
            # Insert the count for i by adding 1 to the current i subtracted with the offset
            # for example: 15 = 1111; 15 - 8 (current offset) = 7
            # 7 = 0111 -> the count of 1's in 7 is 3 
            # then we add 1 to that 
            dp[i] = 1 + dp[i - offset]
            
        return dp
    
    def countBits_AlgoMonster(self, n: int) -> List[int]:
        "https://algo.monster/liteproblems/338"
        # Create a list initialized with zeros for all elements up to n
        ans = [0] * (n+1)
        
        # Loop through all numbers from 1 to n (linear time)
        for i in range(1, n+1):  
            # Use the bit count of the previous registered number that has the same bits
            # except the last set bit using bitwise AND - > (i & (i-1)) 
            # and add 1 for the last set bit
            # This works because i & (i - 1) drops the lowest set bit of i
            # For example, if i = 10100 (binary), i & (i - 1) = 10000, which is i without the last set bit.
            # ans[i & (i - 1)] already contains the count of 1s for 10000,
            # so we just need to add 1 for the dropped bit to get the count for 10100.
            ans[i] = ans[i & (i - 1)] + 1
    
        return ans
        # Time: O(N), Space: O(N)