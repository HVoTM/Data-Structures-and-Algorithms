# LEETCODE 205. Isomorphic String
# Topics: String, HashMap

from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize a hashmap to store each distinctive character's replacement from s to t
        charDict = defaultdict(str)
        # Set to store the characters that s has used to map to another character in t
        takenChar = set()
        for i in range(len(s)):
            # Check if the character is not registered for mapping and current char in t is not already taken 
            if charDict[s[i]] == "" and t[i] not in takenChar:
                charDict[s[i]] = t[i]
                takenChar.add(t[i])
        
            if charDict[s[i]] != t[i]:
                return False
        return True

    def NeetCode(self, s: str, t: str) -> bool:
        mapStoT, mapTtoS = {}, {}
        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            # NOTE: We can use: for c1, c2 in zip(s, t):
            
            # Check if both characters are in the respective hashmaps and the mapped characters are different with the values
            if ((c1 in mapStoT and mapStoT[c1] != c2)
                or (c2 in mapTtoS and mapTtoS[c2] != c1)):
                return False
            
            # Add the new characters in each hashmap
            mapStoT[c1] = c2
            mapTtoS[c2] = c1
        return True
    
# Test example
s = "badc"
t = "baba"

solution = Solution()
print(solution.isIsomorphic(s, t))