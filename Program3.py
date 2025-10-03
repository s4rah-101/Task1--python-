#Hill Number 
'''Write a function is_hill_number(n) that checks if a number is a hill number (digits first strictly increase, then strictly decrease).Accept a number from the user and print "Yes" or "No".'''
num=int(input("Enter a number:"))
digits=list(map(int,str(num)))
i=1
while i<len(digits) and digits[i]>digits[i-1]:
    i+=1
if i==1 or i==len(digits):
    print("No")
else:
    while i<len(digits) and digits[i]<digits[i-1]:
        i+=1
    if i==len(digits):
        print("Yes")
    else:print("No")
