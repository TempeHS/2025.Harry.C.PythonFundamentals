d = {}
size = int(input("Enter the size : "))

for i in range(size):
    key = input("Enter the Course Name: ")
    value = input("Enter the number of students: ")
    d[key] = value

print(f" The disctionary is {d}")
