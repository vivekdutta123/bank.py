def main():
    answer=input("what time is it")
    time=convert(answer)
if time>=7 and time<=8:
    print("breakfast time")
elif time>=12 and time<=13:
    print("lunch time")
elif time>=18 and time<=19:
    print("dinner time")
else:
    print("you are out of time")
def convert(time):
    hours, minutes = time.split(":")
    new_minute=float(minute)/60
    return float(hours) + new_minute

if __name__ == "__main__":
    main()

