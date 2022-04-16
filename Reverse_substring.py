class Solution:
    def reverseParentheses(self, s: str) -> str:
        tracker = []
        for n in s:
            if n == ")":
                reverser = []
                flag = True
                while flag:
                    popped = tracker.pop()
                    if popped != "(":
                        reverser.append(popped)
                    else:
                        flag = False
               
                tracker += reverser

            else:
                tracker.append(n)


        return "".join(tracker)
                
                    
        
