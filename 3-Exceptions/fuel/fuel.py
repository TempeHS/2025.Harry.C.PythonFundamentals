def main():
    try:
        fuel = input("How much fuel is in the tanker: ")
        x, y = fuel.split("/")
        x = float(x)
        y = float(y)
        calculate_percent(x, y)
        return calculate_percent(x, y)
    except ValueError:
        pass


def calculate_percent(x, y):
    try:
        percentage = round(x / y * 100)
    except ZeroDivisionError:
        pass
    if percentage <= 1:
        print("E")
    elif percentage >= 100:
        print("F")
    else:
        print(f"{percentage}%")


main()
