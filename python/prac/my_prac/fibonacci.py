# Fibonacci sequence

def fibonacci(n):
    if n in [1,2]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib_seq = [1,1]
def dp(n):
    if n < len(fib_seq) + 1:
        return fib_seq[n - 1]
    for j in range(3,n+1):
        fib_seq.append(dp(j-1) + dp(j-2))
    return dp(n)
    


# Fibonacci seq 10th number and first 10 numbers
from time import time

start = time()
print(fibonacci(11))
# print("start",end=":")
# for i in range(1,11):
#     print(fibonacci(i),end = " ")
# print("::end")
end = time()
print(end - start)

start = time()
print(dp(11))
# print("start",end=":")
# for i in range(1,11):
#     print(dp(i),end = " ")
# print("::end")
end = time()
print(end - start)

