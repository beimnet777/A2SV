def countingValleys(steps, path):
    count=0
    valley=0
    for  i in path :
        if i=="U":
            count+=1
            if count==0:
                valley+=1
        else:
            count-=1
    return valley
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
