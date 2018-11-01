import random

class array :
    def __init__(self,i):
        self.a = [random.randint(-10,50) for k in range(i)]
        self.lenght = len(self.a)
        self.heapsize = self.lenght
    def parent(self,i):
        return i/2
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def __str__(self):
        return self.a.__str__()
    def heapify(self,i):
        l = self.left(i)
        r = self.right(i)
        if l<self.heapsize and self.a[l] > self.a[i]:
            largest = l
        else:
            largest = i
        if r<self.heapsize and self.a[r]> self.a[largest]:
            largest = r
        if largest != i :
            self.a[i],self.a[largest] = self.a[largest],self.a[i]
            self.heapify(largest)
    def buildHeapyfy(self):
        mid = (self.lenght-1)/2
        for i in range(mid,-1,-1):
            self.heapify(i)

    def heapySort(self):
        self.buildHeapyfy()
        for i in range(self.lenght-1,-1,-1):
            self.a[i],self.a[0] = self.a[0],self.a[i]
            self.heapsize = self.heapsize-1
            self.heapify(0)
    def getMax(self):
        return self.a[0]
    def insert(self,i):
        self.a.append(i)
        self.lenght = self.lenght+1
        self.a[0],self.a[self.lenght-1] = self.a[self.lenght-1],self.a[0]
        self.heapify(0)
    def increaseKey(self,i,key):
        if key < self.a[i]:
            return "error key is less"
        self.a[i] = key
        while i > 0 and self.a[self.parent(i)] < self.a[i]:
            self.a[self.parent(i)],self.a[i] = self.a[i], self.a[self.parent(i)]
            i = self.parent(i)

s = array(10)
print s
s.buildHeapyfy()
print s
s.increaseKey(3,44)
print s
print s.getMax()