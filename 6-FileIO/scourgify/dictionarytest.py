import csv

amt = int(input("How many students will you input data for: "))

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    for _ in range(amt):
        name = input("Enter the students name: ")
        age = input("Enter their age: ")
        writer.writerow({"name": name, "age": age})
