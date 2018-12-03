import copy
import random
class rash:
    const = 60

    def __init__(self,n):
        self.d = [random.randint(1,60) for i in range(n)]

    def getShedule(self):
        n = len(self.d)
        r = []
        s = []
        for i in range(0,n):
            for j in range(0,n-i-1):
                r.append(self.d[i])
                s.append([i,i.__str__()])
        n = len(r)
        for i in range(0,n-1):
            stack = copy.copy(s)
            for j in range(0,len(self.d)-1):
                temp = j+1
                sh = self.count(stack,j)
                for k in range(0,sh):
                    index = self.index(stack,j)
                    stack[index][0] = temp
                    jj = s.index(stack[index])
                    stack[index][1] +=temp.__str__()
                    s[jj] = stack[index]
                    stack.pop(index)
                    if temp != len(self.d)-1:
                        temp+=1
            geush = copy.copy(s)
            geu =[]
            for b in geush:
                lal = b[0]
                geu.append(copy.copy(b))
                for nn in range(0,len(self.d)-lal-2):
                    geu.append(copy.copy(b))
            s = copy.copy(geu)

        j = ''
        for i in s:
            str =''
            val = 0
            for j in i[1]:
                str+=j.__str__()
                val+=self.d[int(j)]
                if 50<=val<=60:
                    print("Project "+str+" value:{}".format(val))
                str+="+"

    def count(self ,s ,k):
        temp = 0
        for i in s:
            if i[0] == k:
                temp+=1
        return temp

    def index(self,s,k):
        temp = 0
        for i in s:
            if i[0] == k:
                return temp
            temp+=1
        return 0

s = rash(5)
s.getShedule()