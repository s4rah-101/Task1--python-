#prime number or not
def is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count +1
    if count==2:
        print("Prime number")
    else:
        print("Composite number")
n=int(input("Enter a number:"))
is_prime(n)

