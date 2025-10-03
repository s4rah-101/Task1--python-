n = int(input("Enter a number: "))
memo = {0: 1, 1: 1}

for i in range(2, n + 1):
    memo[i] = i * memo[i - 1]

print(memo[n])

