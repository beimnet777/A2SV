class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def helper(index,question,memo):
            if index>len(questions)-1:
                return 0
            if index in memo:
                return memo[index]
            solve=helper(index+question[index][1]+1,question,memo)+question[index][0]
            jump=helper(index+1,question,memo)
            memo[index]=max(solve,jump)
            return memo[index]
        memo=dict()
        return helper(0,questions,memo)
