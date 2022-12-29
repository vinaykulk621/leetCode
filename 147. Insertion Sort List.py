# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp,ans,i=head,[],0
        while temp!=None:
            ans.append(temp.val)
            temp=temp.next
        ans.sort()
        temp=head
        while temp!=None:
            temp.val=ans[i]
            i+=1
            temp=temp.next
        return head
