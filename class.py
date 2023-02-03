class student:
	def __init__(self,name,course,subject):
		self.name=name
		self.course=course
		self.subject=subject
	def show(self):
		print("name:",self.name)
		print("course:",self.course)
		
		print("subject:",self.subject)
s1=student("Rishita","bca","python")
s1.show()
 