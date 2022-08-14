# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        level = [root]
        while level:
            nextLevel = []
            for i, n in enumerate(level):
                if i != len(level) - 1:
                    n.next = level[i + 1]
                if n.left:
                    nextLevel.append(n.left)
                    nextLevel.append(n.right)
            level = nextLevel.copy()
        return root


print(Solution().connect(Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))))
