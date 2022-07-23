class RecentCounter:

    def __init__(self):
        self.record=deque()
        

    def ping(self, t: int) -> int:
        while self.record and  t-self.record[0]>3000:
            self.record.popleft()
        self.record.append(t)
        return len(self.record)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
