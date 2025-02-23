# LEETCODE 1456. Maximum number of Vowels in a Substring of Given Length
# Concepts: Sliding Window, Fixed sliding window
# len(s) - k + 1

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        "https://www.youtube.com/watch?v=kEfPSzgL-Ss&ab_channel=NeetCodeIO"
        # Initialize the set of vowels to check
        vowels = {'a', 'e', 'i', 'o', 'u'}  

        # Fixed sliding window algorithm
        # We initialize two pointers left and right to count the number of vowels 
        l, count, res = 0, 0, 0

        for r in range(len(s)): # right pointer is initialize as the running iterable element in the loop

            count += 1 if s[r] in vowels else 0
            
            # this important condition is to shift the window by one element to the right
            # if the index of the right - left + 1 is larger than given k
            if r - l + 1 > k:
                # reduce the count if the left pointer's character is not a vowel
                count -= 1 if s[l] in vowels else 0
                # shift the left pointer by 1
                l += 1 # we need to check the character at the previous left poitner before shifting up by 1
            res = max(res, count)
        return res
        # Time Complexity O(N), Space complexity O(1)

    def InferiorSolution(self, s: str, k: int) -> int:        
        # Not an optimized solution: O(N*K), N: number of characters/elements in the string array 
        # with K numbers of element to be in a substring, for every iteration, the program takes time to search
        # the k number of elements

        # We need to solve it in a fixed sliding window algorithm
        # initialize a set of vowels
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # initialie the max number of vowels encountered, or the answer we will return
        max_vowel = 0

        for i in range(len(s) + 1 - k):
            substr =  s[i : i + k]
            count = 0
            for ch in substr:
                if ch in vowels:
                    count += 1
            max_vowel = max(count, max_vowel)


        return max_vowel
