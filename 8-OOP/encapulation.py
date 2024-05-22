class Person:
    def __init__(self, name, age, city):

        self.name = name
        self.age = age
        self.city = city

    @property
    def age(self):
        print("Getting age")
        return self._age

    @age.setter
    def age(self, value):
        print("Setting age")
        try:
            int(value)
            self._age = value
        except ValueError:
            print("Put in a number for age")


person1 = Person("Harry", 16, "Sydney")
print(person1.age)
