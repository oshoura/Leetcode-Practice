# Definition for singly-linked list.
from queue import Empty


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head:ListNode, k: int) -> ListNode:
        curNode = head
        head = ListNode()
        toAdd = head
        S = []
        while curNode is not None:
            S.append(curNode)
            curNode = curNode.next
            if len(S) == k:
                while S:
                    toAdd.next = S.pop()
                    toAdd = toAdd.next
                toAdd.next = None
                
        while S:
            toAdd.next = S.pop(0)
            toAdd = toAdd.next
        toAdd.next = None
        return head.next

        
        
print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 3))