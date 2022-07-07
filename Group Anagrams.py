class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ma=dict()
        for i in strs:
            x="".join(sorted(i))
            if x in ma:
                ma[x].append(i)
            else:
                ma[x]=[i]
        return ma.values()
