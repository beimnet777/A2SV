# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans=[0]
        def helper(node1,node2):
            if node1==None and node2==None:
                return
            elif node1==None or node2==None:
                ans[0]=-1
                return
            else:
                if node1.val==node2.val:
                    helper(node1.right,node2.left)
                    helper(node1.left,node2.right)
                else:
                    ans[0]=-1
                    return
        helper(root.right,root.left)
        return True if ans[0]==0 else None
