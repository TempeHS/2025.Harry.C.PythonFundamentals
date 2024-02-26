user_input = input("Enter the item: ")

fruit = {
    "Apple": "130",
    "Avocado": "50",
    "Sweet Cherries": "100",
}

value = fruit.get(user_input)


if user_input in fruit:
    print("Calories: ", value)
else:
    print("")
