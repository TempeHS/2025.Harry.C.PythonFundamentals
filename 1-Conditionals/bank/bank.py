answer = input("You're the bank teller greet me : ")

if answer.startswith("hello"):
    print("$0")
elif answer.startswith("h"):
    print("$20")
else:
    print("$100")
