import Line as l


class Point:
    def __init__(self, x_val, y_val, name):
        self.x = x_val
        self.y = y_val
        self.name = name
        self.previous_link = None
        self.next_link = None
        # self.previous_edge = None
        # self.next_edge = None

    def __str__(self):
        return format(f"{self.name}({int(self.x)},{int(self.y)})")

    def add_next_link(self, point):
        self.next_link = point
        point.previous_link = self



a = Point(-1, 5, "O")
b = Point(2, -6, "P")
#
#  print(a, b)
