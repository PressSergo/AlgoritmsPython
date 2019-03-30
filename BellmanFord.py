class Graph:
    def __init__(self):
        n,e = map(int,input().split())
        self.Edge = []
        self.Vertex = n
        self.adj = [[] for i in range(0,n)]
        self.key = [[float("inf"), i] for i in range(0,n)] # оценка кратчайшего пути для ребра
        self.parent = [i for i in range(0,n)]

        for i in range(0,e):
            u, v, w = map(int, input().split())
            self.adj[u].append([w, v])
            self.Edge.append([u,v,w])

    def w(self,u,v):
        for i in self.adj[u]:
            if i[1] == v:
                return i[0]

    def relax(self,u,v):
        if self.key[v][0]>self.key[u][0]+self.w(u,v):
            self.key[v][0] = self.key[u][0]+self.w(u,v)
            self.parent[v] = u

    def BellmanFord(self):
        self.key[0] = [0,0]
        for c in range(0,self.Vertex):
            for i in self.Edge:
                self.relax(i[0], i[1])
        for c in self.Edge:
            if self.key[c[1]][0]>self.key[c[0]][0]+c[2]:
                return False
        return True

g = Graph()
g.BellmanFord()
print(sum(i[0] for i in g.key))