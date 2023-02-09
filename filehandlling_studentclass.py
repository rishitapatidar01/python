roll_no=0
class student:
	def __init__(self):
		self.name=input("enter student's name:")
		self.fathersname=input("enter students fathers name:")
		self.age=input("enter age:")
		self.year=input("enter year:")
		self.course=input("enter course:")
		self.contact=input("enter contact:")

def dwrite(var1,var2,var3,var4,var5,var6):
	file=open("studentdata.txt","a")
	datarow="{},{},{},{},{},{}\n".format(var1,var2,var3,var4,var5,var6,)
	file.write(datarow)
	file.close()
	print("data fetch successfully")

s=student()
name1=s.name
fathersname1=s.fathersname
age1=s.age
year1=s.year
course1=s.course
contact1=s.contact
print("name:{}".format(name1))
print("fathersname:{}".format(fathersname1))
print("age:{}".format(age1))
print("year:{}".format(year1))
print("course:{}".format(course1))
print("contact:{}".format(contact1))


var1=print("name:{}".format(name1))
var2=print("fathersname:{}".format(fathersname1))
var3=print("age:{}".format(age1))
var4=print("year:{}".format(year1))
var5=print("course:{}".format(course1))
var6=print("contact:{}".format(contact1))
dwrite(var1,var2,var3,var4,var5,var6)







	