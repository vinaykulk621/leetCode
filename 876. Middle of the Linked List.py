# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp,count=head,0
        while temp!=None:
            count+=1
            temp=temp.next
        n=count//2
        for _ in range(n):
            head=head.next
        return head
