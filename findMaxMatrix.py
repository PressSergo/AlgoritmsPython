import random

class Matrix:
    def __init__(self,n,m):
        self.arr = [[random.randint(0,1) for i in range(m)] for j in range(n)]
        for i in range(0,n):
            print (self.arr[i])

    def find(self,n,m):
        self.B = [[0 for i in range(m)] for j in range(n)]
        for i in range(0,m):
            if self.arr[0][i] == 0:
                self.B[0][i] = 0
            else:
                self.B[0][i] = 1

        for j in range(0,n):
            if self.arr[j][0] == 0:
                self.B[j][0] = 0
            else:
                self.B[j][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                if self.arr[i][j] == 0:
                    self.B[i][j] = 0
                else:
                    self.B[i][j] = min(self.B[i-1][j],self.B[i][j-1],self.B[i-1][j-1])+1

        print('________________')
        for i in range(0,n):
            print (self.B[i])


    def findVerySlov(self):
        max = -1
        temp = 0
        for i in range(0,len(self.arr)):
            for j in range(0,len(self.arr[0])):
                for k in range(0,min(len(self.arr[0])-j,len(self.arr[0])-i)):
                    BoolTemp = False
                    if self.arr[i][j] != 0:
                        for i1 in range(i,i+k):
                            if BoolTemp: break
                            for i2 in range(j,j+k):
                                if self.arr[i1][i2] == 0:
                                    BoolTemp = True
                                    break
                            temp = i1-i+1
                        if max < temp:
                            max = temp
                    else:
                        break
        print (max)





m = Matrix(300,300)
m.find(300,300)
print("__________")
m.findVerySlov()