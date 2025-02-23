# 1657. Determine if Two Strings are Close
# https://algo.monster/liteproblems/1657

from collections import Counter # Counter is a python built-in data type similar to hashmap, or a subtype of dict
# it is mainly used to contain the keys and values being set as the counter for the frequency of that specified value
# other Python's datatype: https://docs.python.org/3/library/collections.html#

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Operation 1: allows us to reorder characters in any fashion
        # rendering the relative order or characters inconsequential
        # Operation 2: allows us to transform characters into each other, given that both
        # characters exist in both strings
        
        # count the frequency of each character in both words
        counter1, counter2 = Counter(word1), Counter(word2)

        # Operation 2 check
        # If the sets of unique characters (keys of the counters) are the same and 
        # the sorted lists of character counts (values of the counters) are the same,
        # then the strings are close
        sorted_word1 = sorted(counter1.values()) # retrieve the list of values to be sorted
        sorted_word2 = sorted(counter2.values())

        # Operation 1 check 
        # Compare the sets of keys (unique characters) from both words to check if 
        # both words contain exactly the same characters
        keys_match = set(counter1.keys()) == set(counter2.keys())
        # Check both conditions: character counts must match when sorted and 
        # the sets of characters present in both words must be the same
        return sorted_word1 == sorted_word2 and keys_match