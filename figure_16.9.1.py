class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def __str__(self):
        return 'Triangle({}, {}, {}, {}, {}, {})'.format(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)


triangle_1 = Triangle(1, 2, 4, 5, 5, 1)
print(triangle_1)
