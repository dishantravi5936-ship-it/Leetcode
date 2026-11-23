# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)        # 1. Visit left subtree
            result.append(node.val) # 2. Visit current node (root)
            dfs(node.right)       # 3. Visit right subtree

        dfs(root)
        return result
        