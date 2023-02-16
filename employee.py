class employee:
	def __init__(self):
		self.name=input("name of employee:")
		self.employe_id=input("employe id:")
		self.contact=input("contact no:")
		self.address=input("address of employe:")
		self.department_name=input("department name:")

	def show_detail(self):
		print("name:",self.name)
		print("employe_id:",self.employe_id	)
		print("contact:",self.contact)
		print("address:",self.address)
		print("department name:",self.department_name)

	def dwrite(self):
		f=open("employee.txt","a")
		data=self.name+","+self.employe_id+","+self.contact+","+self.address+","+self.department_name+"\n"
		f.write(data)
		print("data access successfully")

class manager(employee):
	#employee().__init__()

	def dept_employee_detail(self):

		f=open("employee.txt","r")
		data=f.read()
		data_row=data.split("\n")
		data_row.pop()
		valid_row=[]
		for i in data_row:
			x=i.split(",")
			if self.department_name==x[len(x)-1]:
				valid_row.append(i)

class owner(manager,employee):
	def show_all(self):
		f=open("employee.txt","r")
		data=f.read()
		data_row=data.split("\n")
		data_row.pop()
		for i in data_row:
			x=i.split(",")
			print("employe name:",x[0])
			print("employee id:",x[1])
			print("contact:",x[2])
			print("address:",x[3])
			print("department:",x[4])

	print("----------")	

s1=employee()
s2=manager()
s3=owner()
s1.dwrite()
s2.dwrite()
s3.dwrite()
s1.show_detail()
s2.show_detail()
s2.dept_employee_detail()
s3.show_detail()
s3.dept_employee_detail()
s3.show_all()		

