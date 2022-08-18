# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        prev=0
        ans=[]
        q=deque([(root,0)])
        tot,ctr=0,0
        while q:
            cur,level=q.popleft()
            if level==prev:
                tot+=cur.val
                ctr+=1
            else:
                ans.append(tot/ctr)
                ctr=1
                tot=cur.val
                prev=level
            if cur.left:
                q.append((cur.left,level+1))
            if cur.right:
                q.append((cur.right,level+1))
        ans.append(tot/ctr)
        return ans
