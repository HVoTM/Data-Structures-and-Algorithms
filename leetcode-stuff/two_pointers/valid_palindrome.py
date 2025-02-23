# LEETCODE 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "" # extra memory
        for ch in s:
            if ch.isalnum():
                new_s += ch.lower()
        
        return new_s == new_s[::-1] # extra memory
        # NOTE: list[::-1] -> reverse of a string
        """
        Time: O(N), Space: O(N)
        """
        # 
    def NeetCode(self, s: str) -> bool:
        # https://www.youtube.com/watch?v=jJXJ16kPFWg&ab_channel=NeetCode
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not alphaNum(s[l]):
                l += 1
            while r > l and not alphaNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
        # Utility function to check the alphanumerical validity of a character
        def alphaNum(c):
            # ord()
            return (ord('A') <= ord(c) <= ord('Z') or 
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))
    
        # No extra memory needed -> Space: O(1)