# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def maxAncestorAcc(maxVal, minVal, maxDifference, node):
            if not node:
                return maxDifference

            thisDiff = max(abs(node.val - maxVal), abs(node.val - minVal))
            # return the max of the left and right
            return max(
                maxAncestorAcc(
                    max(maxVal, node.val),
                    min(minVal, node.val),
                    max(thisDiff, maxDifference),
                    node.left,
                ),
                maxAncestorAcc(
                    max(maxVal, node.val),
                    min(minVal, node.val),
                    max(thisDiff, maxDifference),
                    node.right,
                ),
            )

        return max(
            maxAncestorAcc(root.val, root.val, 0, root.left),
            maxAncestorAcc(root.val, root.val, 0, root.right),
        )


print(
    Solution().maxAncestorDiff(
        TreeNode(
            8,
            TreeNode(3, TreeNode(10), TreeNode(14)),
            TreeNode(1, TreeNode(6), TreeNode(13)),
        )
    )
)
print()
