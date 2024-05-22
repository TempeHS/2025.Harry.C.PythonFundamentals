class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        self.cookies += n
        if n > self.capacity:
            raise ValueError("Too many cookies")
        return n

    def withdraw(self, n):
        self.cookies -= n
        if n < 0:
            raise ValueError("You can't take what there is not")
        return n

    def capacity(self):
        return self.cookies

    def size(self):
        return self.cookies


def main():

    jar = Jar()
    jar.deposit(11)
    jar.withdraw(3)
    print(jar)


if __name__ == "__main__":
    main()
