def main():
    while True:
        try:
            fuel = input("How much fuel is in the tanker: ")
            x, y = fuel.split("/")
            x = int(x)
            y = int(y)
            percentage = round(x / y * 100)
            if percentage > 100:
                print("retry")
                break
            elif percentage >= 99:
                print("F")
                break
            elif percentage <= 1:
                print("E")
                break
            else:
                print(f"{percentage}%")
                break
        except ValueError:
            print("Retry")
            break
        except ZeroDivisionError:
            print("Retry")
            break


main()
