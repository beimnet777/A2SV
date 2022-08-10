"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def helper(node,depth):
            if not node or not node.children:
                return depth
            else:
                maxi=-1
                for i in node.children:
                    d=helper(i,depth+1)
                    if d>maxi:
                        maxi=d
                return maxi
        return helper(root,1) if root else 0
