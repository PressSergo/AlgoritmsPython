class Color:
    WHITE = 0
    GRAY = 1
    BLACK = 2

class Vertex:
    def __init__(self,key):
        self.color = None
        self.parent = None
        self.d = None
        self.f = None
        self.key = key
        self.adj = []

class Graph:
    def __init__(self):
        self.vertex = []

    def addVertex(self,key):
        x = Vertex(key)
        x.color = Color.WHITE
        x.d = 0
        self.vertex.append(x)

    def addEdge(self,f,s):
        x = None
        y = None
        for i in self.vertex:
            if i.key == f:
                x = i
                break
        for j in self.vertex:
            if j.key == s:
                y = j
                break
        x.adj.append(y)
        y.adj.append(x)

    def BFS(self,s):
        s.color = Color.GRAY
        s.distance = 0
        Q = []
        Q.append(s)
        while len(Q) != 0 :
            u = Q.pop()
            for v in u.adj:
                if v.color == Color.WHITE:
                    v.distance = u.distance + 1
                    v.parent = u
                    Q.append(v)
                    print(v.key)
            u.color = Color.BLACK

    def DFFSVised(self,u):
        print(u.key)
        self.time = self.time+1
        u.d = self.time
        u.color = Color.GRAY
        for v in u.adj:
            if v.color == Color.WHITE:
                v.parent = u
                self.DFFSVised(v)
        u.color = Color.BLACK
        self.time+=1
        u.f = self.time


    def DFS(self):
        self.time = 0
        for u in self.vertex:
            if u.color == Color.WHITE:
                self.DFFSVised(u)



g = Graph()
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)

g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(3,5)
g.addEdge(3,4)

#g.BFS(g.vertex[0])

g.DFS()