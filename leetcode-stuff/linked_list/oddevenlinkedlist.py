from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case, list is empty
        if head is None:
            return None
        # given the condition, first node is considered odd -> initial index = 1
        # initalize the odd pointer
        odd = head
        even = head.next # since we know the next linked list is 2, which is even
        # reference to the first node of this even listnode so we can append it to the odd
        # after all execution for traversing the odd and even indexed nodes are finished
        temp = even

        # Traverse the list, rearrange the nodes
        # Explanation of condition
        # even: we have reached the end of the linked list with an even node
        # even.next: we have reached the end of the linked list with an odd node
        while even and even.next:
            # make the next odd link to the node after the next (which is also odd indexed)
            # which is the next node of even
            odd.next = even.next
            # move the odd pointer to its new next node
            odd = odd.next

            # Connect the next of even to next of the new odd node
            even.next = odd.next
            # move the even pointer to the new next
            even = even.next
        
        # After all odd indexed nodes have been linked, append the even indexed nodes
        odd.next = temp

        return head
    """
    Time Complexity:
    The while loop continues until it has traversed all the nodes of the linked list because it stops only when b is None (meaning the end of the list) or b.next is None (meaning the last node is reached).
    Inside the loop, operations have a constant time complexity (O(1)), which includes assigning next pointers for a and b.
    Since each node is visited once during the traversal, the total time complexity is based on the number of nodes in the linked list (n). Therefore, the time complexity is O(n) where n is the number of nodes in the linked list.
    Space Complexity:
    The algorithm only uses a constant amount of extra space for pointers a, b, and c irrespective of the size of the input linked list.
    No additional data structures are used that grow with the input size.
    Therefore, the space complexity is O(1) constant space.
    """
    """
    Comparing it to my prior solution, the approach here used just 2 pointers and adhere to pointing towards the next node of each other, while mine was using a whole other linkedlist, which violates the constraint of O(1) space complexity
    """