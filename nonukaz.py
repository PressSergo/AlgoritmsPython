class list:
    def __init__(self,i):
        self.array = []
        for k in range(3):
            self.array.append([None for s in range(i)])
        self.free = []
        self.initFree()
        self.current = None

    def initFree(self):
        for i in range(len(self.array[0])):
            if self.array[0][i] == None:
                self.free.append(i)

    def add(self,s):
        self.current = self.free.pop()
        self.array[0][self.current] = s[0]
        self.array[1][self.current] = s[1]
        self.array[2][self.current] = s[2]
        self.current = s[0]
        self.initFree()

    def __str__(self):
        return "{}\n{}\n{}\n".format(self.array[0],self.array[1],self.array[2])

s = list(6)
print s
s.add((1,23,None))
s.add((3,56,1))
s.add((1,23,None))
print s