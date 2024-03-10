the_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

date = input("Enter the date: ")

while True:
    try:
        month, day, year = date.split("/")
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            break
    except ValueError:
        try:
            month, day, year = date.split
            month = the_months.index(month) + 1
            day = day.rstrip(",")
            day = int(day)
            if 1 <= month <= 12 and 1 <= day <= 31:
                break
        except ValueError:
            break

print(f"{year}-{int(month):02d}-{int(day):02d}")
