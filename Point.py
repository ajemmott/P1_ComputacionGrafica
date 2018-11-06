class Point:
    def __init__(self, x_val, y_val, name):
        self.x = x_val
        self.y = y_val
        self.name = name

    def __str__(self):
        return format(f"{self.name}({int(self.x)},{int(self.y)})")


a = Point(-1, 5, "O")
b = Point(2, -6, "P")
#
#  print(a, b)
