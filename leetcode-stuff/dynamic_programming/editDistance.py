"""
Real-World Applications of Edit Distance:
-----------
Spell Checking and Auto-Correction
DNA Sequence Alignment
Plagiarism Detection
Natural Language Processing
Version Control Systems
String Matching
"""

# LEETCODE 76. Edit Distance
# Topics: Dynamic Programming, String

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Initialize a 2D array to store the number of steps to convert word1 to word2
        # We will be working in a bottom-up approach
        # columnwise: word2, row-wise: word1
        # dimension: (m+1) x (n+1) | m: length of word1, n: length of word2
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # Initialize the subproblems' base case of an empty string with an existent string 
        # predominantly will be insertion/deletion depending on the word1 or word2 being empty
        # One example to think of for why we do this: word1 = "", word2 = "abc" -> how many operations?
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        # Starting in the tabulation approach, we go from the bottom right corner of the table, which is 0
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                # if the compared characters are the same, we go up to the left (diagonally)
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                
                # Given the other cases, we refer to the cell to the left, upper one, and the diagonal
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        
        # return the cell value in the top-left corner, which should have attained the max number of characters for now
        return dp[0][0]