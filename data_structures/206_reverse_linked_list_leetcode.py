from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1
        previous = None
        current = head
        following = head

        # Step 2
        while current is not None:
            following = following.next
            current.next = previous
            previous = current
            current = following

        return previous
