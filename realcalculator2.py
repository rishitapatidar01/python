def typecheck(x):
    num_chr=["0","1","2","3","4","5","6","7","8","9"]
    num_count=0
    dot_count=0
    other_count=0

    for i in x:
        if i in num_chr:
            num_count+=1
        elif i== "." :
            dot_count+=1
        else:
            other_count+=1

    if other_count==0 and dot_count==0:
        x=int(x)
    elif other_count==0 and dot_count==1:
        x=float(x)
    else:
        x=str(x)
    return x


def calculater(x,y,z):
    if z == "+" :
        result = x+y
    elif z== "-" :
        result = x-y
    elif z== "*":
        result = x*y
    else:
        result=x/y
    return result


def convert(p):
    temp1=int(p)
    temp2=p-temp1

    if temp2 <=0:
        final=int(p)
    else:
        final=float(p)
    return final



a=input("enter fisrt  value : ")
b=input("enter second value : ")
a=typecheck(a)
b=typecheck(b)
print("")
print("first value type = " ,type(a))
print("first value type = " ,type(b))
print("")
c=input("enter the operation (+ , - , * , /) : ")
d=calculater(a,b,c)
print("\n the result is : ",d)


d=convert(d)
print("the typecasted result is : ",d)
print(type(d))