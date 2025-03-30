# LEETCODE: 290. WOrd Pattern
# Topics: Hash table, String

# NOTE: the rules in the problem statement dictate these conditional checks

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Retrieve the string s into an array of words, given the constraints: single space, no leading or trailing space
        s = s.split() # https://docs.python.org/3/library/stdtypes.html#str.split
        # Create a hash table
        pattern_hashmap = dict()
        # Checking discrepancy between the number of elements in pattern morphing
        # e.g.: pattern -> 3 characters while s.split() has 5 elements
        # The remaining elements are illegitimate, making this case fails to follow a full match
        # if we do it in an ordered matter
        if len(pattern) != len(s):
            return False
        # Iterate through the pattern
        for i in range(len(pattern)):
            ch = pattern[i] # for readability
            # Not found in our pattern hash table
            if ch not in pattern_hashmap:
                # We need to also check if the string's word has been used yet, adhering to the problem's rules
                if s[i] not in pattern_hashmap.values():
                    pattern_hashmap[ch] = s[i]
                else: # elif s[i] in pattern_hashmap.values()
                    return False
            elif ch in pattern_hashmap and pattern_hashmap[ch] != s[i]:
                return False
        # Everything goes well, return true
        return True