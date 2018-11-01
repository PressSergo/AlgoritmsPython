class node:
    def __init__(self,k = None):
        self.next = None
        self.prev = None
        self.key = k

    def __str__(self):
        return "{}".format(self.key)

class linkedlist:
    def __init__(self):
        self.NIL = node(None)
        self.NIL.prev = self.NIL
        self.NIL.next = self.NIL
    def display(self):
        temp = self.NIL.next
        s = "list "
        while temp != self.NIL:
            s+= str(temp)+" "
            temp = temp.next
        print s

    def insert(self,x):
        s = node(x)
        s.next = self.NIL.next
        self.NIL.next.prev = s
        self.NIL.next = s
        s.prev = self.NIL

j = linkedlist()
j.insert(93)
j.insert(12)
j.insert(44)
j.insert(432)
j.insert(777)
j.display()