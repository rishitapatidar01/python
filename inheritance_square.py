class square:
	def __init__(self):
		self.side=int(input("enter sides"))

	def area(self):
		a=self.side*self.side
		return a

class cube(square):
	def __init__(self):
		super().__init__()
cb=cube()
side_area=cb.area()
print("side area",side_area)

"""sq1=square()
area=sq1.area()
print("area:",area)"""