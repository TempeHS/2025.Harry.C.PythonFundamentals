# Define a function to convert camel case to snake case
def camel_to_snake(camel_case):
    # Initialize an empty string to store the snake case variable name
    snake_case = ""
    # Iterate through each character in the camel case variable name
    for char in camel_case:
        # Check if the character is uppercase
        if char.isupper():
            # If the character is uppercase, add an underscore before it and convert it to lowercase
            snake_case += "_"
            snake_case += char.lower()
        else:
            # If the character is lowercase, simply append it to the snake case variable name
            snake_case += char
    # Return the snake case variable name
    return snake_case


# Define the main function
def main():
    # Prompt the user to enter a variable name in camel case
    camel_case = input("Enter a variable name in camel case: ")
    # Call the camel_to_snake function to convert the camel case variable name to snake case
    snake_case = camel_to_snake(camel_case)
    # Print the snake case variable name
    print("Snake case variable name:", snake_case)


# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    main()
