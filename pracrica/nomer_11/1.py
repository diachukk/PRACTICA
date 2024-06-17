import math

def calculate_sequence_sum():
    A = [1]  
    sum_elements = A[0] 
   
    for _ in range(4):
        next_A = math.sqrt(A[-1]) / (1 + math.sqrt(A[-1]))
        A.append(next_A)
        sum_elements += next_A
    
    return sum_elements

result = calculate_sequence_sum()
print(f"Сума перших 5 елементів ряду: {result}")
