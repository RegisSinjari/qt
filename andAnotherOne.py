class Qtree:

    def __init__(self, ne=None, nw=None, se=None,sw=None):
        self.total = []
        self.totale=[]
        self.ne = []
        if ne is None:
            self.ne = []
        else:
            self.ne = ne
        ####
        self.nw = []
        if nw is None:
            self.nw = []
        else:
            self.nw = nw
        ####
        if se is None:
            self.se = []
        else:
            self.se = se
        ####
        if sw is None:
            self.sw = []
        else:
            self.sw = sw
        self.merger()
    def merger(self):
        self.total.append(self.ne)
        self.total.append(self.nw)
        self.total.append(self.sw)
        self.total.append(self.se)
    def finale(self):
        self.total.append(self.ne)
        self.total.append(self.nw)
        self.total.append(self.sw)
        self.total.append(self.se)
        return self.totale