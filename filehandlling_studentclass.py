rollno = 0
class student:
    def _init_(self):

        self.name = input("enter students name :")  
        self.fathername = input("enter students fathers name :")    
        self.age = input("enter age :") 
        self.year = input("enter year :")   
        self.course = input("enter course :")   
        self.contact = input("enter contact :")

    def show_detail(self):

        print("Name :", self.name)  
        print("Fathers name :", self.fathername)    
        print("Age :", self.age)    
        print("Year of joining :", self.year)   
        print("course :", self.course)

        print("contact number :", self.contact)

    def generate_rollno(self):

        global rollno   
        rollno = rollno+1   
        self.rollno = rollno    
        print("Roll no. of students :", self.rollno)


class datafile(student):

    def _init_(self):
        super()._init_()

    def dwrite(self):

        file = open("studentsfile.txt", "a")    
        data = "{},{},{},{},{},{}\n".format(self.name, self.fathername, self.age, self.year, self.course, self.contact) 
        file.write(data)
        file.close()
        return data

    def rollgen(self,data):

        file1 = open("details.txt","a")
        fulldata = "{},{}\n".format(self.rollno, data)
        file1.write(fulldata)
        file1.close()


df = datafile()
df.generate_rollno()
df.show_detail()
x = df.dwrite()
df.rollgen(x)