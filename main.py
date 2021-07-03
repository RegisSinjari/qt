class Point:
    def __init__(self, x, y,data=None):
        self.x = x
        self.y = y
        self.data=data
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self):
        return f'({self.x},{self.y})'
"""kjo pjesa siper eshte ok"""

class Node :
    def __init__(self,item,rect):
        self.item=item
        self.rect=rect

    def __hash__(self):
        return hash(self.item)
class Rectangle:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def divide(self):
        w2, h2 = self.w / 2, self.h / 2
        x2, y2 = self.x / 2, self.y / 2
        return Rectangle(x2,y2,w2,h2)

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_w(self):
        return self.x
    def get_h(self):
        return self.y
    def boundaryX(self, point):
        if self.x - self.w / 2 < point.x < self.x + self.w / 2:
            return True
    def boundaryY(self, point):
        if self.y - self.h / 2 < point.y < self.y + self.h / 2:
            return True
    def intersects(self):
        return self.boundaryX() and self.boundaryY

class QTree:
    def __init__(self, depth,threshHold=None):
        self.points = []
        self.sub_point=[]
        self.counter=0
        self.depth=depth
        self.threshHold = threshHold

    def __iter__(self,points,sub_point):
        for child in points:
            for child in sub_point:
                yield child
            yield child

    def add_point(self, item):
        if self.counter< self.threshhold:
            return self.points.append(item)
        else:
            return self.sub_point.append(item)

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
