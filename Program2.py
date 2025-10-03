#functions in lists 
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
list2=list.copy()
newlist=[x**2 for x in list2]
print(newlist)