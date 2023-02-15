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
		print("department name:",department_name)

	def dwrite(self):
		f=open("employee.txt",a)
		data=self.employee_id+","+self.name+","+self.contact+","+self.address+"\n"
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
			if self.dept==x[len(x)-1]:
				valid_row.append(i)

		

