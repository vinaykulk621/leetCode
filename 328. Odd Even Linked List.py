# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt,temp,asli,odd,even=1,head,head,[],[]
        while temp!=None:
            if cnt%2!=0:
                odd.append(temp.val)
            else:
                even.append(temp.val)
            temp=temp.next
            cnt+=1
        while odd:
            asli.val=odd[0]
            asli=asli.next
            odd.pop(0)
        while even:
            asli.val=even[0]
            asli=asli.next
            even.pop(0)
        return head
