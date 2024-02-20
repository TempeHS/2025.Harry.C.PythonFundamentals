def prompt_user():
    coin = int(input("Please insert a coin (25, 10, or 5 cents): "))
    while True:
        if coin in [25, 10, 5]:
            return coin


def calculate_change(total):
    change = total - 50
    return change


def main():
    total_inserted = 0
    while total_inserted < 50:
        coin = prompt_user()
        total_inserted += coin
        print(f"Amount due: {50 - total_inserted} cents")

    if total_inserted > 50:
        change = calculate_change(total_inserted)
        print(f"Change owed: {change} cents")

    main()
