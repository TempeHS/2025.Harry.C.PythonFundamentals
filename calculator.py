# Main is making the variables, int is setting up x as an int, introducing square
def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))


# Defining square variable
def square(n):
    return pow(n, 2)


main()
