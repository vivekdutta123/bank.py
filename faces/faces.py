def main():
    message=input("enter a message: ")
    result=convert(message)
print(result)

def convert(message):
    msg1=message.replace(":)","🙂")
    msg2=msg1.replace(":(","🙁")
    return msg2
main()

