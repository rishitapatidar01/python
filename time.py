#import time as t
#import time.time()
from time import*

i=int(input("enter the fact:"))
#start_time=time.time()
#start_time=t.time()
start_time =time()
fact=1
if i==0 or i==1:
	print("{} is factorial of {}".format(fact,i))
else:
	for j in range(1,i+1):
		fact=fact*j 
	print("{}is factorial of {}".format(fact,i))
#end_time=time.time()
#end_time=t.time()
end_time =time()
total_time = end_time - start_time
print("totaltime=",total_time)