# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp,tra=head,[]
        while temp!=None:
            tra.append(temp.val)
            temp=temp.next
        tra.sort()
        i,temp=0,head
        while temp!=None:
            temp.val=tra[i]
            temp=temp.next
            i+=1
        return head
