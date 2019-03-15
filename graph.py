class vertex:
    def __init__(self,l):
        self.lable = l
        self.wasVisible = False

    def __str__(self):
        return self.lable

class Graph:
    def __init__(self):
        self.Sm = [[0]*10 for i in range(10)]
        self.virtexList = []

    def addV(self,l):
        self.virtexList.append(vertex(l))

    def addEdge(self,s,e):
        self.Sm[s][e] = 1
        self.Sm[e][s] = 1

    def findM(self,v):
        for i in range(len(self.virtexList)):
            if self.Sm[v][i] == 1 and self.virtexList[i].wasVisible == False:
                return i
        return -1

    def dfs(self):
        stack = []
        print(self.virtexList[0])
        self.virtexList[0].wasVisible = True
        stack.append(0)
        while len(stack) != 0:
            v = self.findM(stack[len(stack)-1])
            if v == -1:
                stack.pop()
            else:
                stack.append(v)
                print (self.virtexList[v])
                self.virtexList[v].wasVisible = True
        for i in self.virtexList:
            i.wasVisible = False

    def glu(self):
        queue = []
        print (self.virtexList[0])
        self.virtexList[0].wasVisible = True
        queue.append(0)
        while len(queue)!= 0:
            v = queue.pop(0)
            while self.findM(v)!= -1:
                v2 = self.findM(v)
                print (self.virtexList[v2])
                self.virtexList[v2].wasVisible = True
                queue.append(v2)


f = Graph()
f.addV('A')
f.addV('B')
f.addV('C')
f.addV('D')
f.addV('I')
f.addV('F')
f.addEdge(0,1)
f.addEdge(0,4)
f.addEdge(1,2)
f.addEdge(1,3)
f.addEdge(4,5)
f.addEdge(5,2)
f.dfs()
print ("Glu")
f.glu()