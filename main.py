#import sample1
import sample1 as s
#calculating permutation
n,r=int(input("enter the value of n:")),int(input("enter the value of p:"))
if n>=r:
	result=s.fact(n)/s.fact(n-r)
	print("permutation are",result)
else:
	print("n should be greater than r.")

#calculating combination
n,r=int(input("enter the value of n:")),int(input("enter the value of p:"))
if n>=r:
	result=s.fact(n)/((s.fact(r))*(s.fact(n-r)))
	print("combination are",result)
else:
	print("n should be greater than r.")

