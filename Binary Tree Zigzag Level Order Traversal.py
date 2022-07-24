# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        def helper(node,level):
            if node==None:
                return
            else:
                if len(ans)>level:
                    ans[level].append(node.val)
                else:
                    ans.append([node.val])

                helper(node.left,level+1)
                helper(node.right,level+1)
        helper(root,0)
        for j,i in enumerate(ans):
            if j%2==1:
                ans[j]=reversed(ans[j])
        return ans
