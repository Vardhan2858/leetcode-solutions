# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cnt=0
        curr=head
        while curr is not None:
            cnt+=1
            curr=curr.next
        pos=cnt//2
        curr=head
        for i in range(pos):
            curr=curr.next 
        s=curr
        return s

        