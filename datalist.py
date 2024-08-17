#datalist=[1234,11.23,1+2j]
#for item in datalist:
    #print("type of item is",item,type(item))
f=[]
a=[]
while ch ==y:
    print ch.lower()
    item=int(input("enter a item of a list"))
    a.append(item)
    ch=int(input("do you want to enter a element (yes/no)?")).lower()
print("list is",a)
#to print factorial
for i in a:
    f=1
    for j in range(1,i+1):
        f*=j

fact.append(f)
print("factorial of a number is",fact)
