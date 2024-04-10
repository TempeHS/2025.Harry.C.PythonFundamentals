from tabulate import tabulate
import csv
import sys

try:
    with open(f"{sys.argv[1]}", "r") as file:
        menu = csv.DictReader(file, fieldnames=["Sicilian Pizza", "Small", "Large"])
        print(tabulate(menu, tablefmt="grid"))
except FileNotFoundError:
    print("File doesn't exist")
    sys.exit(1)

if len(sys.argv) > 2:
    print("Too many command-line arguments")
elif len(sys.argv) < 2:
    print("Too few command arugments")
elif sys.argv[1].endswith(".csv"):
    print("Not a csv file")
else:
    print("What did you do")
