# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l: Optional[ListNode], r: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0)
        curr=head
        while l and r:
            if l.val<r.val:
                curr.next=l
                l=l.next
            else:
                curr.next=r
                r=r.next
            curr=curr.next
        while l:
            curr.next=l
            l=l.next
            curr=curr.next
        while r:
            curr.next=r
            r=r.next
            curr=curr.next
        return head.next