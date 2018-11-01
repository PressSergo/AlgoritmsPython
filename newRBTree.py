class color:
    RED = 0
    BLACK = 1

class node:
    def __init__(self,k):
        self.l = None
        self.r = None
        self.p = None
        self.k = k
        self.c = color.RED

class rbTree:
    NIL = node(None)

    def __init__(self):
        self.root = self.NIL
        self.NIL.p = self.NIL
        self.NIL.l = self.NIL
        self.NIL.r = self.NIL
        self.NIL.c = color.BLACK

    def min(self,z):
        while z.l != self.NIL:
            z = z.l
        return z

    def max(self,z):
        while z.r != self.NIL:
            z = z.r
        return z

    def symByPass(self,z):
        if z != self.NIL:
            self.symByPass(z.l)
            print z.k
            self.symByPass(z.r)

    def search(self,key):
        x = self.root
        while x != self.NIL and x.k != key:
            if key < x.k:
                x = x.l
            else:
                x = x.r
        return x

    def leftRotate(self,x):
        y = x.r
        x.r = y.l
        if x.r != self.NIL:
            x.r.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x ==x.p.l:
            y.p.l = y
        else:
            y.p.r = y
        y.l = x
        y.l.p = y

    def rightRotate(self,x):
        y = x.l
        x.l = y.r
        if x.l != self.NIL:
            x.l.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.l:
            y.p.l = y
        else:
            y.p.r = y
        y.r = x
        y.r.p = y


    def insert(self,z):
        x = self.root
        y = self.NIL
        while x != self.NIL:
            y = x
            if z.k < x.k:
                x = x.l
            else:
                x = x.r
        z.p = y
        if y == self.NIL:
            self.root = z
            z.p = self.NIL
        elif z.k < y.k:
            y.l = z
        else:
            y.r = z
        z.l = self.NIL
        z.r = self.NIL
        z.c = color.RED
        self.FixUp(z)

    def FixUp(self,z):
        while z.p.c == color.RED:
            if z.p == z.p.p.l:
                y = z.p.p.r
                if y.c == color.RED:
                    z.p.c = color.BLACK
                    y.c = color.BLACK
                    z.p.p.c = color.RED
                    z = z.p.p
                else:
                    if z == z.p.r:
                        z = z.p
                        self.leftRotate(z)
                    z.p.c = color.BLACK
                    z.p.p.c = color.RED
                    self.rightRotate(z.p.p)
            else:
                y = z.p.p.l
                if y.c == color.RED:
                    y.c = color.BLACK
                    z.p.c = color.BLACK
                    z.p.p.c = color.RED
                    z = z.p.p
                else:
                    if z == z.p.l:
                        z = z.p
                        self.rightRotate(z)
                    z.p.c = color.BLACK
                    z.p.p.c = color.RED
                    self.leftRotate(z.p.p)
        self.root.c = color.BLACK

    def transplant(self,u,v):
        if u.p == self.NIL:
            self.root = v
        elif u == u.p.l:
            u.p.l = v
        else:
            u.p.r = v
        v.p = u.p

    def delete(self,k):
        z = self.search(k)
        y = z
        OrigColorY = y.c
        if z.l == self.NIL:
            x = z.r
            self.transplant(z,z.r)
        elif z.r == self.NIL:
            x = z.l
            self.transplant(z,z.l)
        else:
            y = self.min(z.r)
            OrigColorY = y.c
            x = y.r
            if y.p == z:
                x.p = y
            else:
                self.transplant(y,y.r)
                y.r = z.r
                y.r.p = y
            self.transplant(z,y)
            y.l = z.l
            y.c = z.c
            y.l.p = y
        if OrigColorY == color.BLACK:
            self.FixDelete(x)

    def FixDelete(self,x):
        while x != self.root and x.c == color.BLACK:
            if x == x.p.l:
                w = x.p.r
                if w.c == color.RED:
                    w.c = color.BLACK
                    x.p.c = color.RED
                    self.leftRotate(x.p)
                    w = x.p.r
                if w.l.c == color.BLACK and w.r.c == color.BLACK:
                    w.c = color.RED
                    x = x.p
                elif w.r.c == color.BLACK:
                    w.c = color.RED
                    w.l.c = color.BLACK
                    self.leftRotate(w)
                    w = x.p.r
                w.c = w.p.c
                w.p.c = color.BLACK
                w.r.c = color.BLACK
                self.leftRotate(x.p)
                x = self.root
            else:
                w = x.p.l
                if w.c == color.RED:
                    w.p.c = color.RED
                    w.c = color.BLACK
                    self.rightRotate(w.p)
                    w = x.p.l
                if w.l.c == color.BLACK and w.r.c == color.BLACK:
                    w.c = color.RED
                    x = w.p
                elif w.l.c == color.BLACK:
                    w.c = color.RED
                    w.r.c = color.BLACK
                    self.leftRotate(w)
                    w = x.p.l
                w.c = w.p.c
                w.p.c = color.BLACK
                w.l.c = color.BLACK
                self.rightRotate(w.p)
                x = self.root
        x.c = color.BLACK


r = rbTree()
for i in range(12):
    r.insert(node(i))
r.symByPass(r.root)
r.delete(5)
r.symByPass(r.root)