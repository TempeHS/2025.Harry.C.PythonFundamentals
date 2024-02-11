answer = input("What's the answer to the universe? ")


match answer:
    case "42" | "Forty Two" | "forty-two":
        print("Yes")
    case _:
        print("No")
