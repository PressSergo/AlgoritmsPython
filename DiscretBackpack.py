import random

class Backpack:
    def __init__(self,W,n):
        self.m = [random.randint(1,W) for i in range(0,n)]
        self.c = [random.randint(1,30) for i in range(0,n)]
        self.f = [[0 for j in range(0,W)] for i in range(0,n)]
        self.v = [[0 for j in range(0,W)] for i in range(0,n)]

    def getShedule(self):
        n = len(self.f)
        p = len(self.f[0])
        for i in range(1,n):
            for j in range(1,p):
                self.f[i][j] = self.f[i-1][j]
                self.v[i][j] = 0
                if j > self.m[i] and self.f[i-1][j-self.m[i]]+self.c[i]> self.f[i][j]:
                    self.f[i][j] = self.f[i-1][j-self.m[i]]+self.c[i]
                    self.v[i][j] = 1
        print(self.f[n-1][p-1])
        n-=1
        p-=1
        while n>=1:
            if self.v[n][p] == 1:
                p = p-self.m[n]
                print(n)
            n-=1

g = Backpack(5,60)
g.getShedule()