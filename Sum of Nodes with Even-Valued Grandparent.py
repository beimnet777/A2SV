# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def helper(node,parent,gp):
            if not node:
                return 0
            else:
                left=helper(node.left,node.val%2==0,parent)
                right=helper(node.right,node.val%2==0,parent)
                val=node.val if gp else 0
                return left+right+val
        return helper(root,False,False)    Sum of Nodes with Even-Valued Grandparent
