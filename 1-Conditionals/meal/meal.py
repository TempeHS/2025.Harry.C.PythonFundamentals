def main():
    time = input("What's the time? ")
    z = convert(time)

    if z >= 7 and z <= 8:
        print("Breakfast time")
    elif z >= 12 and z <= 13:
        print("Lunch time")
    elif z >= 18 and z <= 19:
        print("Dinner time")
    else:
        print("Nothing")


def convert(time):
    hours, minutes = time.split(":")
    x = float(minutes) / 60
    y = int(hours)
    z = x + y
    return z


main()
