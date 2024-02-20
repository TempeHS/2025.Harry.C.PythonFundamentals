# Create a function to add the 2 numbers
def add_numbers(add):
    z = sum(add)
    return z


def multiply_numbers(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


add = [4, 4]

z = add_numbers(add)
print("Here are the two added numbers", z)

print("Here are the two numbers multiplied ", multiply_numbers(add))
