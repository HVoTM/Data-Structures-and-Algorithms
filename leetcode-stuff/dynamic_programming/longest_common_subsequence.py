# LEETCODE 1143. Longest COmmon Subsequence
# Dynamic Programming

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        "https://www.youtube.com/watch?v=Ua0GhsJSlWM&ab_channel=NeetCode"
        # Tabulation method: initialize a table for the bottom-up approach
        # the values will be originally 0 then we add up from the bottom right
        dp = [[0 for j in range(len(text2) + 1)]for i in range(len(text1) + 1)]

        # Checking for the subproblem in a bottom-up approach
        # Starting from the bottom right and go up to the beginning indices (0, 0) - topleft
        # NOTE: intuitively we will check from the left to right of string
        # so we shift either bottom or right if the current indexes do not match
        # we shift down-right ([i+1][j+1] if match)
        # Our method will work from the bottom up (checking from right to left)
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # Checking if the two characters sliced from the inputs match
                # for example, "a" == "c"?
                # basically, if matched, we have one extra element for the common subsequence
                # and as we are traversing backwards from the end indices
                # We can still preserve the ordering of the sequences
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                # We would just care for the matching string since we would be adding up from there
                # for any upcoming index from the table that does not match
                # we check for the max of the table index going to the right 
                # or table index going down
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[0][0] # the max length of subsequence should be added up by now
        # Time complexity O(m*n) for length m of text1 and n of text2