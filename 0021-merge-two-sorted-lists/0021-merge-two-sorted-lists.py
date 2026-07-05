# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l: Optional[ListNode], r: Optional[ListNode]) -> Optional[ListNode]:
        if not l or not r:
            return l if l else r
        if l.val>r.val:
            l,r=r,l
        l.next=self.mergeTwoLists(l.next,r)
        return l