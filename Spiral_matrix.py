class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,bottom,left,right=0,len(matrix)-1,0,len(matrix[0])-1
        arr=[]
        while top<=bottom and left<=right:
            if top==bottom:
                ptr=left
                while ptr<=right:
                    arr.append(matrix[top][ptr])
                    ptr+=1
                return arr
            if right==left:
                ptr=top
                while ptr<=bottom:
                    arr.append(matrix[ptr][left])
                    ptr+=1
                return arr
            ptr=left
            while ptr<=right:
                
                arr.append(matrix[top][ptr])
                ptr+=1
            ptr=top+1
            while ptr<=bottom:
                
                arr.append(matrix[ptr][right])
                ptr+=1
            ptr=right-1
            while ptr>=left:
                
                arr.append(matrix[bottom][ptr])
                ptr-=1
            ptr=bottom-1
            while ptr>top:
                print(ptr,left)
                arr.append(matrix[ptr][left])
                ptr-=1
            left+=1
            right-=1
            top+=1
            bottom-=1
        return arr     
