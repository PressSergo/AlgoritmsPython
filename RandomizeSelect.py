import random

class Array :
    def __init__(self,i):
        self.array = [random.randint(0,99) for k in range(i)]
        self.lenght = len(self.array)-1

    def __str__(self):
        return self.array.__str__()

    def RandomizePartition(self,p,r):
        i = random.randint(p,r)
        self.array[i],self.array[r] = self.array[r],self.array[i]
        return self.partition(p,r)

    def partition(self,p,r):
        x = self.array[r]
        i = p-1
        for j in range(p,r+1):
            if self.array[j] < x :
                i = i+1
                self.array[j], self.array[i] = self.array[i], self.array[j]
        self.array[i+1], self.array[r] = self.array[r], self.array[i+1]
        return i+1

    def RandomizeSelect(self,p,r,i):
        if p == r:
            return self.array[p]
        q = self.RandomizePartition(p,r)
        k = q-p+1
        if i==k:
            return self.array[q]
        elif i < k:
            return self.RandomizeSelect(p,q-1,i)
        else :
            return self.RandomizeSelect(q+1,r,i-q)

    def select(self,i):
        return self.RandomizeSelect(0,self.lenght,i)

a = Array(20)
print a
print a.select(0)