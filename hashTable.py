import list

class hashTable :
    def __init__(self,k):
        self.table = [list.linkedlist() for i in range(k)]
        self.lengt = len(self.table)
    def display(self):
        str = "[ "
        for i in range(self.lengt):
            str+="["+self.table[i].display()+ "] "
        str+="]"
        print str
    def getHashMulti(self, key):
        return int(key%self.lengt)
    def getHashDiv(self,key):
        return int(self.lengt*((key*0.15)%1))
    def universHash(self,key):
        return int((2*key+3)%7)%self.lengt
    def insertHash(self,key):
        self.table[self.universHash(key)].add(key)
    def delete(self,key):
        self.table[self.universHash(key)].delete(key)
    def search(self,key):
        self.table[self.universHash(key)].search(key)

j = hashTable(5)
j.display()
j.insertHash(56)
j.insertHash(22)
j.insertHash(98)
j.insertHash(121)
j.insertHash(215)
j.insertHash(54)
j.insertHash(765)
j.insertHash(32)
j.insertHash(77)
j.display()
j.search(22)