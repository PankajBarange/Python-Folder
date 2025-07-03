p=float(input("enter the principal:"))
r=float(input("enter the rate:"))
t=float(input("enter the time:"))
def simpleinterest(p,r,t):
    return (p*r*t)/100
result=simpleinterest(p,r,t)
print(f"simple interest is {result}")
