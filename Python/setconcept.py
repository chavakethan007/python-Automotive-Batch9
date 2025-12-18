myset={'apple','pomegrante','banana','apple',True,1,2,False,0}
mylist=['a','b']
print(myset)
#true=1
#false=0
empty_set=set()
empty_dict={}
print(type(empty_set))
'''mylist.add(10)'''
'''mylist.discard(10)'''
myset.update(mylist)
count=len(myset)
print(count)

for fruit in myset:
    print(fruit)
