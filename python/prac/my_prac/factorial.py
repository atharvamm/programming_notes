# Fibonacci sequence

def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)

fact = [1,1]
def dp(n):
    if n < len(fact) + 1:
        return fact[n]
    for j in range(2,n+1):
        fact.append(j*dp(j-1))
    return dp(n)
    


# Fibonacci seq 10th number and first 10 numbers
from time import time

start = time()
print(factorial(11))
# print("start",end=":")
# for i in range(1,11):
#     print(factorial(i),end = " ")
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

