class node:
    def __init__(self,k = None):
        self.nextl = None
        self.prev = None
        self.key = k

    def __str__(self):
        return "{}".format(self.key)

class linkedlist:
    def __init__(self):
        self.head = node(None)
    def display(self):
        temp = self.head
        s = " "
        while temp.key != None:
            s+= str(temp)+" "
            temp = temp.nextl
        return s
    def add(self,i):
        s = node(i)
        if self.head != None:
            self.head.prev = s
        s.nextl = self.head
        self.head = s

    def search(self,key):
        temp = self.head
        while temp.key != None:
            if temp.key == key:
                print "search: "+ str(temp.prev)+" "+str(temp.nextl)
                return temp
            temp = temp.nextl
        return None

    def delete(self,key):
        temp = self.search(key)
        if temp==None:
            return False
        if temp.prev != None:
            temp.prev.nextl = temp.nextl
        else: self.head = temp.nextl
        if temp.nextl != None:
            temp.nextl.prev = temp.prev

#j = linkedlist()
#j.add(10)
#j.add(21)
#j.add(657)
#j.add(321)
#j.add(123)
#j.add(545)
#j.display()
#j.search(int(input()))
#j.delete(int(input()))
#j.display()