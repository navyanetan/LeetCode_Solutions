# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        tail = ListNode()
        head = tail
        sortedList=[]
        for i in lists:
            while i is not None:
                sortedList.append(i.val)
                i=i.next
        sortedList.sort()
        for number in sortedList:
            tail.next=ListNode(number,None)
            tail=tail.next
        return head.next
            
                