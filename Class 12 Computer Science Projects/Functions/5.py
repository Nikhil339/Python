def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7 <= time <= 9:
        print("breakfast time")
    elif 12 <= time <= 15:
        print("lunch time")
    elif 19 <= time <= 21:
        print("dinner time")
    else:
        pass

def convert(x):
    hours, minutes = x.split(":")
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes/60
    return hours + minutes


if __name__ == "__main__":
    main()