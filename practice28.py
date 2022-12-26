def max_three(a,b,c):
	if a>b and a>c:
		return a
	elif b>a and b>c:
		return b
	else:
		return c
n_1=int(input("enter the first value:"))
n_2=int(input("enter the second value:"))
n_3=int(input("enter the third value:"))
result=max_three(n_1,n_2,n_3)
print("the greatest value is {}".format(result))