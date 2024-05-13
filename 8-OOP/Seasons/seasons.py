from datetime import date
import inflect
import sys

p = inflect.engine()


class Seasons:
    def __init__(self, Date, tdy):
        self.Date = Date
        self.tdy = tdy

    @classmethod
    def get_date(cls):
        try:
            Date = date.fromisoformat(input("Enter Given Date in ISO Format: "))
        except ValueError:
            sys.exit("ISO format is YYYY-MM-DD: Try Again")
        tdy = date.today()
        return cls(tdy, Date)

    def calc_time(self):
        timedelta = self.Date - self.tdy
        timedelta = timedelta.days * 1440
        return timedelta


def main():
    test = Seasons.get_date()
    words = p.number_to_words(test.calc_time()).capitalize()
    words += " minutes"
    print(words)


if __name__ == "__main__":
    main()
