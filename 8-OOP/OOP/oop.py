class Shapes:
    def __init__(
        self,
        colour,
        height,
        x,
        y,
        z,
    ):
        self.colour = colour
        self.x = x
        self.y = y
        self.z = z
        self.height = height


# See how turned area and radius into instance variables
class Circle(Shapes):

    def __init__(self, colour, height, x, y, z):
        super().__init__(colour, height, x, y, z)
        self.r = x / 2
        self.a = self.r * self.r * 3.14

    def circ_area(self):
        return f"This is the {self.a}"

    def circle_circ(self):
        circ = 2 * 3.14 * self.r
        return f"Ths is the circumference of a circle {circ}"

    def return_vol(self):
        r = self.x / 2
        r3 = r * r * r
        v = 4 / 3 * 3.14 * r3
        return f"The volume of the sphere is {v}"


# Put re-used code into initialisation
class Triangle(Shapes):
    def __init__(self, colour, height, x, y, z):
        super().__init__(colour, height, x, y, z)

    def get_tri_area(self):
        area = 1 / 2 * self.x * self.y
        return f"This is the area: {area}"

    def get_tri_volume(self):
        area = 1 / 2 * self.x * self.y
        v = 1 / 3 * area * self.height
        return f"the volume is {v}"


test = Circle("Red", 3, 5, 2, 9)
print(test.circ_area())
