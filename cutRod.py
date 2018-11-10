import random

class Rod:
    def __init__(self,n):
        self.p = [random.randint(1,28) for i in range(n)]
        self.p[0]=0
        self.r = [-1 for i in range(n)]

    def cutRod(self,n):
        if n == 0:
            return self.p[0]
        q = -1
        for i in range(1,n):
            q = max(q,self.p[i]+self.cutRod(n-i))
        return q

    def memoize_cut_down(self,n):
        if self.r[n]>=0:
            return self.r[n]
        else:
            q = -1
            for i in range(1,n+1):
                q = max(q,self.p[i]+self.memoize_cut_down(n-i))
            self.r[n] = q
            return self.r[n]

    def up_down_cut_Rod(self,n):
        r = [-1 for i in range(n)]
        r[0] = 0
        for i in range(1,n):
            q = -1
            for j in range(1,i+1):
                q = max(q,self.p[j]+r[i-j])
            r[i] = q
        return r[n-1]

    def extendButtomUp(self,n):
        r = [-1 for i in range(n)]
        s = [-1 for k in range(n)]
        r[0] = 0
        for j in range(1,n):
            q = -1
            for i in range(1,j+1):
                if q<self.p[i]+r[j-i]:
                    q = self.p[i]+r[j-i]
                    s[j] = i
            r[j] = q
        return (r , s)


h = Rod(10)
print(h.memoize_cut_down(len(h.p)-1))
print (h.up_down_cut_Rod(len(h.p)))
#print(h.cutRod(len(h.p)))
(r,s) = h.extendButtomUp(len(h.p))
print (r)
print (s)