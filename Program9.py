#matrix multiplication 
r1=int(input('Enter the no of rows of Matrix A:'))
c1=int(input('Enter the no of columns of Matrix A:'))
print('Enter the elements row by row for Matrix A:')
A=[]
for i in range(r1):
    row=list(map(int,input().split()))
    A.append(row)
r2=int(input('Enter the no of rows of Matrix B:'))
c2=int(input('Enter the no of columns of Matrix B:'))
B=[]
for i in range(r2):
    row=list(map(int,input().split()))
    B.append(row)
if c1!=r2:
    print("Matrix Multiplication is not possible")
else:
    result= [[0 for i in range(c2)] for j in range(r1)]
for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            result[i][j] += A[i][k] * B[k][j]
print("Resultant Matrix:")
for row in result:
    print(row)



