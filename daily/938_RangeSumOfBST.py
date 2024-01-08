# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def recursive(actual):
            if actual == None:
                return 0
            left = recursive(actual.left)
            right = recursive(actual.right)
            if actual.val in range(low,high+1):
                return actual.val+left+right
            else:
                return left+right

        return recursive(root)