import random

class array:
    def __init__(self,i):
        self.a = [random.randint(-10,50) for k in range(i)]
        self.lenght = len(self.a)
        self.heapsize = self.lenght
        self.dim = 3

    def __str__(self):
        return self.a.__str__()

    def child(self,i):
        child = []
        for k in range(1,self.dim+1):
            child.append(int(3*i+k))
        return child

    def getParent(self,i):
        if i%self.dim == 0:
            return i/self.dim+1
        else:
            return i/self.dim

    def findMax(self,s,r):
        max = s
        for i in range(s+1,r+1):
            if self.a[i]>self.a[max]:
                max = i
        return max

    def heapify(self,i):
        child = self.child(i)
        for k in range(self.dim):
            if child[k] >= self.heapsize:
                return
        max = self.findMax(child[0],child[self.dim-1])
        if self.a[i]>self.a[max]:
            max = i
        if max!= i:
            self.a[i],self.a[max] = self.a[max],self.a[i]
            self.heapify(max)

    def buildHeap(self):
        mid = (self.lenght-1)/3
        for i in range(mid,-1,-1):
            self.heapify(i)

    def sort(self):
        self.buildHeap()
        for i in range(self.lenght-1,-1,-1):
            self.a[0],self.a[i] = self.a[i],self.a[0]
            self.heapsize = self.heapsize-1
            self.heapify(0)




a = array(10)
print a
a.buildHeap()
print a
a.sort()
print a