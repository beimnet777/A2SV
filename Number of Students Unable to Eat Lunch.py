class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student=deque(students)
        sandwiches=sandwiches[::-1]
        print(sandwiches)
        x={1:0,0:0}
        for i in student:
            x[i]+=1
        while True: 
            if len(sandwiches)==0 or  x[1]==0 and  sandwiches[-1] ==1 or x[0]==0 and  sandwiches[-1] ==0:
                break
            else:
                if student[0]==sandwiches[-1]:
                    if student.popleft()==1:
                        x[1]-=1
                    else:
                        x[0]-=1
                    sandwiches.pop()
                else:
                    student.append(student.popleft())
        return x[1]+x[0]
