#datalist=[1234,11.23,1+2j]
#for item in datalist:
    #print("type of item is",item,type(item))
#f = []
#a = []
#ch = "y"

#while ch.lower() == "y":
   # item = int(input("Enter an item for the list: "))
    #a.append(item)
    #ch = input("Do you want to enter another element (yes/no)? ").lower()

#print("List is", a)

# To print factorial
#fact = []
#for i in a:
    #f = 1
    #for j in range(1, i + 1):
    # f *= j
    #fact.append(f)

#print("Factorial of the numbers is", fact)
#total = 0
#count = 0

#while True:
    #inp = input("Enter a number: ")

    #if inp.lower() == "done":
        #break

    #try:
        #value = float(inp)
        #total = total + value
        #count = count + 1
    #except ValueError:
       # print("Invalid input, please enter a number.")

#if count > 0:
    #average = total / count
    #print('Average:', average)
#else:
   # print("No numbers were entered.")
numlist=[]
while True:
    inp=input("Enter a number:")
    if inp.lower()=="done":
        break
    try:
        
