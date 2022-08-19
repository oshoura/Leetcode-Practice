# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from queue import PriorityQueue
class Solution:
    
    def mergeKLists(self, lists):
        heap = PriorityQueue()

        head = ListNode()
        cur_node=head

        for node in lists:
            if node:
                heap.put((node.val, node))

        while not heap.empty():
            val, node = heap.get()
            cur_node.next = ListNode(val)
            cur_node = cur_node.next
            node = node.next
            if node:
                heap.put((node.val, node))
        return head.next
            

#silly error with priority queue
#when the priorities are the same for two items in the heap,
#it tries to compare the second item in the tuple, the actual object
ans = Solution().mergeKLists([ListNode(1, ListNode(4,ListNode(5,None))), 
                             ListNode(1,ListNode(3,ListNode(4, None))), 
                            ListNode(2,ListNode(6 ,None))])

while ans is not None:
    print(ans.val)
    ans = ans.next