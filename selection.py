#User function Template for python3

class Solution: 
    def select(self, arr, i):
        x=arr[i:len(arr)]
	    num=x[0]
	    for i in x:
		    if i<num:
			    num=i
	    return num,x.index(num)
 
    
    def selectionSort(self, arr,n):
        for i in range (n):
    		z,y=self.select(arr,i)
    		num2=arr[i]
    		arr[i]=z
    		arr[y+i]=num2
	    return arr
