import random

class cSort :
    count = 40
    def __init__(self,i):
        self.array = [random.randint(0,self.count) for i in range(i)]
        self.lenght = len(self.array)

    def __str__(self):
        return self.array.__str__()

    def Sort(self,k):
        B = [0 for i in range(len(self.array))]
        C = [0 for i in range(k)]
        for j in self.array:
            C[j] = C[j]+1
        for i in range(1,k):
            C[i] = C[i]+C[i-1]
        for i in range(len(self.array)-1,-1,-1):
            B[C[self.array[i]]-1] = self.array[i]
            C[self.array[i]] = C[self.array[i]]-1
        return B

    def Dsort(self):
        return self.Sort(self.count+1)

s = cSort(20)
print s
print s.Dsort()