import random

class cher:
    def __init__(self,n,m):
        self.A = [[random.randint(1,10) for i in range(m)] for j in range(n)]
        self.str =''
        for i in self.A:
            print (i)

    def findWay(self ,n,m):
        self.B = [[0 for i in range(m)] for j in range(n)]
        self.B[0][0] = self.A[0][0]

        for i in range(1,n):
            self.B[i][0] = self.A[i][0]+self.B[i-1][0]

        for j in range(1,m):
            self.B[0][j] = self.A[0][j] + self.B[0][j-1]
        i = 0
        j = 0

        for i in range(1,n):
            for j in range(1,m):
                self.B[i][j] = max(self.B[i-1][j],self.B[i][j])+self.A[i][j]

        print("_________________")
        for i in self.B:
            print (i)

    def getWay(self,n,m):
        if n == 0 and m == 0: return
        if n >0 and m ==0: self.getWay(n-1,m)
        elif n==0 and m>0: self.getWay(n,m-1)
        else:
            if (self.B[n][m]-self.A[n][m]) == self.B[n-1][m]:
                self.getWay(n-1,m)
            else:
                self.getWay(n,m-1)
        self.str+=str(n)+' '+str(m)+"; "

h = cher(3,3)
h.findWay(3,3)
h.getWay(2,2)
print('__________')
print(h.str)