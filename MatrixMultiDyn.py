import random
import math

class MatrixMulti:
    def __init__(self,n):
        self.p = [random.randint(1,67) for i in range(n+1)] #size matrix p(i-1,i)
        self.cM = len(self.p) #lengt sequence matrix
        self.strin =''

    def MatrixChainOrder(self):
        n = self.cM
        self.m = [[math.inf for i in range(n)] for j in range(n)]
        self.s = [[0 for i in range(0,n)] for j in range(0,n)]
        for i in range(0,n):
            self.m[i][i] = 0
            self.s[i][i] = 0
        for l in range(2,n+1):
            for i in range(1,n-l+1):
                j = i+l-1
                for k in range(i,j):
                    q = self.m[i][k]+self.m[k+1][j]+self.p[i-1]*self.p[k]*self.p[j]
                    if q < self.m[i][j]:
                        self.m[i][j] = q
                        self.s[i][j] = k
        return (self.m,self.s)

    def printOptimal(self,s,i,j):
        if i==j:
            self.strin+='A'+str(i)
        else:
            self.strin+='('
            self.printOptimal(s,i,s[i][j])
            self.printOptimal(s,s[i][j]+1,j)
            self.strin+=')'

j = MatrixMulti(5)
print (j.p)
k = j.MatrixChainOrder()
print (k[0][1][j.cM-1])
print (k[1])
j.printOptimal(j.s,1,j.cM-1)
print (j.strin)