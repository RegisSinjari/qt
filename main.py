class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'


def recta(x, y, w, h):
    return x + w, y + h


class QTree:
    def __init__(self, x=None, y=None, w=None, h=None, threshHold=None):
        self.points = []
        self.threshHold = threshHold
        self.x, self.y = x, y
        self.w, self.h = w, h

    def subdivide(self, recta):
        w=

    def add_point(self, item):
        return self.points.append(item)

    def insert(self, x, y):
        item = str(Point(x, y))  # TODO SHIKO DHE NJER RETURN TYPE
        if item not in self.points:
            self.add_point(item)

    def return_points(self) -> list:
        return self.points

    def __len__(self):
        return len(self.points)


a = QTree()
a.insert(1, 2)
a.insert(3, 4)
a.insert(1, 2)
a.insert(1, 2)
cd = a.return_points()
print(cd, len(a))
