import random

class sort:

    def __init__(self,i):
        self.a = [random.randint(0,70) for k in range(i)]
        self.lenght = len(self.a)

    def __str__(self):
        return self.a.__str__()

    def Merge(self,p,q,r):
        l = self.a[p:q+1]
        r = self.a[q+1:r+1]
        leftIndex = 0
        RightIndex = 0
        index = p
        while leftIndex < len(l) and RightIndex < len(r) :
            if l[leftIndex] >= r[RightIndex] :
                self.a[index] = l[leftIndex]
                leftIndex = leftIndex+1
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

    def MergeSort(self,p,r):
        if p<r:
            q = (p+r)/2
            self.MergeSort(p,q)
            self.MergeSort(q+1,r)
            self.Merge(p,q,r)

    def sort(self):
        self.MergeSort(0,self.lenght)

    def searhElement(self,key):
        left = 0
        right = self.lenght-1
        while left < right:
            s = self.a[left]+self.a[right]
            if s == key:
                return [self.a[left],self.a[right]]
            elif s > key:
                left = left+1
            else:
                right = right-1
        return "NotFound"


s = sort(5)
print s
s.sort()
print s
print s.searhElement(int(input("search:")))