from datetime import date

Date = date.fromisoformat(input("Enter Given Date in ISO Format: "))

tdy = date.today()

timedelta = tdy - Date

timedelta = timedelta.days * 1440

print(timedelta)
