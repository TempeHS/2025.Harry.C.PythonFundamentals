expression = input("Please place your equation here: ")
x, y, z = expression.split(" ")

x = float(x)
z = float(z)


if y == ("+"):
    result = round(x + z, 1)
elif y == ("*"):
    result = round(x * z, 1)
elif y == ("-"):
    result = round(x - z, 1)
elif y == ("/"):
    result = round(x / z, 1)
else:
    print("Unable to satisfy request")

print(result)
