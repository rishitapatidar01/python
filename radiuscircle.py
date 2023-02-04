class circle:
	def __init__(self):
		self.radius=int(input("enter the radius:"))
	def area(self):
		return 3.14*self.radius*self.radius
	def circumference(self):
		return 3.14*2*self.radius
def dwrite(var1,var2,var3):
	file=open("detail.txt","a")
	datarow="{},{},{}\n".format(var1,var2,var3)
	file.write(datarow)
	file.close()
	print("write operation done succcessfully")

c1=circle()
area1=c1.area()
circumference1=c1.circumference()
radius1=c1.radius
print("radius:{} cm".format(radius1))
print("area:{} sq cm".format(area1))
print("circumference:{} cm".format(circumference1))

var1="radius:{} cm".format(radius1)
var2="area:{} sq cm".format(area1)
var3="circumference:{} cm".format(circumference1)
dwrite(var1,var2,var3)