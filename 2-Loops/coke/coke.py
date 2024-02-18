while True:
    x = int(input("Insert Coins: "))

    if x != "25" or "10" or "5":
        x = 0
    else:
        y = 50 - x
    if y != "0":
        continue
    elif y == "0":
        break
    print("Amount Owed: ", y)
