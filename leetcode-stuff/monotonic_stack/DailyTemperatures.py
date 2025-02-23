# LEETCODE 739. Daily Temperatures
# topic: Array, Stack

from typing import List

class Solution:
    def naive(self, temperatures: List[int]) -> List[int]:
        left, right = 0, 0
        ans = []

        count = 0
        while left <= len(temperatures) - 2:
            while temperatures[left] >= temperatures[right]:
                if right >= len(temperatures) - 1:
                    count = 0
                    break
                else:
                    right += 1
                    count += 1
            ans.append(count)
            count = 0
            left += 1
            right = left
        
        ans.append(0)
        "O(n^2) time complexity"
        return ans
    
    def monotonicStackMethod(self, temperatures: List[int]) -> List[int]:
        """
        Monotonic stack solution
        https://www.youtube.com/watch?v=cTBiBSnjO3c&ab_channel=NeetCode
        """
        # Initialize a list of zeros for the answer with the same length as the input list
        res = [0] * len(temperatures)
        # Initialize an empty list to be used as a stack to keep track of temperatures indices
        # Monotonic decreasing order
        stack = [] # pair: [temp, index]
        
        for i, t in enumerate(temperatures):
            # Loop through the stack as long as it's not empty and the current temperature
            # is greater than the temperature at the index of the last element in the stack
            # retrieve the right end of the stack and index 0 for the temperature
            while stack and t > stack[-1][0]:
                stackTemperature, stackIndex = stack.pop()
                # Calculate the number of days between the previous and current temperature
                # and update the answer list
                res[stackIndex] = (i - stackIndex)
            stack.append([t, i])

        return res  # Runtime: O(N)
# Driver code
test = Solution() 
temperatures = [73,74,75,71,69,72,76,73]
print(test.naive(temperatures))