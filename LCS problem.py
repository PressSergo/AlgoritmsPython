class LCS :
    def __init__(self):
        self.A = "ABCBDAB"
        self.B = "BDCABA"
        self.str =''

    def LCS(self):
        n = len(self.A)
        m = len(self.B)
        c = [[0 for i in range(m+1)] for j in range(n+1)]
        b = [[0 for i in range(0,m+1)] for j in range(0,n+1)]
        for i in range(0,n+1):
            c[i][0] = 0
        for j in range(0,m+1):
            c[0][j] = 0

        for i in range(1,n+1):
            for j in range(1,m+1):
                if self.A[i-1] == self.B[j-1]:
                    c[i][j] = c[i-1][j-1]+1
                    b[i][j] = "\\"
                elif c[i-1][j]>=c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = '|'
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = '--'


        for i in range(0,n+1):
            print(c[i])

        print ("_____________")
        for i in range(0,n+1):
            print(b[i])

        self.printLCS(b,self.A,len(self.A),len(self.B))

        print(self.str)

    def printLCS(self,b,A,i,j):
        if i ==0 or j == 0:
            return
        if b[i][j] == "\\":
            self.printLCS(b,A,i-1,j-1)
            self.str+=A[i-1]
        elif b[i][j] == "|":
            self.printLCS(b, A, i - 1, j)
        else:
            self.printLCS( b, A, i, j-1)

h = LCS()
h.LCS()