# import sys

try:
    with open(f"{sys.argv[1]}", "r") as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            if line.isspace():
                continue
            else:
                total += 1
                print(total)
except FileNotFoundError:
    print("File does not exist")

file_name = sys.argv[1]

if len(sys.argv) < 2:
    print("Too few command line prompts")
elif len(sys.argv) > 2:
    print("Too many command-line prompts")
elif not file_name.endswith(".py"):
    print("Not a python file")
else:
    sys.exit(1)
