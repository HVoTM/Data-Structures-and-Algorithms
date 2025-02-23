# 2130. Maximum Twin Sum of a Linked List
# Definition for singly-linked list.

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # My Simple solution
        # val_
        val = []
        while head:
            val.append(head.val)
            head = head.next

        # initialize the maximum count encountered
        max = 0
        
        n = len(val)
        for i in range(int(n/2)):
            twin_sum = val[i] + val[n - 1 -i]
            if twin_sum >= max:
                max = twin_sum
        
        return max
    # Runtime 39ms - 98.88%, Memory 47.78MB - 21.23%


    def NeetCode(self, head: Optional[ListNode]) -> int:
        # https://www.youtube.com/watch?v=doj95MelfSA&ab_channel=NeetCodeIO
        # a tortoise and hare pointer?
        
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        res = 0

        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        
        return res
    # Runtime: 84ms , 40.96% , Memory: 35.17MB, 91.13%