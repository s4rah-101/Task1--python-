w1=input("Enter the first word")
w2=input('Enter the second word')
isanagram=sorted(w1.lower())==sorted(w2.lower())
print(isanagram)
