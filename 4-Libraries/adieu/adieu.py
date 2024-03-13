import inflect

p = inflect.engine()

names = []

user_input = ""

while True:

    user_input = input("Enter a name: ")

    if user_input != "∂":
        names.append(user_input)
    else:
        break

names = p.join((names), final_sep="")


print(f"Adieu, adieu, to {names}")
