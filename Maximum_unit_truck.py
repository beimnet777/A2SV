class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        def key1(elem):
            return elem[1]
        boxTypes.sort(key=key1,reverse=True)
        box=0
        ans=0
        for i in boxTypes:
            box+=i[0]
            if truckSize<box:
                j=i[0]-(box-truckSize)
                ans+=j*i[1]
                return ans
            else:
                ans+=i[0]*i[1]
        return ans        
