# Swap without using temp variable

# Logic: The right side is a tuple therfore it works

a = 5 
b = 10

print(a,b)
a,b = b,a
print(a,b)