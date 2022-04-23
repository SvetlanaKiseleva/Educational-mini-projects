class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def rect_area(self):
        return self.width * self.height


value_1 = Rectangle(8, 12)
print(value_1.rect_area())
