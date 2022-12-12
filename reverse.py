name=input("enter your string:")
reverse=" "
for i in range(len(name)-1,-1,-1):
	reverse=reverse+name[i]
print("user given string is {}".format(name))
print("reverse string is {}".format(reverse))
