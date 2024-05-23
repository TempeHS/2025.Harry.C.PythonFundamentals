class Shapes:
    def __init__(self, height, x, y):
        self.x = x
        self.y = y
        self.height = height


# See how turned area and radius into instance variables
class Circle(Shapes):

    def __init__(
        self,
        height,
        x,
        y,
    ):
        super().__init__(
            height,
            x,
            y,
        )
        self.radius = x / 2
        self.area = self.radius * self.radius * 3.14
        self.circ = 2 * 3.14 * self.radius
        self.volume = 4 / 3 * 3.14 * self.radius * self.radius * self.radius

    def get_circ_area(self):
        return f"This is the {self.area}"

    def get_circle_circ(self):
        return f"Ths is the circumference of a circle {self.circ}"

    def get_circ_vol(self):
        return f"The volume of the sphere is: {self.volume}"


# Put re-used code into initialisation
class Triangle(Shapes):
    def __init__(self, height, x, y):
        super().__init__(height, x, y)
        self.area = 1 / 2 * self.x * self.y
        self.volume = 1 / 3 * self.area * self.height

    def get_tri_area(self):
        return f"This is the area: {self.area}"

    def get_tri_volume(self):
        return f"the volume is: {self.volume}"


class Square(Shapes):
    def __init__(self, height, x, y):
        super().__init__(height, x, y)
        self.area = self.x * self.y
        self.volume = self.x * self.y * self.height

    def get_square_area(self):
        return f"The area is: {self.area}"

    def get_square_volume(self):
        return f"The square volume is: {self.volume}"


class Move:
    def __init__(self, colour, x, y, z):
        self.colour = colour
        self.x = x
        self.y = y
        self.z = z


test = Circle(3, 5, 9)
print(test.get_circ_vol())
