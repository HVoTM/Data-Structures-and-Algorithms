# 1431. Kids with the Greatest Number of Candies
from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)

        ans = []
        for candy in candies:
            if candy + extraCandies >= max_candy:
                ans.append(True)
            else:
                ans.append(False)
        return ans