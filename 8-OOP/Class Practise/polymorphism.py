class Dog:
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walks(self):
        return "He prefers car rides"

    def bark(self):
        return "Woof!"


class Samoyed(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)


class Poodle(Dog):

    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def shedding_amount():
        return 0


class GoldenRetriver(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def fetch_ability(self):
        if self.age < 2:
            return 8
        elif self.age < 10:
            return 10
        else:
            return 7


class GoldenDoodle(Poodle, GoldenRetriver):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def bark(self):
        return "Arf!"


Harry = GoldenDoodle("Harry", 2, 5)
print(Harry.bark())
