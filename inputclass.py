class student:
	def __init__(self):
		self.name=input("enter name:")
		self.course=input("enter course:")
		self.subject=input("enter subject:")
	def show(self):
		print("name:",self.name)
		print("course:",self.course)
		
		print("subject:",self.subject)
s1=student()
s1.show()
s2=student()
s2.show()
