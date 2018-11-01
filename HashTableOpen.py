
class hash:
    def __init__(self,k):
        self.table = [None for i in range(k)]
        self.lenght = len(self.table)
    def hash(self,key):
        return int(key%self.lenght)
    def secondHash(self,key):
        return int(((5*key+12)%21)%self.lenght)
    def linearSearh(self,key,i):
        return int((self.hash(key)+i)%self.lenght)
    def cubSearh(self,key,i):
        return int((self.hash(key)+5*i+2*i^2)%self.lenght)
    def doubleSearh(self,key,i):
        return int((self.hash(key)+i*self.secondHash(key))%self.lenght)
    def insert(self,key):
        i = 0
        while True:
            j = self.doubleSearh(key,i)
            if self.table[j] == None:
                self.table[j] = key
                print "Succesful"
                return
            i = i+1
            if i >=self.lenght:
                print "Memory not found"
                return
    def search(self,key):
        i = 0
        while True:
            j = self.doubleSearh(key,i)
            if self.table[j] == key:
                print "Succesful"
                return
            i = i+1
            if i >= self.lenght or self.table[j] == None:
                print "Not found"
                return
    def __str__(self):
        return self.table.__str__()


y = hash(20)
print y
y.insert(54)
y.insert(231)
y.insert(44)
y.insert(87)
y.insert(291)
y.insert(901)
y.insert(322)
y.insert(1222)
y.insert(0)
y.insert(984)
y.insert(129)
y.insert(419)
print y
y.search(int(input("key:")))
y.search(int(input("key:")))
y.search(int(input("key:")))