# LEETCODE 17. Letter Combinations of a Phone Number

# Topic: Hash Table, String, Character

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Create a dictionary to storee the values of digits to characters
        button_mapping = {"1": "", "2":"abc", "3":"def", "4":"ghi", "5":"jkl","6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz", "0":" "}
        # Initialize the answer to store for possible letter combinations
        ans = []

        def backtrack(i, currStr):
            # base case if the length of the string meets the requirements to return as one variable
            if len(currStr) == len(digits):
                ans.append(currStr)
                return # we end this search for the corresponding characters and backtrack to the next 
                # viable solution

            # We start by the first index of the digits combination
            # search for the continuing possible letter combinations as we increment the index
            # and continuously update the string to return
            for c in button_mapping[digits[i]]:
                backtrack(i+1, currStr + c)

        # Initialize the backtracking step, starting with index 0 and an empty string
        if digits:
            backtrack(0, "")

        return ans