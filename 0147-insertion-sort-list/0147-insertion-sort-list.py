# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        i=1
        while i<len(arr):
            j=i
            val=arr[i]
            while j-1>=0 and arr[j-1]>arr[j]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
                j-=1
            i+=1
        head=ListNode(0)
        curr=head
        for i in arr:
            curr.next=ListNode(i)
            curr=curr.next
        return head.next