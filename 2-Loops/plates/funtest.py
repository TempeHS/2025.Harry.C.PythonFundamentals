def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for _ in s:
        if (
            s[0:2].isalpha()
            and 2 <= len(s) <= 6
            and s[-1].isdigit()
            and s[0] != "0"
            and s.isalnum()
        ):
            return s
        else:
            break


if __name__ == "__main__":

    main()
