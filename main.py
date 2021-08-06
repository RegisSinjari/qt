Pointss=[]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __eq__(self, other):
        if isinstance(other, Point):            #kontrollon if point1 == point2
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self):
        return f'({self.x},{self.y})'


"""kjo pjesa siper eshte ok"""


class Node:
    def __init__(self, item, rect):
        self.item = item
        self.rect = rect            #mbase behen merge

    def __hash__(self):
        return hash(self.item)


class Rectangle:
    def __init__(self, x, y, w, h,lista=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.lista=lista
    def divideNE(self,lista=None):
        if lista is None:
            lista = []
        w2, h2 = self.w / 2, self.h / 2
        x2, y2 = self.x - w2, self.y + h2
        return Rectangle(x2, y2, w2, h2,lista=[])
    def divideNW(self,lista=None):
        if lista is None:
            lista = []
        w2, h2 = self.w / 2, self.h / 2
        x2, y2 = self.x + w2, self.y + h2
        return Rectangle(x2, y2, w2, h2,lista=[])
    def divideSE(self,lista=None):
        if lista is None:
            lista = []
        w2, h2 = self.w / 2, self.h / 2
        x2, y2 = self.x - w2, self.y - h2
        return Rectangle(x2, y2, w2, h2,lista=[])
    def divideSW(self,lista=None):
        if lista is None:
            lista = []
        w2, h2 = self.w / 2, self.h / 2
        x2, y2 = self.x + w2, self.y - h2
        return Rectangle(x2, y2, w2, h2,lista=[])
    def divide(self, item):
        if item.x > self.x / 2 and item.y > self.y / 2:
            return self.divideNE()
        elif item.x < self.x / 2 and item.y > self.y / 2:
            return self.divideNE()
        elif item.x < self.x / 2 and item.y < self.y / 2:
            return self.divideSE()
        elif item.x > self.x / 2 and item.y < self.y / 2:
            return self.divideSW()



    def boundaryX(self, point): # remove?
        if self.x - self.w / 2 < point.x < self.x + self.w / 2:
            return True

    def boundaryY(self, point): # remove?
        if self.y - self.h / 2 < point.y < self.y + self.h / 2:
            return True

    def intersects(self, item): #dokumento dumbo returns TRUE/FALSE
        #print("fals")
        #print(self.x, self.y, self.h, self.w, item.x, item.y)
        #print(f'({self.x}-{self.w / 2}<{item.x}<{self.x + self.w / 2})')
        #print(f'({self.y}-{self.h / 2}<{item.y}<{self.y + self.h / 2})')
        # print (str(self.x - self.w / 2 +'<'+ item.x +'<'+ self.x + self.w / 2 ))
        return self.x - self.w / 2 <= item.x <= self.x + self.w / 2 and self.y - self.h / 2 <= item.y <= self.y + self.h / 2
        print("tru")
        # self.boundaryX and self.boundaryY
    def __repr__(self):
        return f'({self.x},{self.y},{self.w},{self.h})'

    def appends(self, item):
        self.lista.append(item)


class QTree(Rectangle):

    def __init__(self, x=None, y=None, w=None, h=None, lista=None):  # x=None,y=None
        super().__init__(x, y, w, h,lista)
        self.points = []
        self.sub_point = []
        self.counter = 0
        self.capacitys=3
        self.depth = 1

    def capacity(self,subpoints,threshhold):
        return len(subpoints)>threshhold


    def __iter__(self, points, sub_point):
        for child in points:
            for child in sub_point:
                yield child
            yield child

    def add_point(self, item):
        print(type(item))

        if len(self.points)< 5:
            return self.points.append(item)
        elif len(self.sub_point)< 5:
            Rectangle.divide(item)
            return self.sub_point.append(item)

    def insert(self, item):
        # TODO SHIKO DHE NJER RETURN TYPE done
        print(type(self.points))
        if item not in self.points:
            self.add_point(item)

    def newinsert(self, item):
        self.item=item
        if Rectangle.intersects(self,item):
            if len(self.points) > 2:
                Rectangle.divide(self, item)
                if Rectangle.intersects(self, item):
                    print("u nda u fut")
                    if len(self.sub_point) > 2:
                        self.sub_point.append([item])
                    self.sub_point.append(item)
            elif len(self.sub_point) > 2:
                Rectangle.divide(self, item)
            self.points.append(item)

#so like you need lists on the rectangles and when you divide new lists are created 
    def newNewInsert(self,item):
        self.item = item
        if len(self.points)<self.capacitys:
            if Rectangle.intersects(self, item):
                print(len(self.points))
                return self.points.append(item)
        if len(self.sub_point)<self.capacitys:
            Rectangle.divide(self,item)
            self.depth += 1
            if Rectangle.intersects(self, item):
                return self.sub_point.append(item)
        else:
            self.sub_point=[]

    def insertneu(self, item):
        if item not in self.points:
            self.newNewInsert(item)

    def return_points(self) -> list:
        return self.points
    def return_sub_points(self) -> list:
        return self.sub_point
    def __len__(self):
        return len(self.points)



#ads = Rectangle(0, 0, 8, 8)
b = Point(1, 2)
#print(ads)
a = QTree(0, 0, 8, 8)
print(type(a))
"""
a.newNewInsert(Point(2, 1))
a.newNewInsert(Point(2, 1))
a.newNewInsert(Point(2, 1))
a.newNewInsert(Point(2, 1))
a.newNewInsert(Point(2, 1))
a.newNewInsert(Point(2, 1))
a.newNewInsert(Point(2, 1))
a.newNewInsert(Point(2, 1))
a.newNewInsert(Point(2, 1))
a.newNewInsert(Point(-1, 2))"""
a.insertneu(Point(-1, 2))
a.insertneu(Point(2, 1))
a.insertneu(Point(-1.5, 2))
a.insertneu(Point(-1.6, 2))
a.insertneu(Point(-1.7, 2))
a.insertneu(Point(-1.8, 2))
a.insertneu(Point(-1.8, 2.1))
a.insertneu(Point(-1.8, 2.2))


#print(ads)
print(a.points)
print(a.sub_point)
print(a.lista)
#m = Point(1, 2)
#n = a.points[0]
# print(type(n),type(m),type(a.points[1]))
# print(m==a.points[1])
#cd = a.return_points()
#print(Rectangle(0,0,4,4).divideNE())
#print("--------------",Rectangle(0,0,4,4).divideNE().intersects(Point(-2, 1)))
#print("________",Rectangle(0,0,4,4).divide(Point(-2, 1)))
# print(a.points[1])
# print(a.points[2])
# print(type(a.points[1]))
# print(a.points[1]==a.points[2])
#print(cd, len(a),a.return_sub_points())
"""
insert>
points qe intersect nga Rect

    if points counter>3
        split rect
        insert on subpoints that intersect minirects
        points.append(subpoints)
        if subpoints counter >3
            split()
            insert()
            counter=
    points.append(point)
Rect(x,y,w,h,counter=0)==>add ==>counter+1
(divide) return counter0

add(item)   [(1, 2),(1, 2),(2, 2)]  |   [0,0,3,3]        add:
    if intersects(Rectangle):
        if points.len<2:        [(1, 2),[(1, 2),(2, 2)]]
            append to points
        elif subpoints <2
            Rectangle.Divide()
            append to subpoints
        append to subpoints
    append subpoints to points
"""



