import random

class Select:
    def __init__(self,n):
        self.F = [random.randint(2, n * 2) for i in range(n)]
        self.F = sorted(self.F)
        self.S = [random.randint(0, self.F[i]) for i in range(0, n)]

    def __str__(self):
        for i in range(len(self.F)):
            print("process {}: start {} , finish {}".format(i, self.S[i], self.F[i]))
        return ''

    def DinSelect(self):
        n = len(self.S)
        C = [[0 for i in range(n)] for j in range(n)]
        l = 2 # initial step
        for i in range(0, n - l + 1):
            j = i + l - 1
            if self.F[i] <= self.S[j]:
                C[i][j] = 0
            else:
                C[i][j] = -1

        for l in range(3,n+1):
            for i in range(0,n-l+1):
                j = i+l-1
                q = -1
                if self.F[i] <= self.S[j]:
                    q = 1
                for k in range(i+1,j):
                    q = max(q,C[i][k]+C[k][j]+1)
                C[i][j] = q

        print("Optimal Size: {}".format(C[0][n-1]+2))


    def select(self):
        A = [0]
        m = 0
        for i in range(1,len(self.S)):
            if self.S[i]>=self.F[m]:
                A.append(i)
                m = i
        for i in range(len(A)):
            print("process {}: start {} , finish {}".format(A[i], self.S[A[i]], self.F[A[i]]))
        print('')

s = Select(40)
print(s)
s.select()
s.DinSelect()