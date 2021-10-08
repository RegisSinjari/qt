"""
find the shortest path in a range of nodes

initialize graph
loop through graph
check if sum of current node is smaller than the sum of other nodes

 1) understand connection between vertices and nodes
 2) loop throw em



return steps through graph



"""  # 0, 1, 2  3  4   5    6
vertices = [[0, 2, 6, 0, 0, 0, 0],
            [2, 0, 0, 5, 0, 0, 0],
            [6, 0, 0, 8, 0, 0, 0],
            [0, 5, 8, 0, 10, 15, 0],
            [0, 0, 0, 10, 0, 6, 2],
            [0, 0, 0, 15, 6, 0, 6],
            [0, 0, 0, 0, 2, 6, 0]]

# print(vertices[0][0])
"""for a in range(len(vertices)):
    for b in range(len(vertices[a])):
        print(vertices[a][b])

for a in range(len(vertices)):
    for b in range(len(vertices[0])):
        print(vertices[a][b])
        """
lista = []
holder = []
dictor = {}


def non0(vertices):
    v = list(set(vertices))
    for a in range(len(v)):
        if a == 0:
            v.pop(a)
    return v


def rmvCol(vertices, ind):
    for a in range(len(vertices)):
        vertices[a].pop(ind)
    return vertices


def minimumi(listad):
    current = 999
    for a in listad:
        if a < current and a != 0:
            current = a
    return current


def minIndex(vertices):
    current = 999
    for a in range(len(vertices)):
        if vertices[a] < current and vertices[a] != 0:
            current = a
    return current


def minDict(dict):
    pass


def rmvRow(vert, ind):
    vert.pop(ind)
    return vert


"""
for a in range(len(vertices)):
    print(vertices[a])
    print(minIndex(vertices[a]))
    print(minimumi(vertices[a]))
print(vertices)
for a in vertices:
    lista.append(minimumi(a))
    holder.append(minIndex(a))
print(vertices)
print(lista)
print(holder)
#print(minimumi(vertices[0]))
#print(lista)
print("----------")
print(vertices[1])
print(vertices[1].remove(0))
print(non0(vertices[1]))
print(vertices[5])
print(dictor)
#dictor[minIndex(vertices[1])]=minimumi(vertices[1])
#dictor[minIndex(vertices[5])]=minimumi(vertices[5])
"""

startFrom = 0
endTo = 5
print(vertices)
# okay don't delete indexes just exclude them
# loop throw a row find shortest then move to index
temp = []
"""
for rows in range(len(vertices)):
    print(rows)
    if rows==0:
        temp.append(minimumi(vertices[rows]))
    if rows == int(minIndex(vertices[rows]))-1:
        temp.append(minimumi(vertices[rows]))
"""


def neighbour(vertices, index):
    """returns a list of vertices(indexes,values) that are next to the vertex specified"""
    newList = {}
    for a in range(len(vertices[index])):
        if vertices[index][a] != 0:
            newList[f'Vertex: {a}'] = vertices[index][a]
    return newList


print("new")
for a in range(len(vertices)):
    print(neighbour(vertices, a))
    print(vertices[a])
"""
start looping from the column that is the number
find the smallest value in the row
add the index to the dict
add the values 
return to the other option 
if the option is less than
"""
#introduce some dynamic programing
#start from the two vertices start and end
print(neighbour(vertices, a))
print(vertices[a])



# 0-->5 {0,1,3,4,5}
class Dijkstra:
    def __init__(self, graph=None, start=None, end=None):
        if graph is None:
            self.graph = []
        self.placeHolders = {}
        self.results = {}
        self.infinity = 99999
        self.start = start
        self.end = end

    def solution(self):
        for a in self.graph[self.start]:
            print(a)

    def neighbours(self, vert):
        for a in range(len(self.graph[vert])):
            ...

    def __repr__(self):
        return self.results
