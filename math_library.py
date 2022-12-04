import math

a = 14
b = 21

# 최대공약수(Greatest Common Divisor)
print(math.gcd(a, b))

# 최소공배수(Least Common Multiple)
def lcm(a, b):
    return a * b // math.gcd(a, b)


print(math.lcm(a, b))
print(lcm(a, b))
