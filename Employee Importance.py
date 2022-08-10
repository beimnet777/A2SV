"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        x=dict()
        for j,i in enumerate(employees):
            x[i.id]=i
        def helper(employee):
            if not employee:
                return 0
            else:
                tot=0
                for i in employee.subordinates:
                    tot+=helper(x[i])
                return tot+employee.importance
        return helper(x[id])
