s=int(input("enter how many number you want to find for largest number: "))
a=[]
for i in range(s):
    n=int(input("Enter Number:"))
    a.append(n)
largestnumber=max(a)
print("largest Number is:",largestnumber)