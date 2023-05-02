from Geometry import Geometry


class Rectangule(Geometry):
    def __init__(self, x, y):
        super().__init__(x, y)

    def get_area(self):
        print("This is an area of rectangule")
        return self.x * self.y

    def get_perimeter(self):
        print("This is an perimeter of rectangule")
        return 2 * (self.x + self.y)