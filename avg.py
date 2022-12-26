choice=int(input("enter no. of term"))
sum=0
for i in range(choice):
	value=int(input("enter the value"))
	sum=sum+value
average=sum/choice
print("average=",average)