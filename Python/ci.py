import calci
def compoundinterest(p,r,t):
    try:
        interest=float(calci.division(r,100))
        interest=float(calci.add(1,interest))
        interest=float(calci.power(interest,t))
        interest=int(calci.multiplication(interest,p))
        return interest
    except TypeError:
        return "Error: Invalid Data is used"
    except ZeroDivisionError:
        return "Error: Division with zero is not allowed"
    except  Exception as e:
        return "Unexpected Error"

"""try:
    p=int(input("Enter Principal amount: "))
    r=int(input("Enter Rate Of Intrest: "))
    t=int(input("Enter Time  period: "))
except ValueError:
    print("Please Enter Numeric Values only")

print('compound interest:',compoundinterest(p,r,t))"""