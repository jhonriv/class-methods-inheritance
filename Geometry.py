class Geometry:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        print("This is an area of geometry")
        return self.x * self.y
    
    def get_perimeter(self):
        print("This is an perimeter of geometry")
        return 2 * (self.x + self.y)