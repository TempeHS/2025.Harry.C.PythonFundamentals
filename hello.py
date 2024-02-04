# Defining hello function, using paramter to plug into print
def main():
    name = input("What's your name? ")
    hello()


def hello(to="world"):
    print("hello,", to)


main()
