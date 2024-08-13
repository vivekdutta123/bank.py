def main():
    answer = input("What time is it? (HH:MM) ")
    time = convert(answer)
    if 7 <= time <= 8:
        print("Breakfast time")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")
    else:
        print("You are out of time")

def convert(time):
    hours, minutes = time.split(":")
    new_minute = float(minutes) / 60  
    return float(hours) + new_minute

if __name__ == "__main__":
    main()

