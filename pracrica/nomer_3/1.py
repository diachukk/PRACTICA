import math

def compute_arccos_values(A, B, M):
    H = (B - A) / M
    
    arccos_values = []

    for i in range(1, M + 1):
        Xi = A + i * H
        result = math.acos(Xi) 
        arccos_values.append(result)
    
    return arccos_values


A = 0.5
B = 1.0
M = 10

values = compute_arccos_values(A, B, M)
print(f"Значення функції arccos(x) на відрізку ({A}, {B}]:")
for i, value in enumerate(values, 1):
    Xi = A + i * ((B - A) / M)
    print(f"arccos({Xi}) = {value}")
