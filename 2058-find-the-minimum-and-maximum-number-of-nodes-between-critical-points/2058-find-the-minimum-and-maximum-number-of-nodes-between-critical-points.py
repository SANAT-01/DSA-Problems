# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical=[]
        cnt=0
        while head and head.next and head.next.next:
            if head.val<head.next.val>head.next.next.val:
                critical.append(cnt+1)
            elif head.val>head.next.val<head.next.next.val:
                critical.append(cnt+1)
            cnt+=1
            head=head.next
        print(critical,cnt)
        if len(critical)<2 or not critical:
            return [-1,-1]
        mini=cnt
        for i in range(len(critical)-1):
            mini=min(critical[i+1]-critical[i],mini)
        return [mini,critical[-1]-critical[0]]