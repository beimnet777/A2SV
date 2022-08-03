class Solution:

    def heapify(self,arr, n, i):
        big=i
        left=2*i+1
        right=2*i+2
        if left<n and arr[left]>arr[big]:
            big=left
        if right <n and arr[right]>arr[big]:
            big=right
        if big != i:
            arr[i],arr[big]=arr[big],arr[i]
            self.heapify(arr,n,big)
    
    
    def buildHeap(self,arr,n):
        pass
    
    def HeapSort(self, arr, n):
        for i in range(len(arr)//2 - 1, -1, -1):
            self.heapify(arr, len(arr), i)
        for i in range(len(arr)-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.heapify(arr, i, 0)
