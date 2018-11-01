import random

class array:
    def __init__(self,i):
        self.array = [random.randint(0,50) for k in range(i)]
        self.lenght = len(self.array)
    def __str__(self):
        return self.array.__str__()

    def mergeSort(self,p,r):
        if r-p > 5:
            q = (p+r)/2
            self.mergeSort(p,q)
            self.mergeSort(q,r)
            self.merge(p,q,r)
        else :
            self.insertSort(p,r)



    def merge(self,p,q,r):
        L = self.array[p:q]
        R = self.array[q:r]
        i = 0
        j = 0
        c = p
        while i < len(L) and j < len(R):
            if L[i] >= R[j]:
                self.array[c] = L[i]
                i=i+1
            else:
                self.array[c] = R[j]
                j=j+1
            c = c+1
        for l in range(i,len(L)):
            self.array[c] = L[l]
            c=c+1
        for r in range(j,len(R)):
            self.array[c] = R[r]
            c=c+1

    def sort(self):
        self.mergeSort(0,self.lenght)

    def insertSort(self,p,q):
        for i in range(p+1,q):
            j = i-1
            max = self.array[i]
            while j >= p and self.array[j] < max:
                self.array[j+1] = self.array[j]
                j=j-1
            self.array[j+1] = max

a = array(24)
print a
a.sort()
print a