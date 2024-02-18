camel = input("Enter the name please? ")

snake = ""

for i in camel:

    if i.isupper():

        snake += i.lower
    else:
        snake += i

print(snake.lstrip("_"))
