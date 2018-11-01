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

    def InorderThreeWalk(self,x):
        if x != None:
            self.InorderThreeWalk(x.left)
            print x.key
            self.InorderThreeWalk(x.right)

    def Searh(self,k):
        x = self.root
        while x != None and x.key != k:
            if x.key < k:
                x = x.right
            else: x = x.left
        return x

    def TreeInsert(self,z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else: x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else: y.right = z

    def TreeMinimum(self,x):
        while x.left != None:
            x = x.left
        return x

    def transplant(self,u,v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else: u.p.right = v
        if v != None:
            v.p = u.p

    def threeDelete(self,k):
        z = self.Searh(k)
        if z == None:
            print "Error found and delete"
            return
        if z.left == None:
            self.transplant(z,z.right)
        elif z.right == None:
            self.transplant(z,z.left)
        else:
            y = self.TreeMinimum(z.right)
            if y.p != z:
                self.transplant(y,y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z,y)
            y.left = z.left
            y.left.p=y
        print "Success delete"

k = three()
k.TreeInsert(Node(12))
k.TreeInsert(Node(21))
k.TreeInsert(Node(322))
k.TreeInsert(Node(98))
k.TreeInsert(Node(1))
k.TreeInsert(Node(2))
k.InorderThreeWalk(k.root)
k.threeDelete(98)
k.InorderThreeWalk(k.root)