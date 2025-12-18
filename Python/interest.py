import calci

def simpleinterest(p,r,t):
    interest=calci.multiplication(p,r)
    interest=calci.multiplication(interest,t)
    interest=calci.division(interest,100)
    return interest

p=int(input("Enter Principal amount: "))
r=int(input("Enter Rate Of Intrest: "))
t=int(input("Enter Time  period: "))

print('simple interest: ',simpleinterest(p,t,r))