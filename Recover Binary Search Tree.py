# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nums=[]
        def helper(node):
            if not node:
                return
            else:
                helper(node.left)
                nums.append((node.val,node))
                helper(node.right)
        helper(root)
        ptr=0
        target=[-1,None]
        while ptr<len(nums)-1:
            if nums[ptr+1][0]<nums[ptr][0]:
                target[0],target[1]=nums[ptr+1][0],nums[ptr+1][1]
            ptr+=1
        for i,j in nums:
            if i>target[0]:
                # print(i,target[0])
                j.val,target[1].val=target[1].val,j.val
                break
