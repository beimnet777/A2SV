class minMaxQueue:
    def __init__(self):
        self.q=[]
        self.minQ=[]
        self.maxQ=[]
    def get_minmax(self):
        return self.minQ[0],self.maxQ[0]
    def enqueue(self,val):
        while self.minQ and self.minQ[-1]>val:
            self.minQ.pop() 
        while self.maxQ and self.maxQ[-1]<val:
            self.maxQ.pop() 
        self.maxQ.append(val)
        self.minQ.append(val)
        self.q.append(val)
    def dequeue(self):
        val=self.q.pop(0)
        if val==self.minQ[0]:
            self.minQ.pop(0) 
        if val==self.maxQ[0]:
            self.maxQ.pop(0) 
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        queue=minMaxQueue()
        i,j=0,0
        ans=0
        while j<len(nums):
            queue.enqueue(nums[j])
            small,large=queue.get_minmax()
            if abs(large-small)<=limit:
                pass  
            else:
                if ans < j-i:
                    ans=j-i
                queue.dequeue()
                i+=1
            j+=1   

        if ans < j-i:
            ans=j-i
        return ans
