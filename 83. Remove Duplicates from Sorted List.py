# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp,prev=head,None
        while temp is not None:
            if  prev!=None and prev.val==temp.val:
                temp=temp.next
                prev.next=temp
            else:
                prev=temp
                temp=temp.next
        return head
