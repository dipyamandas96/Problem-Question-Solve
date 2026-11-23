# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow=fast=head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if not fast.next:
            return slow
        return slow.next