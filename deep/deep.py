answer=input(" what is the answer to the Great Question of Life, the Universe and Everything?")
if answer.strip()=="42":
    print("yes")
if answer.capitalize().strip()=="forty two":
    print("yes")
if answer.lower().strip()=="forty-two":
    print("yes")
else:
    print("no")
