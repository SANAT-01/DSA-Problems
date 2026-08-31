# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical=[]
        cnt=0
        mini=float('inf')
        while head and head.next and head.next.next:
            if head.val<head.next.val>head.next.next.val or head.val>head.next.val<head.next.next.val:
                if critical:
                    mini=min(mini,cnt+1-critical[-1])
                critical.append(cnt+1)
            cnt+=1
            head=head.next
        if len(critical)<2 or not critical:
            return [-1,-1]
        return [mini,critical[-1]-critical[0]]