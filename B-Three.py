T = 2

class Node:
    def __init__(self):
        self.n = 0
        self.leaf = True
        self.key = [None for i in range(0,2*T-1)]
        self.child = [None for i in range(0,2*T)]

class BThree:
    def __init__(self):
        x = Node()
        self.root = x

    def BThreeSplit(self,x,i):
        z = Node()
        y = x.child[i]
        z.leaf = y.leaf
        z.n = T-1
        for j in range(1,T):
            z.key[j-1] = y.key[j+T-1]
        if not y.leaf :
            for j in range(1,T+1):
                z.child[j-1] = y.child[j+T-1]
        y.n = T-1
        for j in range(x.n,i,-1):
            x.child[j+1] = x.child[j]
        x.child[i+1] = z
        for j in range(x.n,i-1,-1):
            x.key[j] = x.key[j-1]
        x.key[i]=y.key[T-1]
        x.n = x.n+1

    def BThreeInsertNonFull(self,x,k):
        i = x.n-1
        if x.leaf:
            while i>0 and k < x.key[i]:
                x.key[i+1] = x.key[i]
                i = i-1
            x.key[i+1] = k
            x.n = x.n+1
        else:
            while i>=0 and k < x.key[i]:
                i = i-1
            i = i+1
            if x.child[i].n == 2*T-1:
                self.BThreeSplit(x,i)
                if k > x.key[i]:
                    i=i+1
            self.BThreeInsertNonFull(x.child[i],k)

    def ThreeInsert(self,k):
        r = self.root
        if r.n == 2*T-1:
            s = Node()
            s.leaf = False
            self.root = s
            s.child[0] = r
            self.BThreeSplit(s,0)
            self.BThreeInsertNonFull(s,k)
        else:
            self.BThreeInsertNonFull(r,k)

h = BThree()
h.ThreeInsert(1)
h.ThreeInsert(2)
h.ThreeInsert(3)
h.ThreeInsert(4)
h.ThreeInsert(5)
h.ThreeInsert(6)
h.ThreeInsert(7)
h.ThreeInsert(8)
h.ThreeInsert(9)
h.ThreeInsert(10)
print('Hello world')
print('Hello world')