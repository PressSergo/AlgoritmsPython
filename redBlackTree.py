class Color:
    RED = 0
    BLACK = 1

class Node:
    def __init__(self,key,color = Color.RED):
        self.l = None
        self.r = None
        self.p = None
        self.k = key
        self.c = color

    def __str__(self):
        return str(self.k)


class redBlackTree:

    Nil = Node(None,Color.BLACK)

    def __init__(self):
        self.root = self.Nil
        self.Nil.p = self.Nil
        self.Nil.l = self.Nil
        self.Nil.r = self.Nil

    def leftRotate(self,x):
        y = x.r
        x.r = y.l
        if y.l != self.Nil:
            y.l.p = x
        y.p = x.p
        if x.p == self.Nil:
            self.root = y
        elif x == x.p.l:
            x.p.l = y
        else:
            x.p.r = y
        y.l = x
        x.p = y

    def rightRotate(self,x):
        y = x.l
        x.l = y.r
        if y.r != self.Nil:
            y.r.p = x
        if x.p == self.Nil:
            self.root = y
        elif x == x.p.l:
            x.p.l = y
        else: x.p.r = y
        y.r = x
        x.p = y

    def insert(self,z):
        y = self.Nil
        x = self.root
        while x != self.Nil:
            y = x
            if x.k < z.k:
                x = x.r
            else:
                x = x.l
        z.p = y
        if y == self.Nil:
            self.root = z
        elif y.k < z.k:
            y.r = z
        else:
            y.l = z
        z.l = self.Nil
        z.r = self.Nil
        self.FixUp(z)

    def FixUp(self,z):
        while z.p.c == Color.RED:
            if z.p == z.p.p.l:
                y = z.p.p.r
                if y.c == Color.RED:
                    z.p.c = Color.BLACK
                    y.c = Color.BLACK
                    z.p.p.c=Color.RED
                    z = z.p.p
                else:
                    if z == z.p.r:
                        z = z.p
                        self.leftRotate(z)
                    z.p.c=Color.BLACK
                    z.p.p.c=Color.RED
                    self.rightRotate(z.p.p)
            else:
                y = z.p.p.l
                if y.c == Color.RED:
                    y.c = Color.BLACK
                    z.p.c = Color.BLACK
                    z.p.p.c = Color.RED
                    z = z.p.p
                else:
                    if z == z.p.l:
                        z = z.p
                        self.rightRotate(z)
                    z.p.c = Color.BLACK
                    z.p.p.c = Color.RED
                    self.leftRotate(z.p.p)
        self.root.c=Color.BLACK

    def diplay(self,z):
        if z.k != None:
            self.diplay(z.l)
            print z
            self.diplay(z.r)

    def transplant(self,u,v):
        if u.p == self.Nil:
            self.root = v
        elif u == u.p.l:
            u.p.l = v
        else: u.p.r = v
        v.p = u.p

    def searh(self,k):
        x = self.root
        while x!=self.Nil and x.k != k:
            if k<x.k:
                x = x.l
            else:
                x = x.r
        return x

    def minimum(self,x):
        while x.l !=self.Nil:
            x = x.left
        return x

    def delete(self,k):
        z = self.searh(k)
        y = z
        yColor = y.c
        if z.l == self.Nil:
            x = z.r
            self.transplant(z,z.r)
        elif z.r == self.Nil:
            x = z.l
            self.transplant(z,z.l)
        else:
            y = self.minimum(z.r)
            yColor = y.c
            x = y.r
            if y.p == z:
                x.p = y
            else:
                self.transplant(y,y.r)
                y.r = z.r
                y.r.p = y
            self.transplant(z,y)
            y.l = z.l
            y.l.p = y
            y.c = z.c
        if yColor == Color.BLACK:
            self.fixUpDelete(x)

    def fixUpDelete(self,x):
        while x != self.root and x.c == Color.BLACK:
            if x == x.p.l:
                w = x.p.r
                if w.c == Color.RED:
                    w.c = Color.BLACK
                    x.p.c = Color.RED
                    self.leftRotate(x.p)
                    w = x.p.r
                if w.l.c == Color.BLACK and w.r.c == Color.BLACK:
                    w.c = Color.RED
                    x=x.p
                elif w.r.c == Color.BLACK:
                    w.l.c = Color.BLACK
                    w.c = Color.RED
                    self.rightRotate(w)
                    w = x.p.r
                w.c = x.p.c
                x.p.c = Color.BLACK
                w.r.c = Color.BLACK
                self.leftRotate(x.p)
                x = self.root
            else:
                if x == x.p.r:
                    w = x.p.l
                    if w.c == Color.RED:
                        w.c = Color.BLACK
                        x.p.c = Color.RED
                        self.rightRotate(x.p)
                        w = x.p.l
                    if w.r.c == Color.BLACK and w.l.c == Color.BLACK:
                        w.c = Color.RED
                        x = x.p
                    elif w.l.c == Color.BLACK:
                        w.r.c = Color.BLACK
                        w.c = Color.RED
                        self.leftRotate(w)
                        w = x.p.l
                    w.c = x.p.c
                    x.p.c = Color.BLACK
                    w.l.c = Color.BLACK
                    self.rightRotate(x.p)
                    x = self.root
        x.c = Color.BLACK

r = redBlackTree()
for i in range(12):
    k = Node(i)
    k.p = redBlackTree.Nil
    k.l = redBlackTree.Nil
    k.r = redBlackTree.Nil
    r.insert(k)
r.diplay(r.root)
r.delete(5)
r.diplay(r.root)