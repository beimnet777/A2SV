class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        i=0
        h_index=0
        length=len(citations)
        while i<length:
            if citations[i]>=length-i:
                return length-i
            i+=1
        return h_index
