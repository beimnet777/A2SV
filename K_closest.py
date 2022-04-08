class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=self.distance)
        return points[:k]
    def distance(self,pairs):
        dist=pairs[0]* pairs[0] + pairs[1]*pairs[1]
        return dist
