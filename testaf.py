"""
first a ndarje te pergjithshme
ne momentin qe ndahen te gjitha
shif nqs e kane kaluar limitin
if then fillo nje ndarje te dyte me limite te reja
shif nqs kane kaluar prap limitet
then fillo nje ndarje tjtr tjtjr
repeat until limiti < limiti

Qtree(holder=None):
    def init:
        self.onetwo=[]
        self.twothree=[]
        self.holder=holder
        self.organizer()
        self.checker()
        self.mixer(onetwo+twothree)

def organizer(self):
    for item in holder:
        if self.a < item < self.b:
            self.onetwo.append(item)
        if self.b < item < self.c:
            self.twothree.append(item)

def checker(self):
    if self.onetwo > 5:
        self.onetwo=(Qtree(holder=self.onetwo)
    if self.twothree>5
        self.twothree=(Qtree(holder=self.twothree)

def intersects(self,item):
"""
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

class Qtree:
    def __init__(self,x=None, y=None, w=None, h=None,reducer=None,holder=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ne = []
        self.nw = []
        self.sw = []
        self.se = []
        self.onetwo=[]
        self.twothree = []
        self.total=[]
        if holder is None:
            self.holder=[]
        else:
            self.holder=holder
        if reducer is not None:
            self.x = self.x / 2
            self.y = self.y / 2
            self.w = self.w / 2
            self.h = self.h / 2

        self.organizer()
        self.checker()
        #needs some await
        self.mixer()


    def checker(self):
        print(self.w,self.h)
        if len(self.ne) > 3:
            self.ne = [list(Qtree(holder=self.ne,reducer=True))]
        elif len(self.nw) > 3:
            self.nw=[list(Qtree(holder=self.nw,reducer=True))]
        elif len(self.se) > 3:
            print(self.w,self.h,self.se,self.holder)
            self.se = list(Qtree(self.x,self.y,self.w,self.h,holder=self.se,reducer=True))
            print(self.se)
        elif len(self.sw) > 3:
            self.sw=[list(Qtree(holder=self.sw,reducer=True))]

    def mixer(self):
        self.total.append(self.ne)
        self.total.append(self.se)
        self.total.append(self.nw)
        self.total.append(self.sw)

    def intersects(self, item):  # returns TRUE/FALSE
        return self.x - self.w / 2 <= item.x <= self.x + self.w / 2 and \
               self.y - self.h / 2 <= item.y <= self.y + self.h / 2
    def reducer(self):
        self.x = self.x / 2
        self.y = self.y / 2
        self.w = self.w / 2
        self.h = self.h / 2

    def organizer(self):
        for items in self.holder:
            print(items)
            if items.x > (self.x + self.w) / 2 and items.y > (self.y + self.h) / 2:
                self.ne.append(items)
            elif items.x < (self.x + self.w) / 2 and items.y > (self.y + self.h) / 2:
                self.nw.append(items)
            elif items.x < (self.x + self.w) / 2 and items.y < (self.y + self.h) / 2:
                self.se.append(items)
            elif items.x > (self.x + self.w) / 2 and items.y < (self.y + self.h) / 2:
                self.sw.append(items)
    #ok
    def __iter__(self):
        for child in self.total:
            yield child
    def __repr__(self):
        return f'{self.total}'

arr=[Point(1, 1),Point(1, 1),Point(1, 1),Point(1, 1)]
a=Qtree(0,0,8,8,holder=arr)
print(a)