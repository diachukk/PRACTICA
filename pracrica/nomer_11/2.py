import math

def t(x, y):
    return math.sqrt(x) + y

def p(x, y, z):
    return t(x, y) * z


x = 1
y = 1
z = 2

result_t = t(x, y)
print(f"Значення t({x}, {y}) = {result_t}")

result_p = p(x, y, z)
print(f"Значення p({x}, {y}, {z}) = {result_p}")
