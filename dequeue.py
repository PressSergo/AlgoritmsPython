
class dequeue:
    def __init__(self,k):
        self.array = [0 for i in range(k)]
        self.lenght = len(self.array)
        self.top = 0
        self.tail = 0
    def __str__(self):
        return self.array.__str__()
    def isEmpty(self):
        if self.top == self.tail:
            return True
        return False
    def Enqueue(self,i):
        if self.tail == self.lenght:
            self.tail = self.tail % self.lenght
        self.array[self.tail] = i
        self.tail = self.tail+1
    def dequeue(self):
        if self.top == self.lenght:
            self.top = self.top%self.lenght
        x = self.array[self.top]
        self.array[self.top] = 0
        self.top = self.top+1
        return x
    def headdequeue(self):
        k = self.array[self.tail-1]
        self.array[self.tail-1] = 0
        self.tail = self.tail-1
        return k



k = dequeue(4)
print k
print k.isEmpty()
k.Enqueue(12)
k.Enqueue(23)
k.Enqueue(41)
print k
print k.isEmpty()
print k.dequeue()
print k.headdequeue()
print k
k.Enqueue(101)
print k