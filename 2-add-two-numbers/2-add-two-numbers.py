# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        string1=""
        string2=""
        while l1 is not None:
            string1+= str(l1.val)
            l1=l1.next
        while l2 is not None:
            string2+= str(l2.val)
            l2=l2.next
        string1=string1[::-1]
        string2=string2[::-1]
        sum = str(int(string1)+int(string2))
        sum = sum[::-1]
        output= ListNode()
        head=output
        for letters in sum:
            output.next= ListNode(letters,None)
            output=output.next
        return head.next