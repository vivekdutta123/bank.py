answer=input(" what is the answer to the Great Question of Life, the Universe and Everything?")
if answer.strip()=="42":
    print("yes")
if answer.capitalize()=="Forty Two":
    print("yes")
if answer=="forty-two":
    print("yes")
else:
    print("no")
