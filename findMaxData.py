import random
import itertools

class Matrix:
    def __init__(self,n,m):
        self.A = [[random.randint(1,5) for i in range(m)] for j in range(n)]
        self.n = n
        self.m = m

    def find(self):
        self.B = [[0 for i in range(0,self.m)] for j in range(0,self.n)]
        for i in range(0,self.n):
            self.B[i][0] = self.A[i][0]
            for j in range(1,self.m):
                self.B[i][j] = self.B[i][j-1]+self.A[i][j]
        print("tes")
        for i in range(1,self.n):
            for j in range(0,self.m):
                self.B[i][j] = self.B[i-1][j]+self.B[i][j]

        row =[]
        for i in range(0,self.n):
            row.append(sum(self.A[i]))

        col=[]
        for j in range(0,self.m):
            suma = 0
            for i in range(0,self.n):
                suma+=self.A[i][j]
            col.append(suma)
        print("hel")
        #Сгенерировать перестановки , так как мы сможем вычеркивать любую строку и любой столбец
        #Методы динамического программирования , использовались чтобы найти сумму по столбце и по строчке
        #А также сумму матриц , в итоге вычитаем сумму столбцов , имитируя вычеркивание


stuff = [1,2,3]
for sub in itertools.combinations(stuff,):
    print(sub)