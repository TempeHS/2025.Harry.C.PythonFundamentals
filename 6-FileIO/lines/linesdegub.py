import sys

try:
    with open(f"{sys.argv[1]}", "r") as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            if line.isspace():
                continue
            else:
                total += 1
except FileNotFoundError:
    print("File does not exist")

if len(sys.argv) < 2:
    print("Too few command line prompts")
elif len(sys.argv) > 2:
    print("Too many command-line prompts")
elif len(sys.argv) != str(sys.argv).endswith(".py"):
    print("Not a python file")
else:
    print(total)
