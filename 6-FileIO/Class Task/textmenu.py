user_input = ""

while user_input != "4":
    user_input = input(
        "Which one would you like: \n 1) First Item \n 2) Second Item \n 3) Third Item \n 4) Exit \n Enter your option: "
    ).rstrip()
    if user_input == "1":
        print("You bought the first Item, is there anything else you would like")
    elif user_input == "2":
        print("You bought the second Item, is there anything else you would like")
    elif user_input == "3":
        print("You bought the second Item, is there anything else you would like")
    elif user_input == "4":
        break
    else:
        print("Please pick an option 1-4")
        continue
