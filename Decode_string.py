class Solution:
    def decodeString(self, s: str) -> str:
        i=0
        string=s
        char_stack=[]
        while i<len(string):
            if string[i]=="[":
                char_stack.append(i)
            elif string[i]=="]":
                index=char_stack.pop()
                j=index-1
                while j>=0:
                    if not string[j].isdigit():
                        break
                    else:
                        j-=1
                if j+1<index-1:
                    num=int(string[j+1:index])
                else:
                    num=int(string[index-1])
                sub_str=string[index+1:i]
                sub_str=sub_str*num
                diff=len(sub_str)-((i)-(j))
                string=string.replace(string[j+1:i+1],sub_str)
                i+=diff
                continue
            else:
                pass
            i+=1
        return string
