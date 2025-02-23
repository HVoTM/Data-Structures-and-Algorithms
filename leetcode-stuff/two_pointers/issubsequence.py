# LEETCODE 392. Is Subsequence
# TOpics: Array, Two Pointers, Dynamic Programming

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize two pointers for both the subsequence and the sequence
        subsequence_index = 0
        sequence_index = 0

        # Iterate over the sequence while there are characters left in both
        # the subsequence and the sequence
        while subsequence_index < len(s) and sequence_index < len(t):
            # If the current characters match, move to the next character in the subsequence
            if s[subsequence_index] == t[sequence_index]:
                subsequence_index += 1
            # Move to the next character in the sequence
            sequence_index += 1
      
        # Return True if all characters in the subsequence have been matched
        # This is indicated by subsequence_index pointing to the end of subsequence
        return subsequence_index == len(s)