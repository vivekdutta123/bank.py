file=open("myfile.txt","w")
# w refers to open for writing, truncting the first file .
file.write("Hellow how are you. I think you love coding lets begain with python.")
file.close()
file=open("distinationfile.txt","w")
file.write("all copid information")
file.close()
file_to_read="myfile.txt"
write_to_file="destination.txt"
file=open(file_to_read,"r")
#r open for reading
data=file.read()
file.close
with open(write_to_file,"a")as file:
    # a which allows appending data to the end of the file.
    file.write(data)
print("completed")
