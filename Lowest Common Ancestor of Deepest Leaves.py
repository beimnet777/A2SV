# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans=[None,0]
        
        def helper(node,depth):
            if not node:
                return depth-1
            else:
                x=helper(node.left,depth+1)
                y=helper(node.right,depth+1)
                if x==y and ans[1]<=x:
                    ans[0]=node
                    ans[1]=x
                return x if x>y else y
        helper(root,0)
        return ans[0]                    
