class Message:
    def __init__(self):
        self.str1 = raw_input("text1:")
        self.str2 = raw_input("text2:")
        self.EncodeStr1 = []
        self.KeyForText2 = []

    def getText(self):
        print "text1: "+self.str1
        print "text2: "+self.str2

    def getEncodeText(self):
        print ("Encodtext: " +' '.join(str(i) for i in self.EncodeStr1))
        print ("KeyText2: " +' '.join(str(i) for i in self.KeyForText2))

    def transcript(self):
        t = Transcript(self.KeyForText2)
        t.GetText1(self.EncodeStr1)

class Transcript:
    def __init__(self,k):
        self.cod1 = Encode1()
        self.cod2 = Encode2()
        self.key = k

    def GetText1(self,msg):
        temp = 0
        message=[]
        for j in range(len(msg)):
            for i in range(101, 173, 1):
                if self.cod1.PositionFunc(chr(i), 0) == msg[temp]:
                    message.append(chr(i))
                    temp = temp + 1
                    break
                elif self.cod1.PositionFunc(' ', 0) == msg[temp]:
                    message.append(' ')
                    temp = temp + 1
                    break
        print("Text1:"+''.join(message))




class Collision:
    def __init__(self,m):
        self.cod1 = Encode1()
        self.cod2 = Encode2()
        self.msg = m

    def EncodeText(self):
        for i in self.msg.str1:
            self.msg.EncodeStr1.append(self.cod1.PositionFunc(i,0))

    def CreateKey(self):
        temp = 0
        code = 20
        for j in self.msg.str2:
            while True:
                if self.cod2.PositionFunc(j,code) == self.msg.EncodeStr1[temp]:
                    self.msg.KeyForText2.append(code)
                    code = 20
                    temp = temp+1
                    break
                code = code+1


class Encode1:
    def PositionFunc(self,i,j):
        h = ord(i) + j
        return h % 85

class Encode2:
    def PositionFunc(self,i,j):
        h = ord(i)+j
        return h%55


m = Message()
c = Collision(m)
c.EncodeText()
c.CreateKey()
m.getText()
m.getEncodeText()
m.transcript()