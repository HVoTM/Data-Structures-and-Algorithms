# LEETCODE 649. DOTA2 Senate

# Concepts: queue, double queue, priority and offsetting the winner's order after he wins this round

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # https://www.youtube.com/watch?v=zZA5KskfMuQ&ab_channel=NeetCodeIO
        # operation on string is more costly since it is immutable
        # we turn this into a list - O(1)
        senate = list(senate)

        # Intialize two queues (FIFO) for popleft
        D, R = deque(), deque()
        
        # Building the two queues to store the corresponding senator to their party
        # we append by adding the ordering index, meaning which senator comes first in their respective
        # order in the given senate string
        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)

        # Main simulation loop to compare
        while D and R:
            dTurn = D.popleft()
            rTurn = R.popleft()

            if rTurn < dTurn:
                # if the Radiant senator is preceding the Dire senator, which means the Radiant one
                # can vote out the Dire one
                # we do not append the popped Dire senator since it is out
                # for the winning senator, we put it back the end of the queue by append()
                # NOTE: AND we add it with an offset of the length list 'senate' as that senator
                # will have the lower order compared to the sequential senators to be compared
                R.append(dTurn + len(senate))
        
            # the other case
            else:
                D.append(rTurn + len(senate))        
        # we are returning the nonempty queue after the previous loop breaks
        return "Radiant" if R else "Dire"