# Define the function to replace any spaces with 3 dots
def slowed(speaker):
    slowed_text = speaker.replace(" ", "...")
    return slowed_text


# Get the user to input the words
speech = input("Enter the text you want to slow down: ")

# Make a new variable to lower complexity of code
result = slowed(speech)


print("Slowed down text:", result)
