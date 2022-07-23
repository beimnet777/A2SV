class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        x=[(i,j) for j,i in enumerate(tasks)]
        x.sort(key=lambda x:x[0][0])
        availables=[]
        heapq.heapify(availables)
        ans=[]
        time=x[0][0][0]
        index=0
        while True:
            while index<len(tasks) and time>=x[index][0][0]:
                heapq.heappush(availables,(x[index][0][1],x[index][1]))
                index+=1
            if len(availables)==0 and index<len(tasks):
                time=x[index][0][0]
                continue
            cur=heapq.heappop(availables)
            ans.append(cur[1])
            time+=cur[0]
            if len(ans)==len(tasks):
                return ans
