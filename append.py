file_to_read="Readdata.txt"
write_to_file="writedata.txt"
file=open(file_to_read,"r")
data=file.read()
file.close
with open(write_to_file,"a")as file:
    
