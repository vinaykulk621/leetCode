# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp,count=head,0
        curr,count,prev=head,0,None
        while temp!=None:
            count+=1
            temp=temp.next
        traverse=count-n
        count=0
        while curr!=None:
            if count==traverse and prev==None:
                return head.next
                break
            elif count==traverse and prev!=None:
                prev.next=curr.next
                return head
            else:
                count+=1
                prev=curr
                curr=curr.next
