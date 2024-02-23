def main():

    abbrev = input("What is the text you would like to abbreviated: ")

    vowels = {"a", "e", "i", "o", "u"}

    result = ""

    for char in abbrev:

        if char.lower() not in vowels:
            result += char

    print("Abbreviated text:", result)


if __name__ == "__main__":

    main()
