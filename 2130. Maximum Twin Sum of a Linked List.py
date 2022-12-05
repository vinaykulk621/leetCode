# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp,cnt=head,0
        prev,curr=None,head
        while temp!=None:
            cnt+=1
            temp=temp.next
        n=cnt//2
        if n!=0:
            cnt=0
            while cnt<n:
                prev=curr
                curr=curr.next
                cnt+=1
            prev.next=curr.next
            return head
        return None
