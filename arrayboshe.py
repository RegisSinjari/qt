class arr:

    def __init__(self, a=None, b=None, c=None):
        self.total = []
        self.totale=[]
        self.a = []
        if a is None:
            self.a = []
        else:
            self.a = list(a)
        ####
        self.b = []
        if b is None:
            self.b = []
        else:
            self.b = b
        ####
        #self.c = []
        if c is None:
            self.c = []
        else:
            print("log")
            print(c)
            self.c = c
            print(self.total)
        self.merger()

    def merger(self):
        print("ktu")
        self.total.append(self.a)
        self.total.append(self.b)
        self.total.append(self.c)
        print(self.total)

    def injection(self):
        print("injection")
        print(len(self.c))
        if len(self.a) >5 :
            self.a=(arr().total)
        if len(self.b) > 3:
            copylista = list(self.b)
            self.b.clear()
            self.b = list(arr(b=copylista))
            self.total[1] = [self.b]
        if len(self.c) > 3:
            print(len(self.c))
            print("copylista")
            print(self.c)
            copylista=list(self.c)
            placeholder=[list(arr(c=copylista))]

            #self.c.clear()
            #del self.c[:]
            print(len(placeholder))
            self.c=placeholder
            print("then")
            print(self.c)
            #self.c = [self.c.copy()]
            #self.c.clear()
    def finale(self):
        self.totale.append(self.a)
        self.totale.append(self.b)
        self.totale.append(self.c)
        return self.totale
    def organizer(self, item):
        self.injection()
        print("te organizeri")
        print(len(self.c))
        if 0 < item <= 1:
            self.a.append(item)
        elif 1 < item <= 2:
            self.b.append(item)
        elif 2 < item <= 3:
            self.c.append(item)
    def __iter__(self):
        for child in self.total:
            yield child
    def __repr__(self):
        return f'{self.total}'


"""
    def append(self, item):
        self.total.append(item)
    def __len__(self):
        return len(self.total)"""

a = arr()
print(a.total)
a.organizer(1)
a.organizer(1)
a.organizer(1.1)
a.organizer(1.2)
a.organizer(2.3)
a.organizer(2.3)
a.organizer(2.4)
a.organizer(2.6)
a.organizer(2.4)
a.organizer(2.6)
a.organizer(2.7)
a.organizer(2.6)
a.organizer(2.7)
a.organizer(2.7)
a.organizer(2.7)
a.organizer(2.8)
a.organizer(2)
a.organizer(1.9)
print("fin")
print(a.c)
print(a.total)
print(len(a.total))
print(a.finale())
"""b=arr(c=[1,2])
print(b.total)"""
