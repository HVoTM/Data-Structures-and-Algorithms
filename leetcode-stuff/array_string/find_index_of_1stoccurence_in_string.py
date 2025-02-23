# LEETCODE 28. Find the Index of the First Occurence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            # Ohh, we use string splicing. Damn I am dumb
            if haystack[i : i+len(needle)] == needle:
                return i
        return -1