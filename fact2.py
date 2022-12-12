i=int(input("enter the fact"))
fact=1
if i==0 or i==1:
	print("factorial of {} is {}". format(i,fact))
else:
	for j in range(i,0,-1):
		fact=fact*j
		print(fact*i)
	print("factorial of{} is {}".format(i,fact))