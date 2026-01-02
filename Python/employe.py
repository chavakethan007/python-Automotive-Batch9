office={}
m=int(input("Enter How many managers there in the office: ?")) #here as per the question we are assigning 3
for i in range(m):
    manager=input("Enter Manager Name: ")
    office[manager]=[]
    e=int(input(f"How many Employees under {manager} manger: "))
    for i in range(e):
        employee=input(f"Enter Employee Name{i+1}: ")
        office[manager].append(employee)
        office[manager]=list(set(office[manager]))
    
print(office)