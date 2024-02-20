def prompt_user():
    while True:  # Loop indefinitely until a valid coin is inserted
        coin = int(
            input("Please insert a coin (25, 10, or 5 cents): ")
        )  # Prompt the user to insert a coin
        if coin in [25, 10, 5]:  # Check if the inserted coin is a valid denomination
            return coin  # Return the inserted coin if it's valid


def calculate_change(total):
    change = (
        total - 50
    )  # Calculate the change owed by subtracting 50 from the total inserted amount
    return change  # Return the calculated change


def main():
    total_inserted = 0  # Initialize the total inserted amount to 0
    while (
        total_inserted < 50
    ):  # Continue looping until the total inserted amount reaches or exceeds 50 cents
        coin = (
            prompt_user()
        )  # Prompt the user to insert a coin and get the inserted coin value
        total_inserted += (
            coin  # Add the value of the inserted coin to the total inserted amount
        )
        print(
            f"Amount due: {50 - total_inserted} cents"
        )  # Print the remaining amount due

    if total_inserted > 50:  # Check if the total inserted amount exceeds 50 cents
        change = calculate_change(total_inserted)  # Calculate the change owed
        print(f"Change owed: {change} cents")  # Print the amount of change owed


if __name__ == "__main__":
    main()  # Call the main function recursively (This line is unnecessary and should be removed)
