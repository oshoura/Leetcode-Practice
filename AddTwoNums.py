# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def addTwoNumbersAcc(l1, l2, carry):
            if l1 and l2:
                sum = l1.val + l2.val + carry
                return ListNode(sum%10, addTwoNumbersAcc(l1.next, l2.next, sum//10))
            if l1 and not l2:
                sum = l1.val + carry                
                return ListNode(sum%10, addTwoNumbersAcc(l1.next, None, sum//10))
            if not l1 and not l2:
                sum = l2.val + carry
                return ListNode(sum%10, addTwoNumbersAcc(None, l2.next, sum//10))
            if not l1 and not l2:
                return None
        return addTwoNumbersAcc(l1,l2,0)

