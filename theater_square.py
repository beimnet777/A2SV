def theatreSquare():
	nums=input().split()
	n=int(nums[0])
	m=int(nums[1])
	a=int(nums[2])
	width=n/a if n%a==0 else n//a+1
	height=m/a if m%a==0 else m//a+1
	return int(width*height)
print(theatreSquare())
