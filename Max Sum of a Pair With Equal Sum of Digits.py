class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        x=dict()
        def digit_sum(n):
            j=list(str(n))
            return sum([int(i) for i in j])
        for i in nums:
            sumx=digit_sum(i)
            if sumx in x:
                heapq.heappush(x[sumx],-i)
            else:
                x[sumx]=[-i]
                heapq.heapify(x[sumx])
        ans=-1
        for i in x.keys():
            if len(x[i])>1:
                first=-heapq.heappop(x[i])
                second=-heapq.heappop(x[i])
                ans=max(ans,first+second)
        return ans 
