x=input("enter the string:")
y=" "
for i in x:
	if ord(i)>=97 and ord(i)<=122:
		a=ord(i)
		b=chr(a)
		y=y+b
	else:
		y=y+i
print("value before conversion =",x)
print("value after conversion =",y)
	