# LEETCODE 383. Ransom Note
# Concepts: Hashmap, collections.Counter, Python's all()
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        for ch in magazine: 
            if ch not in count:
                count[ch] = 1

            else:
                count[ch] += 1
        
        for ch in ransomNote:
            if ch not in count:
                return False

            if ch in count: 
                count[ch] -= 1
                if count[ch] < 0:
                    return False

        return True

    """
    Solution 1:
    """
    def OneLiner(self, ransomNote: str, magazine: str) -> bool:
        return all([magazine.count(x)>=ransomNote.count(x) for x in set(ransomNote)])

        # Python's all() function will return True if all items in a list are True
        # in this list we initialize, we will record and compare if each character's frequency of occurance
        # in magazine is greater than equal to that of ransomNote
        # if a character in ransomNote has a greater frequency thatn magazine, that means:
        # 1. magazine does not have that character
        # 2. ransomNote uses more instances of that character than the magazine string

    def AlgoMonster(self, ransomNote: str, magazine: str) -> bool:
        "https://algo.monster/liteproblems/383"
        # Create a counter object for all characters in the magazine
        char_count = Counter(magazine)
      
        # Check each character in the ransom note
        for char in ransomNote:
            # Decrement the count for this character in the counter
            char_count[char] -= 1
          
            # If count goes below zero, we cannot construct the note from the magazine
            if char_count[char] < 0:
                return False
      
        # If we haven't returned False, we can construct the ransom note
        return True
