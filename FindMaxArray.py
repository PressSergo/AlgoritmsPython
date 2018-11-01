import random

class array :
    def __init__(self,i):
        self.a = [-22, -28, -37, 24]#[random.randint(-50,50) for k in range(i)]
        self.lenght = len(self.a)

    def __str__(self):
        return self.a.__str__()

    def FindCross(self,left,mid,right):
        leftSum = -100
        sum = 0
        for i in range(mid,left-1,-1):
            sum=sum+self.a[i]
            if sum > leftSum:
                leftSum = sum
        sum = 0
        rightSum = -100
        for i in range(mid+1,right+1):
            sum = sum+self.a[i]
            if sum > rightSum:
                rightSum = sum
        return (left,right,leftSum+rightSum)

    def findMax(self,p,r):
        if r-p<=5:
            return self.findstront(p,r)
        else:
            mid = (p+r)/2
            left = self.findMax(p,mid)
            right = self.findMax(mid+1,r)
            cross = self.FindCross(p,mid,r)
            if left[2] > right[2] and left[2]>cross[2]:
                return left
            elif right[2]>left[2] and right[2]>cross[2]:
                return right
            else:
                return cross

    def findstront(self,p,r):
        max = (0,0,-100)
        for i in range(r+1):
            sum = self.a[i]
            for j in range(i,r+1):
                if i == j:
                    sum =sum
                else:
                    sum = sum+self.a[j]
                if sum>max[2]:
                    max = (i,j,sum)
        return max

    def fineasy(self,p,r):
        max = -1000
        sum = self.a[0]
        for i in range(p,r-1):
            if sum+self.a[i+1] > 0 and sum+self.a[i+1] < self.a[i+1]:
                sum = self.a[i+1]
            elif sum+self.a[i+1] < 0 and sum+self.a[i+1] > self.a[i+1]:
                sum = self.a[i+1]
            else:
                sum = sum+self.a[i+1]
            if sum > max:
                max = sum
        return max

    def find(self):
        return self.findMax(0,self.lenght-1)

a = array(4)
print a
print a.find()
print a.fineasy(0,4)