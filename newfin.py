class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __eq__(self, other):
        if isinstance(other, Point):  # kontrollon if point1 == point2
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self):
        return f'({self.x},{self.y})'


class QTree(object):

    def __init__(self, x, y, w, h, placeholderSe=None,divided=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.nw = []
        self.ne = []
        self.se=[]
        self.sw = []
        self.divided = True
        self.points_holder = []
        self.points = []
        self.sectionizer()
        if placeholderSe is not None:
            self.points_holder = placeholderSe
        else:
            self.points_holder = []
        if divided is not None:
            self.divided=False
        if self.divided:
            self.runs()
        #self.sectionizer()

    def runs(self):
        self.points.append(self.ne)
        #self.points.append("elo")
        self.points.append(self.nw)
        self.points.append(self.se)
        self.points.append(self.sw)

    def return_points(self) -> list:
        return self.points

    def intersects(self, item):  # returns TRUE/FALSE
        return self.x - self.w / 2 <= item.x <= self.x + self.w / 2 and self.y - self.h / 2 <= item.y <= self.y + self.h / 2

    def sectionizer(self):
        for item in self.points_holder:
            if item.x > (self.x + self.w) / 2 and item.y > (self.y + self.h) / 2:
                if len(self.ne) < 5:
                    self.ne.append(item)
                else:
                    self.ne.append(QTree(0, 0, 4, 4))
            elif item.x < (self.x + self.w) / 2 and item.y > (self.y + self.h) / 2:
                if len(self.nw) < 5:
                    self.nw.append(item)
                else:
                    self.nw.append(QTree(0, 0, 4, 4))
            elif item.x < (self.x + self.w) / 2 and item.y < (self.y + self.h) / 2:
                if len(self.se) < 5:
                    self.se.append(item)
                else:
                    # self.se.append(self.divideSE())
                    # self.se=self.divideSE()
                    w2, h2 = self.w / 2, self.h / 2
                    x2, y2 = self.x - w2, self.y - h2
                    placeHolderSe = self.se
                    self.se=QTree(x2, y2, w2, h2,placeHolderSe,divided=False)
                    #self.se = QTree(x2, y2, w2, h2)


            elif item.x > (self.x + self.w) / 2 and item.y < (self.y + self.h) / 2:
                if len(self.sw) < 5:
                    self.sw.append(item)
                else:
                    self.sw.append(QTree(0, 0, 4, 4))
            # self.points=self.ne+self.nw+self.sw+self.se
        # for x in [self.ne,self.nw,self.se,self.sw]:
        #    self.points.append(x)
        if self.divided==False:
            self.points.append(self.ne)
            self.points.append(self.nw)
            self.points.append(self.se)
            self.points.append(self.sw)

    def inserter(self, item):
        self.item = item
        if self.intersects(item) and item not in self.points_holder:
            self.points_holder.append(item)

    def divideSE(self):
        w2, h2 = self.w / 2, self.h / 2
        x2, y2 = self.x - w2, self.y - h2
        return QTree(x2, y2, w2, h2).sectionizer()

    def __len__(self):
        return len(self.points)

    def __repr__(self):
        return f'({self.points})'
        # return f'({self.x},{self.y},{self.w},{self.h})'

    def __iter__(self):
        for child in self.points:
            yield child

    def append(self, item):
        self.points.append(item)


a = QTree(0, 0, 8, 8)

a.inserter(Point(1,2))
a.inserter(Point(1.1,2))
a.inserter(Point(1.2,2))
a.inserter(Point(1.3,2))
a.inserter(Point(-2,2))
a.inserter(Point(2,2))
a.inserter(Point(3,2))
a.inserter(Point(-5,-5))
a.inserter(Point(4,4))
a.inserter(Point(2,2.5))
a.inserter(Point(-2,2.1))
a.inserter(Point(2,2.2))
a.inserter(Point(3.3,2.1))
a.inserter(Point(-5,-5))
a.inserter(Point(4,4))
a.inserter(Point(1,3))
a.inserter(Point(5,2.5))
a.inserter(Point(105,2.5))
a.sectionizer()
print(a.se)
print(a.sw)
print(a.ne)
print(a.nw)
print(a.points_holder)

# print(a.points)
print(type(a))
print("next")
print(a)
