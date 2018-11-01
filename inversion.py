import random
class array:
    def __init__(self,i):
        self.a = [random.randint(1,50) for k in range(i)]
        self.lenght = len(self.a)
        self.inv = 0

    def __str__(self):
        return self.a.__str__()

    def merge(self,p,q,r):
        l = self.a[p:q+1]
        r = self.a[q+1:r+1]
        leftIndex = 0
        RightIndex = 0
        index = p
        while leftIndex < len(l) and RightIndex < len(r):
            if l[leftIndex] >= r[RightIndex]:
                self.a[index] = l[leftIndex]
                leftIndex = leftIndex+1
                self.inv = self.inv + 1
            else:
                self.a[index] = r[RightIndex]
                RightIndex = RightIndex+1
            index = index+1
        for i in range(leftIndex,len(l)):
            self.a[index] = l[i]
            index = index+1
        for i in range(RightIndex,len(r)):
            self.a[index] = r[i]
            index = index+1

    def mergeSort(self,p,r):
        if p<r:
            q = (p+r)/2
            self.mergeSort(p,q)
            self.mergeSort(q+1,r)
            self.merge(p,q,r)

    def sort(self):
        self.mergeSort(0,self.lenght)

    def inversion(self):
        print self.inv

a = array(20)
print a
a.sort()
print a
a.inversion()