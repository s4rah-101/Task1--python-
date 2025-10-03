#fibonacci series
n=int(input("Enter the no of terms:"))
x,y=0,1
print("Fibonacci series:")
for i in range(n):
    print(x,end="")

    x,y=y,x+y
