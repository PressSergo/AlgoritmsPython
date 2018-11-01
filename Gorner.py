import random
class Gorner:
    def __init__(self,i):
        self.a = [random.randint(1,10) for k in range(i+1)]
        self.lenght = len(self.a)
    def __str__(self):
        return self.a.__str__()
    def gorner(self,x):
        y = 0
        for i in range(self.lenght-1,-1,-1):
            y = self.a[i]+x*y
        return y

s = Gorner(10)
print s
print s.gorner(2)
