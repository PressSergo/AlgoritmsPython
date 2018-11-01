class Node:
    def __init__(self,k):
        self.p = None
        self.left = None
        self.right = None
        self.key = k
    def __str__(self):
        return self.key

class three:
    def __init__(self):
        self.root = None

    def SymmetrialWalk(self,x):
        if x != None:
            self.SymmetrialWalk(x.left)
            print x.key
            self.SymmetrialWalk(x.right)

    def Searh(self,x,k):
        if x == None or x.key==k:
            return x
        elif x.key < k:
            return self.Searh(x.right,k)
        else: return self.Searh(x.left,k)

    def minimum(self,x):
        while x.left != None:
            x = x.left
        return x

    def insert(self,z):
        y = None
        x = self.root
        while x != None:
            y = x
            if x.key < z.key:
                x = x.right
            else: x = x.left
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else: y.right = z

    def transplate(self,u,v):
        if u==None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else: u.p.right = v
        if v != None:
            v.p = u.p

    def delete(self,k):
        z = self.Searh(self.root,k)
        if z.left == None:
            self.transplate(z,z.right)
        elif z.right == None:
            self.transplate(z,z.right)
        else:
            y = self.minimum(z.right)
            if z != y.p:
                self.transplate(y,y.right)
                y.right = z.right
                y.right.p = y
            y.p = z.p
            self.transplate(z,y)
            y.left = z.left
            y.left.p = y
        print "Success delete"

k = three()
k.insert(Node(12))
k.insert(Node(21))
k.insert(Node(322))
k.insert(Node(98))
k.insert(Node(1))
k.insert(Node(2))
k.SymmetrialWalk(k.root)
k.delete(322)
k.SymmetrialWalk(k.root)