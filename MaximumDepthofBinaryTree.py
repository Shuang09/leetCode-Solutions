# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Given a binary tree, find its maximum depth.
#The maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

