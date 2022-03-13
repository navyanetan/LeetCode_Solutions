# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        traversal =[]
        output = 0
        if not root:
            return
        def inorder(root):
            if root.left:
                inorder(root.left)
            traversal.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        for i in traversal:
            if i >= low and i <= high:
                output+=i
        return output
            