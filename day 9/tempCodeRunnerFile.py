class abcd:

    def getSum(self, a, b):
        return a + b

    def getSum(self, a, b, c):
        return a + b + c
    
c1 = abcd()
print(c1.getSum(10, 20))  # This will call the first getSum method
print(c1.getSum(10, 20, 30))  # This will call the second getSum method
print(c1.getSum(10, 20, 30, 40))  # This will raise an error since there is no method defined for four parameters
