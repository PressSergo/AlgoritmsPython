import random

class heap:
    def __init__(self,l):
        self.array = [16, 14, 29, 9, 40, -9, 30, 26, 31, 10]
        self.heapSize = l
        self.lenght = l-1

    def __str__(self):
        return self.array.__str__()

    def parent(self,i):
        return i/2

    def left(self,i):
        return 2*i+1

    def right(self,i):
        return 2*i+2

    def HeapSave(self,i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heapSize and self.array[l] > self.array[i]:
            large = l
        else: large = i
        if r < self.heapSize and self.array[r] > self.array[large]:
            large = r
        if large != i:
            [self.array[i],self.array[large]] = [self.array[large],self.array[i]]
            self.HeapSave(large)

    def BuilHeap(self):
        l = self.lenght/2
        for l in range(l,-1,-1):
            self.HeapSave(l)

    def HeapSorted(self):
        self.BuilHeap()
        for i in range(self.lenght,-1,-1):
            [self.array[0],self.array[i]] = [self.array[i],self.array[0]]
            self.heapSize = self.heapSize-1
            self.HeapSave(0)

i = heap(10)
print i
i.HeapSorted()
print i