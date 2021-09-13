class div:
    def __init__(self, n=None, onetwo=None, twothree=None, holder=None):
        self.a = 1
        self.b = 2
        self.c = 3
        self.total = []

        if onetwo is None:
            self.onetwo = []
        else:
            self.onetwo = []
            for v in onetwo:
                print(v)
                self.ranger(v)
        if twothree is None:
            self.twothree = []
        else:
            self.twothree = twothree

        if n is None:
            pass
        else:
            self.divider()
        if holder is None:
            self.holder = []
        else:
            self.holder = holder
        self.merger()
    def merger(self):
        self.total.append(self.onetwo)
        self.total.append(self.twothree)

    def divider(self):
        self.a = 1
        self.b = 1.5
        self.c = 2

    def divider3(self):
        self.a = 2
        self.b = 2.5
        self.c = 3

    def ranger(self, item):
        self.injet()
        if item is not list:
            if self.a < item < self.b:  # 1 /0.5 --- 2/1   a=1 b=1.5 c = 2
                self.onetwo.append(item)
            if self.b < item < self.c:  # 2 /1  ---- 3---1.5
                self.twothree.append(item)

    def injet(self):
        if len(self.onetwo) > 3:
            testa = [list(div(onetwo=list(self.onetwo), n=True))]
            print(testa, "ffff")
            print(self.onetwo)
            self.onetwo = testa
            print(self.onetwo)

    def __iter__(self):
        for child in self.total:
            yield child

    def __repr__(self):
        return f'{self.total}'


a = div()
a.ranger(1.1)
a.ranger(1.22)
a.ranger(1.3)
a.ranger(1.75)
a.ranger(1.8)
a.ranger(2.3)
print(a.onetwo)
print(a.twothree)
print(a.total)
