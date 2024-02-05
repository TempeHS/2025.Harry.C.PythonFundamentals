# Define the function to replace any spaces with 3 dots
def Emoji(Speech):
    emoji_text = Speech.replace(":)", "🙂")
    emoji_text = Speech.replace(":(", "🙁")
    return emoji_text


# Get the user to input the words
speech = input("Please speak: ")

# Make a new variable to lower complexity of code
result = Emoji(speech)


print(result)
