class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-float('inf'))
        prev=dummy
        while head:
            if prev.val>head.val:
                prev=dummy
            while prev.next and prev.next.val<head.val:
                prev=prev.next
            tmp=head.next
            head.next=prev.next
            prev.next=head
            head=tmp
        return dummy.next