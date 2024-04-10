new_numbers = []

with open("MyText.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = int(line)
        line += 1
        line = str(line)
        new_numbers.append(line)

with open("MyText.txt", "w") as file:
    for num in new_numbers:
        file.write(num + "\n")
