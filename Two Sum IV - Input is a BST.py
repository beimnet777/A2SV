# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        x=dict()
        def helper(node):
            if node==None:
                return
            else:
                x[node.val]=x.get(node.val,0)+1
                helper(node.right)
                helper(node.left)
        helper(root)
        q=deque([root])
        while q:
            cur=q.popleft()
            target=k-cur.val
            if target !=cur.val and target in x:
                return True
            elif target ==cur.val and x[target]>1:
                return True
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return
