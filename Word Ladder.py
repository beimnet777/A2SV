from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        x=defaultdict(list)
        for i in wordList:
            for j in range(len(i)):
                pattern=i[:j]+"*"+i[j+1:]
                x[pattern].append(i)
        def find(word):
            ans=[]
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                for i in x[pattern]:
                    ans.append(i)
            return ans
        q=deque([(beginWord,1)])
        visited=set()
        while q:
            cur =q.popleft()
            if cur not in visited:
                visited.add(cur[0])
                if cur[0]==endWord:
                    return cur[1]
                else:
                    for i in find(cur[0]):
                        if i not in visited:
                            q.append((i,cur[1]+1)) 
        return 0
