class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        arr1=[]
        for i in nums:
            arr1.append(int(i))
        arr1.sort()
        print (arr1)
        j= str(arr1[-k])
        return j 
