class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ctr=0
        while ctr <len(arr) and x > arr[ctr]:
            ctr+=1
        if ctr==len(arr):
            target=ctr-1
        elif ctr==0 :
            target=ctr
        else:
            target= ctr if arr[ctr]-x<x-arr[ctr-1] else ctr-1
        heap=[arr[target]]
        heapq.heapify(heap)
        l=target-1 if target >0 else -1
        r=target+1 if target<len(arr)-1 else len(arr)
        for i in range (k-1):
            if l>-1 and r<len(arr):
                if x-arr[l] <= arr[r]-x:
                    heapq.heappush(heap,arr[l])
                    l-=1
                else:
                    heapq.heappush(heap,arr[r])
                    r+=1
            elif r<len(arr):
                heapq.heappush(heap,arr[r])
                r+=1
            else:
                heapq.heappush(heap,arr[l])
                l-=1
        ans=[]
        while len(heap)>0:
            ans.append(heapq.heappop(heap))
        return ans
