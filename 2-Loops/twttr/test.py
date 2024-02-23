# Define a string
my_string = "Hello"

# Define a set of vowels
vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

# Initialize an empty string to store the result
result = ""

# Iterate through each character in the string
for char in my_string:
    # Check if the character is not a vowel
    if char not in vowels:
        # If it's not a vowel, append it to the result string
        result += char

# Print the result without vowels
print("String without vowels:", result)
