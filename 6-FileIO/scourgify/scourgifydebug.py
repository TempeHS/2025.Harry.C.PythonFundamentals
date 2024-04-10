import csv
import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif not (sys.argv[1]).endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    newcsv = sys.argv[2]
    with open(sys.argv[1]) as file:
        raw = csv.DictReader(file, fieldnames=["name", "house"])
        with open(newcsv, "w") as file:
            updated = csv.DictWriter(file, fieldnames=["First", "Last", "House"])
            updated.writeheader()
            for row in raw:
                Last, First = row["name"].split(",")
                updated.writerow({"First": First, "Last": Last, "House": ["House"]})
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
