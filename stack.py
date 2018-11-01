import random

class stack:
    def __init__(self,k):
        self.array = [0 for i in range(k)]
        self.lenght = len(self.array)
        self.top = 0
    def __str__(self):
        return self.array.__str__()
    def isEmpty(self):
        if self.top == 0:
            return True
        return False
    def push(self,i):
        if self.top != self.lenght:
            self.array[self.top] = i
            self.top=self.top+1
            return True
        return False
    def pop(self):
        if self.isEmpty():
            return False
        k = self.array[self.top-1]
        self.array[self.top-1] = 0
        self.top = self.top-1
        return k

k = stack(9)
print k
print k.isEmpty()
k.push(12)
k.push(23)
k.push(41)
print k
print k.isEmpty()
print k.pop()
print k