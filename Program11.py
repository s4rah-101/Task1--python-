s1=set(map(int,input("Enter numbers Set1(space seperated):")))
s2=set(map(int,input("Enter numbers Set2(space seperated):")))

print("Union of the sets is", s1 | s2)
print("Intersection of the sets is", s1 & s2)
print("Difference of the sets(Set1-Set2) is", s1 - s2)
print("Difference of the sets(Set2-Set1) is", s2-s1)
