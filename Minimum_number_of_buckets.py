class Solution:
    def minimumBuckets(self, street: str) -> int:
        ptr=0
        buckets=0
        indexes=set()
        while ptr<len(street):
            if street[ptr]=="H":
                if ptr-1 in indexes:
                    pass
                elif ptr<len(street)-1 and  street[ptr+1]=='.':
                    indexes.add(ptr+1)
                    buckets+=1
                elif ptr>0 and street[ptr-1]=='.':
                    indexes.add(ptr-1)
                    buckets+=1
                else:
                    return -1                    
            ptr+=1
        return buckets
