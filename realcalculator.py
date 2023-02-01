import typecheck as t
def choice():
	print("what you want to do")
	print("press 1 for addition")
	print("press 2 for subtraction")
	print("press 3 for division")
	print("press 4 for multiplication")
	print("press 5 for mode")


	choice=input("enter yoour choice")
	return()

def calculator(x,y):
	
	if choice=="1":
		r=x+y
		print("additioin of numbers are:",r)
	elif choice=="2":
		r=x-y
		print("subtraction of numbers are:",r)
	elif choice=="3":
		r=x/y
		print("division of numbers are:",r)
	elif choice=="4":
		r=x*y
		print("multiplication of numbers are:",r)
	elif choice=="5":
		r=x%y
		print("modulus of numbers are",r)
		
	else:
		print("invalid choice")
		return()
x=int(input("enter the num1:"))
y=int(input("enter the num2:"))
var1=choice()
print(var1)
print(calculator(x,y))
t.typecheck(x,y)
