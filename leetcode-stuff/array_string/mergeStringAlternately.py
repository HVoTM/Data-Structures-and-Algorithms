# LEETCODE 1768. Merge Strings Alternately
# Topic: string, Two pointers

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # We will be using the two pointers technique to pass along the two strings alternately
        i, j = 0, 0
        # Initialize an empty string to return as the output
        ans = ""
        # Maintain the loop if both pointers are still in the range of indices
        while i < len(word1) and j < len(word2):
            # Just adding the character and increment the pointer indices
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1
        # Checking if word1 or word2 runs out first, we append the remaining
        if i >= len(word1):
            ans += word2[j:]
        else:
            ans += word1[i:]

        return ans # Time: O(N), Memory: O(1)