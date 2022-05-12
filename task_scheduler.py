class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        task=dict(Counter(tasks))
        freq,max_val=1,0
        for i in task.values():
            if i>max_val:
                max_val=i
                freq=1
            elif i==max_val:
                freq+=1
        ans =(n+1)*(max_val-1)+freq   
        print(freq)
        print(n+1)
        print(max_val)
        
        return max(ans,len(tasks))
