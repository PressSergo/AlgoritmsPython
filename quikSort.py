import random

class QuickSort :
    def __init__(self,i):
        self.array = [random.randint(0,100) for k in range(i)]
        self.lenght = len(self.array)-1
    def __str__(self):
        return self.array.__str__()
    def sorted(self):
        self.quickSort(0,self.lenght)

    def quickSort(self,p,r):
        if p<r:
            q = self.partition(p,r)
            self.quickSort(p,q-1)
            self.quickSort(q+1,r)

    def partition(self,p,r):
        max = self.array[r]
        i = p-1
        for j in range(p,r+1):
            if max > self.array[j]:
                i = i+1
                self.array[i] , self.array[j] = self.array[j] , self.array[i]
        self.array[i+1], self.array[r] = self.array[r], self.array[i+1]
        return i+1


q = QuickSort(25)
print q
q.sorted()
print q