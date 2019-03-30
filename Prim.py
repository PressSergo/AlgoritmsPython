class Graph:
    def __init__(self):
        n,e = map(int,input().split())
        self.adj = [[] for i in range(0,n)]
        self.key = [[float("inf"), i] for i in range(0,n)] # Из нее формируется приоритетная очередь
        self.vert = [i for i in range(0,n)] # резонирует списку ключей
        self.parent = [i for i in range(0,n)]
        for i in range(0,e):
            u, v, w = map(int, input().split())
            self.adj[u].append([w, v])
            self.adj[v].append([w, u])

    def men(self,x,y,u):
        for i in x:
            if i[1] == y:
                x.remove(i)
                x.insert(0,u)
        return x


    def prim(self):
        keys = self.key.copy()
        keys[0] = [0,0]
        self.key[0] = [0,0]
        while len(keys) != 0:
            u = keys.pop(0)
            self.vert.remove(u[1])
            for v in self.adj[u[1]]:
                if v[1] in self.vert and v[0] < self.key[v[1]][0]:
                    self.key[v[1]] = [v[0],v[1]]
                    keys = self.men(keys,v[1],[v[0],v[1]])
                    self.parent[v[1]] = u[1]
                    keys.sort()

g = Graph()
g.prim()
print(sum(i[0] for i in g.key))