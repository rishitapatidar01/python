roll_no=0
class student:
	def __init__(self):
		self.name=input("enter student's name:")
		self.fathersname=input("enter students fathers name:")
		self.age=input("enter age:")
		self.year=input("enter year")
		self.course=input("enter course")
		self.contact=input("enter contact")

	def show_details(self):
		print("name:",self.name)
		print("fathersname:",self.fathersname)
		print("age:",self.age)
		print("year of joining:",self.year)
		print("course:",self.course)
		print("contact:",self.contact)

	def generate_rollno(self):
		global roll_no 
		roll_no=roll_no+1
		self.roll_no=roll_no
		print("Roll no of student:",self.roll_no)
		
print(roll_no)
s1=student()
s1.generate_rollno()
s1.show_details()
print(roll_no)


		
