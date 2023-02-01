def typecheck(x):
	num_chr=["0","1","2","3","4","5","6","7","8","9"]
	num_count=0
	float_count=0
	other_count=0

print("what you want to do")
print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for division")
print("press 4 for multiplication")


choice=input("enter yoour choice")

num1=input("enter the num1:")
num2=input("enter the num2:")
for i in num1:
	if i in num_chr:
		num_count+=1
	elif i==".":
		dot_count+=1
	else:
		other_count+=1
		
num3=num1+num2
num4=num1-num2
num5=num1/num2
num6=num1*num2

if choice=="1":
	print(num3)
elif choice=="2":
	print(num4)
elif choice=="3":
	print(num5)
elif choice=="4":
	print(num6)
else:
	print("invalid choice")
