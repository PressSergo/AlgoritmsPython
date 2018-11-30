class rash:
    const = 60

    def __init__(self):
        self.d = [36,9,10,45,15]

    def getShedule(self):
        n = len(self.d)
        r = [0 for i in range(n)]
        p = [0 for i in range(n)]
        r[0] = self.d[0]
        for j in range(1,n):
            q = 0
            for i in range(1,j+1):
                if q <= self.d[i] + r[j-i] :
                    q = self.d[i] + r[j - i]
                    p[j] = i
            r[j] = q
        print(r)

g = rash()
g.getShedule()