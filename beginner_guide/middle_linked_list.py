# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
def middle_node(head):
    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow
