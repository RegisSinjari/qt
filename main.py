class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
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
        if self.x - self.w/ 2 < point.x < self.x + self.w / 2:
            return True
    def boundaryY(self, point):
        if self.y - self.h / 2 < point.y < self.y + self.h / 2:
            return True
    def intersects(self,item):
        print("fals")
        print(self.x,self.y,self.h,self.w,item.x,item.y)
        print(f'({self.x}-{self.w/2}<{item.x}<{self.x+self.w/2})')
        print(f'({self.y}-{self.h / 2}<{item.y}<{self.y + self.h / 2})')
        #print (str(self.x - self.w / 2 +'<'+ item.x +'<'+ self.x + self.w / 2 ))
        return self.x - self.w/ 2 <= item.x <= self.x + self.w / 2 and self.y - self.h / 2 <= item.y <= self.y + self.h / 2
        print("tru")
         #self.boundaryX and self.boundaryY

class QTree:
    def __init__(self,x=None,y=None,w=None,h=None ,depth=None,threshHold=None): #x=None,y=None
        self.points = []
        self.x=x
        self.y = y
        self.w = w
        self.h = h
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
        print(type(item))
        if Rectangle.intersects(self,item):
            return self.points.append(item)

        """
        if self.counter< self.threshhold:
            return self.points.append(item)
        else:
            return self.sub_point.append(item)"""

    def insert(self,item):
         # TODO SHIKO DHE NJER RETURN TYPE
        print(type(self.points))
        if item not in self.points:
            self.add_point(item)



    def return_points(self) -> list:
        return self.points

    def __len__(self):
        return len(self.points)


b = Point(1,2)
print(type(b))
a=QTree(0,0,4,4)
print(type(a))
a.add_point(Point(1,2))
a.insert(Point(1,3))
a.insert(Point(2,1))
a.insert(Point(2,1))
a.insert(Point(1,2))
m=Point(1,2)
n=a.points[0]
#print(type(n),type(m),type(a.points[1]))
#print(m==a.points[1])
cd = a.return_points()
#print(a.points[1])
#print(a.points[2])
#print(type(a.points[1]))
#print(a.points[1]==a.points[2])
print(cd, len(a))
