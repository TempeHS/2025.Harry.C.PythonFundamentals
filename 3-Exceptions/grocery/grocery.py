order = {}

item = ""

while item != "∂":

    item = (input("Enter the item you would like: ")).upper().strip()

    try:
        if item == "∂":
            break
        elif item in order:
            order[item] += 1
        else:
            order[item] = 1

    except EOFError:
        break

for a, b in order.items():
    print(f"{b} {a}")
