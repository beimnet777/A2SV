class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q=deque([start])
        visited=set()
        visited.add(start)
        while q:
            cur=q.popleft()
            if arr[cur]==0:
                return True
            else:
                if cur-arr[cur]>=0 and cur-arr[cur] not in visited:
                    q.append(cur-arr[cur])
                    visited.add(cur-arr[cur])
                if cur+arr[cur]<len(arr) and cur+arr[cur] not in visited:
                    q.append(cur+arr[cur])
                    visited.add(cur+arr[cur])
        return  
