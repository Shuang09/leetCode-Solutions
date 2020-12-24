# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        results = []

        def addNum(node, level):
            # root append deque
            if level == len(results):
                results.append(deque([node.val]))
            else:
                #
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node is not None:
                    addNum(next_node, level + 1)

        addNum(root, 0)

        return results


