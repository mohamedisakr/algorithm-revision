# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = 2 * res + head.val
            head = head.next
        return res

    # def build_number(self, head: ListNode) -> str:
    #     current = head
    #     num_str = ''
    #     while current:
    #         num_str += str(current.val)
    #     return num_str
