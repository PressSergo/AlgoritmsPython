class fib:
    def __init__(self,n):
        self.kes = [-1 for i in range(n+1)]
        self.len = n
        self.kes[0] = 0
        self.kes[1] = 1

    def getFibRec(self,n):
        if n == 1 or n == 2:
            return 1
        return self.getFibRec(n-2)+self.getFibRec(n-1)

    def down_getFib(self,n):
        if self.kes[n] >= 0:
            return self.kes[n]
        q = self.down_getFib(n-1)+self.down_getFib(n-2)
        self.kes[n] = q
        return self.kes[n]

    def up_method_Fib(self,n):
        kes = [-1 for i in range(n+1)]
        kes[0] = 0
        kes[1] = 1
        for j in range(2,n+1):
            q = -1
            for i in range(2,j+1):
                q = kes[i-1]+kes[i-2]
            kes[j] = q
        return kes[n]


f = fib(1000)
print (f.down_getFib(f.len))
print(f.up_method_Fib(f.len))
print(f.getFibRec(f.len))