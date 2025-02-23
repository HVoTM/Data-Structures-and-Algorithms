# LEETCODE 1268. Search Suggestions System
# Topic: Array, String, Binary Search, Trie, Sorting, Heap (Priority Queue)

from typing import List

class Solution:
    def brute_force(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Initialize the return variable
        ans = []
        # Sort the list in a lexicographical manner, from a to b
        # "If there are more than three products with a common prefix 
        # return the three lexicographically minimums products."
        products.sort()

        # Pass the characters in the search word
        for i in range(len(searchWord)):
            # flag for when more than 3 words are found to be matching
            j = 0
            # array to store the current suggested words for every addtional character typed into
            curr_list = []
            for product in products:
                if j >= 3:
                    continue
                # Basically just brute force matching
                if product[:i+1] == searchWord[:i+1]:
                    curr_list.append(product)
                    j += 1

            ans.append(curr_list)
        return ans

    def binarySearch_method(self, products: List[str], searchWord: str) -> List[List[str]]:
        "Another better, more efficacious approach is to use Binary Search (according to hint 2)"
        # https://www.youtube.com/watch?v=D4T2N0yAr20&ab_channel=NeetCode
        # First off, sort the given databases of products to suggest in alphabetical (lexicographical) order
        products.sort()
        # Initialize the returning array that stores the (max) top 3 suggested words
        ans = []
        # Initialize pointers 
        left, right = 0, len(products) - 1
        for i in range(len(searchWord)):
            # Check for every character in searchWord
            c = searchWord[i]
            # Maintaining the condition of left right pointers not passing each other
            # Shift the left pointer up by 1 if the length of the suggested product is in the search range (searchWord does not exceed the suggested word's range)
            # and the corresponding character in that index does not match
            # The condition stop and we keep the left pointer there
            while left <= right and (len(products[left]) <= i or products[left][i] != c):
                left += 1
            # Same thing for the right pointer, only to shift the pointer down by 1
            while left <= right and (len(products[right]) <= i or products[right][i] != c):
                right -= 1
            # Personally, I would not got this obsfucating piece of array
            # I could just declare an open array then insert it into the array
            ans.append([])
            # All the matching suggested words' indices are now identified for that typed in character hitherto
            remain = right - left + 1
            # But only add 3 of them if remain > 3
            for j in range(min(3, remain)):
                ans[-1].append(products[left + j])
        return ans
    "Time complexity is O(nlogn + n + m) where n is size of products, and m is length of searchWord."

