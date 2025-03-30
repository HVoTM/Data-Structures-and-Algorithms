# LEETCODE 1207. Unique Number of Occurences
# Topics: Hash Table, Array

from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Using collections.Counter to turn this array into a hash table of each unique element's frequencies
        valueOccurences = Counter(arr)
        # print(valueOccurences.values())

        # By comparing between the length of
        # 1. Typecast the values (which are retrieved as a list of values by using values() on the dictionary)
        # 2. And the length of array storing the values of frequencies
        # We can identify if there are elements having the same number of frequencies
        return len(set(valueOccurences.values())) == len(valueOccurences)        
        
    def uniqueOccurrences_longer(self, arr: List[int]) -> bool:
        "My previous submission"
        # Basically this can be using collections.Counter
        count = {}
        for i in arr:
            if i not in count:
                count[i] = 0
            else:
                count[i] += 1
        # getting the set of unique values in the hash map
        unique_values = set(count.values())

        # compare the length of the dictionary and the set
        # that way, if there is one or more pair of same number of occurences
        # the number of unique values is going to be lower than the number of elements in a hashmap
        if len(unique_values) == len(count):
            return True
        return False
        
        