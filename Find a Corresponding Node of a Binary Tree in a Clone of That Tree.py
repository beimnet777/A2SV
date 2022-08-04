# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        x=[cloned]
        visited=set()
        while x:
            cur =x.pop()
            if cur.val==target.val:
                return cur
            if cur.left:
                x.append(cur.left)
            if cur.right:
                x.append(cur.right)
