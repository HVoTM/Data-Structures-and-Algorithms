# LEETCODE 2300. Successful Pairs of Spells and Potions
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        successful_pairs = []
        potions.sort()
        # Perform a binary search to check
        for spell in spells:
            # Find the weakest potion (furthest to the left) that works
            idx = len(potions) # initialize to length of the array incase there is no potion
            # that works with the spell, so we append them by len(potions) - len(potions) = 0
            l, r = 0, len(potions) -1
            while l <= r:
                m = (l + r) // 2 # middle index 
                # Check for the successful pair of potion-spell
                if spell * potions[m] >= success:
                    r = m - 1
                    idx = m
                else:
                    l = m + 1
            successful_pairs.append(len(potions) - idx)
        return successful_pairs