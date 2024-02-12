expression = input("Please place your equation here: ")
x, y, z = expression.split(" ")

float(x)
float(z)


if y == ("+"):
    result = x + z
elif y == ("*"):
    result = x * z
elif y == ("-"):
    result = x - z
elif y == ("/"):
    result = x / z
else:
    print("Unable to satisfy request")

print(round(result, 1))
