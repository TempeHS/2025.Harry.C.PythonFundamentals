def main():
    time = input("What's the time")
    z = convert(time)
    print(z)


def convert(time):
    hours, minutes = time.split(":")
    x = float(minutes) / 60
    y = int(hours)
    z = x + y
    return z


if z >= 7 or z <= 8:
    print("Breakfast time")


main()
