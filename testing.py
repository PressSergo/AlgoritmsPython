import random
from math import ceil

class Array :
    def __init__(self,i):
        self.array = [random.randint(0,70) for k in range(i)]
        self.lenght = len(self.array)

    def __str__(self):
        return self.array.__str__()

    def search(self,key):
        for i in range(self.lenght):
            if self.array[i] == key:
                return i
        return "not found"

    def InsertSort(self,r):
        if r > 0 :
            self.InsertSort(r-1)
            max = self.array[r]
            i = r-1
            while i >=0 and self.array[i] > max :
                self.array[i+1] = self.array[i]
                i=i-1
            self.array[i+1] = max

    def sort(self):
        self.InsertSort(self.lenght-1)

    def insertSortFor(self):
        for i in range(1,self.lenght):
            j = i-1
            max = self.array[i]
            for j in range(i-1,-1,-1):
                if self.array[j] > max and j >= 0 :
                    self.array[j+1] = self.array[j]
                    j=j-1
                else : break
            self.array[j+1] = max

    def BinarySearch(self,key):
        p = 0
        r = self.lenght-1
        while p<=r :
            q = (p + r) / 2
            if self.array[q] == key:
                return q
            elif self.array[q]>key:
                r = q-1
            else: p = q+1
        return "not found"




a = Array(20)
#print a
#b = int(input("key:"))
#print a.search(b)
#a.sort()
a.insertSortFor()
print a
while True:
    print a.BinarySearch(int(input("key:")))


