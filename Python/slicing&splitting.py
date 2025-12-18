mystring='abcdef ghijkl'
sub1=mystring[0:6]
sub2=mystring[7: ]
sub3=mystring[ :5]
sub4=mystring[10]
sub5=mystring[-5]
print(sub1)
print(sub2)
print(sub3)
print(sub4)
print(sub5)

if "a" in mystring:
    print("a is there")

word=mystring.split(" ")
print(word)
print(mystring.upper())
print(mystring.lower())

mystring=mystring+'m'
print(mystring)
