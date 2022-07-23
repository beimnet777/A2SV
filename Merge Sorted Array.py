class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr=[]
        l,r=0,0
        for i in range(len(nums1)-m):
            nums1.pop()
        if len(nums1)==0:
            nums1.extend(nums2)
            return
        while r<len(nums2) and l<len(nums1):
            if nums1[l]<nums2[r]:
                l+=1
            else:
                nums1.insert(l,nums2[r])
                r+=1
        while r<len(nums2):
            nums1.append(nums2[r])
            r+=1
                
        
        
#         while l<len(nums1)and  nums1[l]!=0:
#             arr.append(nums1[l])
#             l+=1
#         while r<len(nums2):
#             arr.append(nums2[r])
#             r+=1
#         print(arr)
        nums1=arr
