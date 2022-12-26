user_string=input("enter the string")
x=" "
for i in user_string:
		if i==".":
			print(x)

			x=" "
		else:
			x=x+i
print(x)