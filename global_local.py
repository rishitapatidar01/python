def myfunction():
	global i
	"""x=input("enter value")
	y=input("enter value")
	z=x+y
	print(z)
	print(i)"""
	i=["i am inside"]
	print(id(i))

i=["i am fine"]
print(id(i))
print(i)

myfunction()
print(i)
	
#i="i am outside" #this is a global variable
#myfunction()
#print(z) #because z is a local variable so it can't accessed outside myfunction
