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
    """returns a dict of vertices(indexes,values) that are next to the vertex specified"""
    newList = {}
    for a in range(len(vertices[index])):
        if vertices[index][a] != 0:
            newList[f'Vertex: {a}'] = vertices[index][a]
    return newList


def minNotIn(vertices, lista):
    current = 999
    for a in vertices:
        if a < current and a != 0 and a not in lista:
            current = a
    return current


print("new")
"""
start looping from the column that is the number
find the smallest value in the row
add the index to the dict
add the values 
return to the other option 
if the option is less than
"""
# introduce some dynamic programing
# start from the two vertices start and end

# find all the neighbours and start adding ideja eshte te fillosh ne 0 dhe te mbarrosh ne 5
#scrap that
zgjidhje = {}
zgj=[]
visitedNodes=[]
# def sol2(start,finish):
#     bestRoute=0
#     start = neighbour(vertices, start)
#     startiVal = list(start.values())
#     startiKey = list(start.keys())
#     print(start)
#     #if sum e nje route me vogel se routi tjtr dmt if sum
#
#     route=0
#     for a in start:
#
#         for b in neighbour(vertices, int(a.strip('Vertex: '))):
#
#         neigh=neighbour(vertices, a)
#
#
#
#
#     print(startiVal)
#     print(startiKey)
#     while len(nodes):
#         ...
#
#         #look for the neighbour in start
#
#         #
#         #bla bla pop.start
#         #start =lowest value
#     return starti





# duhen 2 cikle dhe llogarit kush eshte shuma me e vogel

# def solution(start, finish):
#     """ fillon me nje cikel te vertexi i pare"""
#     starti = neighbour(vertices, start)
#     startiL = list(starti.values())
#     print("eeeee")
#     print(startiL)
#     stTest = [11, 2]
#     finish = neighbour(vertices, finish)
#     exclude = set()
#     minVal = 0
#     minVal2 = 0
#     for key in starti:  # look for
#         exc = start
#         minVal = min(starti, key=starti.get)
#         exclude.add(exc)
#         minVal3 = minNotIn(startiL, exclude)
#         print(key, starti[key])
#         print(exclude)
#         print("notin")
#         print(minVal3)
#         starti = neighbour(vertices, start)
#
#         for key2 in neighbour(vertices, int(key.strip("Vertex: "))):
#             minVal2 = min(neighbour(vertices, int(key.strip("Vertex: "))),
#                           key=neighbour(vertices, int(key.strip("Vertex: "))).get)
#             print(key2)
#             print("minnn2" + minVal2)
#             # switch nums
#     for i in range(len(vertices)):
#         ...
#     # nje gje qe fillon basically recurssion
#     # start = 0
#     # base case eshte qe
#     endforReal = finish
#     if start == endforReal:
#         return
#
#     print("minnn1" + minVal)
#     """for key in finish:  # look for start
#         print(key,finish[key])"""
#

print("####")

allNeighnours={f'Vertex: {a}' : neighbour(vertices, a) for a in range(len(vertices))}
allNodes=[f'Vertex: {a}' for a in range(7)]
#print(allNodes)
path=[]
path2=[]
print("ssssssss")
for node in allNeighnours['Vertex: 0']:
    if allNeighnours['Vertex: 0'][node] == minimumi(allNeighnours['Vertex: 0'].values()):
        print("noe")
#print(minimumi(allNeighnours['Vertex: 0'].values()))
#print(allNeighnours['Vertex: 1']['Vertex: 2'])
print("^^^")

#print(allNeighnours)
def dikstr(st,fin):

    currentNode=st
    #ktu ok
    # tani kerko ca ke perreth dhe kthej ne lista
    # for node in allNeighnours[currentNode]:
    #     if allNeighnours[currentNode][node]<inF:
    #         inF=allNeighnours[currentNode][node]
    #         inInd=node
    #         visitedNodes.append(node)
    #     visitedNodes.append(node)
    # print(inF)
    # print(inInd)
    allNodes.remove(st)
    while len(allNodes):
        if currentNode == fin:
            break
        for node in allNeighnours[currentNode]:
            if node in allNodes:
                if allNeighnours[currentNode][node] == minNotIn(allNeighnours[currentNode].values(),path2):
                    path.append(node)
                    path2.append(allNeighnours[currentNode][node])
                    currenttNode = node
                else:
                    allNodes.remove(node)
                if node in allNodes:
                    allNodes.remove(node)
        currentNode=currenttNode
        print(currentNode)




dikstr('Vertex: 0','Vertex: 3')
print(path)
print(path2)
print("Eyo KTU")
print(visitedNodes)
        #sum(min(nodit,min(nodit+1))
        # current node=min


#print(allNeighnours['Vertex 1: '])

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
