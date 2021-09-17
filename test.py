listas = []


class newQuad:
    global listas

    def __init__(self, x):
        self.x = x
        self.listas=[]

    def divide(self):
        return self.x / 2
        # list1

    # return [list1+list2+list3+list4]
    def fn(self):
        return newQuad((self.x / 2))

    def appender(self, item):
        listas.append(item)

    def __repr__(self):
        return f'{self.x}'

    def intersects(self):
        pass

    def __eq__(self, other):
        if isinstance(other, newQuad):  # kontrollon if point1 == point2
            return self.x == other.x
        return False

    def division(self):
        if newQuad.x < 1.0:
            return newQuad((self.x / 2))
        else:
            self.division()

    def divisione(self, newQuad=None):
        if newQuad.x < 1.0:
            return newQuad.x
        else:
            self.divisione(newQuad.fn())

    # self.division(newQuad.fn())
    def inserter(self, item):
        if self.intersects() and len(self.listas) < 3:
            self.listas.append(newQuad((self.x / 2)))
        else:
            self.division(item)


a = newQuad(4)
b = a.inserter(a)
c=a.fn()
print(type(b))
print(type(c))
a.appender(1)
print(a)
