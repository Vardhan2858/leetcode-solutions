# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s=ListNode()
        curr=s
        while list1 is not None and list2 is not None:
            if list1.val<list2.val:
                curr.next=list1
                list1=list1.next 
                curr=curr.next
            else:
                curr.next=list2
                curr=curr.next
                list2=list2.next 
        while list1 is not None:
            curr.next=list1
            curr=curr.next
            list1=list1.next
        while list2 is not None:
            curr.next=list2
            curr=curr.next
            list2=list2.next
        return s.next
