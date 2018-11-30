import random
class Portf:
    def __init__(self,n,m):
        self.P = [random.randint(1,n*2) for i in range(0,n)]
        self.W = [random.randint(0,m) for i in range(0,n)]
        self.W = sorted(self.W)
        self.Mass = m

    def disStart(self):
        for (i,j,k) in zip(self.P,self.W,range(0,len(self.P))):
            print("thing {} weight: {} price: {}".format(k,j,i))

    def getMaxUseful(self):
        n = len(self.W)
        r = [0 for i in range(0,n)]
        p = [0 for i in range(0,n)]
        r[0] = self.W[0]
        p[0] = self.P[0]
        for j in range(1,n):
            q = 0
            m = 0
            for i in range(0,j):
                if r[i]+self.W[j] <= self.Mass and q<=self.P[j]+p[i] :
                    m = r[i]+self.W[j]
                    q = self.P[j]+p[i]
                elif self.W[i]+self.W[j] <= self.Mass and q <= self.P[i]+self.P[j]:
                    m = self.W[i]+self.W[j]
                    q = self.P[i]+self.P[j]
                elif q <= self.P[j]:
                    m = self.W[j]
                    q = self.P[j]
            p[j] = q
            r[j] = m

        k = p.index(max(p))
        print("Optimal Solution weight: {} price: {}".format(r[k],p[k]))
        for i in range(k,-1,-1):
            print("thing {} weight: {} price: {}".format(i, self.W[i], self.P[i]))
            if (p[k]-self.P[k])!=0:
                k = p.index(p[k]-self.P[k])


l = Portf(22,80)
l.disStart()
l.getMaxUseful()