class abcd:

    def getSum(self,*args):
        return sum(args)

c1 = abcd()
print(c1.getSum(10,20))
print(c1.getSum(10,20,30,40,50,60,70,80,90,100))

