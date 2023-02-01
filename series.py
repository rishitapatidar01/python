"""n=int(input("enter the term"))
var=1
print(var, end=" ")
for i in range(2, n+1):
	var=var+var
	print(var, end=" ")"""

"""n=int(input("enter the term"))
var=1
print(var, end=" ")
for i in range(2, n+1):
	var=var*2
	print(var, end=" ")"""

n=int(input("enter the no. of term"))
for i in range(1,n):
	if(i%2!=0):
		print(i)
