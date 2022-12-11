# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 == None or l2 == None:
            return l1
        
        start_val = l1.val + l2.val

        if start_val < 10:
            ansNode = ListNode(start_val)
            ansNode.next = self.addTwoNumbers(l1.next, l2.next)
            return ansNode
        
        else:
            remainder = l1.val + l2.val - 10
            ansNode = ListNode(remainder)
            ansNode.next = self.addTwoNumbers(listNode(1), self.addTwoNumbers(l1.next, l2.next))
            return ansNode