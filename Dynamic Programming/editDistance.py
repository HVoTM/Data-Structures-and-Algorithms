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

# LEETCODE 76. Edit Distance | Topics: Dynamic Programming, String
class Solution:
    def naive(self, word1: str, word2: str) -> int:
        
        def recursion(word_1, word_2, m, n):
            # base case of either word1 or word2 is empty while the other has characters
            # if word1 is empty, only option is to insert all characters of word2 into word1
            # vice versa, word2 is empty, only option is to delete all characters
            if m == 0:
                return n
            if n == 0:
                return m    
        
            # Checking from the right to left
            if word_1[m-1] == word_2[n-1]:
                return recursion(word_1, word_2, m-1, n-1)
            
        # If last characters are not same, consider all three operations on last character of first string,
        # recursively compute minimum cost for all three operations and take minimum of three values.
            return 1 + min(recursion(word_1, word_2, m, n-1), 
                           recursion(word_1, word_2, m-1, n),
                           recursion(word_1, word_2, m-1, n-1))

        return recursion(word1, word2, len(word1), len(word2))

    def topDown(self, word1: str, word2: str) -> int:
        """basically the naive recursive method but we add a memoization element to store the variable"""
        m, n = len(word1), len(word2)
        memo = [[-1 for _ in range(n + 1) for _ in range(m + 1)]]

        def recursion(word1, word2, m, n, memo):
            # Base case, like mentioned above
            if m == 0:
                return n
            if n == 0:
                return m
            # If value is memoized
            if memo[m][n] != -1:
                return memo[m][n]
            
            # If the last character of the two strings are same, get the count for the remaining substring (subproblems)
            if word1[m-1] == word2[n-1]:
                memo[m][n] = recursion(word1, word2, m-1, n-1, memo)
                return memo[m][n]
            
            # If the last characters are not the same, consider all three operations on the last character of 
            # the first word, recursively compute the minimum cost for all three operations and take minimum
            # of three values
            memo[m][n] = 1 + min(recursion(word1, word2, m, n-1, memo), 
                           recursion(word1, word2, m-1, n, memo),
                           recursion(word1, word2, m-1, n-1, memo))

            return memo[m][n]

        return recursion(word1, word2, m, n, memo)

    def bottomUp(self, word1: str, word2: str) -> int:
        """A bottom-up approach | https://www.youtube.com/watch?v=XYi2-LPrwm4&ab_channel=NeetCode"""
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