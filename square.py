"""num=int(input("enter the number"))
sqaure=num*num
print("square of {} is {}".format(num,sqaure))


num=int(input("enter the number"))
n=int(input("enter the term"))
square=num**n
print(square)"""
n=int(input("enter the number"))
if n<2:
	print("not a prime no.")
else:
	for i in range(2,n):
		if(n%i==0):
			print("not a prime")
			break
		else:
			print("n is prime")




"""i=int(input("enter the fact:"))
fact=1
if i==0 or i==1:
	print("{} is factorial of {}".format(fact,i))
else:
	for j in range(1,i+1):
		fact=fact*j 
	print("{}is factorial of {}".format(fact,i))"""