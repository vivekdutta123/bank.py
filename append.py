#file=open("myfile.txt","w")
#file.write("more information")
#file.close()
file=open("distinationfile.txt","w")
file.write("all copid information")
file.close()
file_to_read="myfile.txt"
write_to_file="destination.txt"
file=open(file_to_read,"r")
data=file.read()
file.close
with open(write_to_file,"a")as file:
    file.write(data)
print("completed")
