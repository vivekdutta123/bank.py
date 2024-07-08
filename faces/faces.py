def main():
    message=input("enter a message -")
    result=convert(message)
print(result)
def convert(message):
    msg1=message.replace(":)","🙂")
    msg2=message.replace(":(","🙁")
