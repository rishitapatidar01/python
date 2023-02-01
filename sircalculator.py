
import typecheck as t
def calculator():
	print("Welcome to My Calculator")
	var1 = int(input("Enter Value1 : "))
	var2 = int(input("Enter Value2 : "))
	oper_choice = input("Please in Operation of your choice :\n1 for Addition \n2 for Substraction \n3 for Multiplication \n4 for Division\n5 for modulus\n6 for root Please Enter Your Choice :  ")
	if oper_choice == "1" : 
		result = var1 + var2
		print(result)
		type1=t.typecheck(result)
		print(type1) 
	elif oper_choice == "2":
		result = var1 - var2
		print(result)
		type2=t.typecheck(result) 
		print(type2) 
	elif oper_choice == "3":
		result = var1 * var2 
		print(result)
		type3=t.typecheck(result)
		print(type3)  
	elif oper_choice == "4":
		result = var1/var2
		print(result)
		type4=t.typecheck(result) 
		print(type4) 
	elif oper_choice=="5":
		result=var1%var2
		print(result)
		type5=t.typecheck(result)
		print(type5)  
	elif oper_choice=="6":
		result=var1^var2
		print(result)
		type6=t.typecheck(result)
		print(type6)  
	else : 
		print("invalid operation given")
	calculator()

def next_move():
	next_choice = input("Enter y to continue or n to close : ")
	if next_choice == "y":
		return True
	elif next_choice == "n":
		return False
	else : 
		print("Invalid Input")
		next_move()

while True : 
	calculator()
	var3 = next_move()
	if var3 == True :
		calculator()

	elif var3 == False: 
		print("Thanks for using my calculator")
		break
