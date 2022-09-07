# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans=[]
        def helper(node):
            if not node:
                ans.append("()")
            else:
                ans.append(str(node.val))
                if node.left and node.right:
                    ans.append("(")
                    helper(node.left)
                    ans.append(")")
                    ans.append("(")
                    helper(node.right)
                    ans.append(")")
                elif node.left:
                    ans.append("(")
                    helper(node.left)
                    ans.append(")")
                elif node.right:
                    helper(node.left)
                    ans.append("(")
                    helper(node.right)
                    ans.append(")")          
        helper(root)
        return "".join(ans)
