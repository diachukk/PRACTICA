import numpy as np

def transform_matrix(matrix):
 
    N, M = matrix.shape
    
   
    for i in range(N):
      
        max_element = np.max(matrix[i])
        min_element = np.min(matrix[i])
        
        
        max_index = np.argmax(matrix[i])
        min_index = np.argmin(matrix[i])
        
        
        matrix[i][0], matrix[i][max_index] = matrix[i][max_index], matrix[i][0]
        
       
        matrix[i][-1], matrix[i][min_index] = matrix[i][min_index], matrix[i][-1]

    return matrix


A = np.array([
    [3, 5, 1, 7],
    [2, 8, 6, 4],
    [9, 3, 2, 5]
])

print("Початкова матриця A:")
print(A)

transformed_matrix = transform_matrix(A)

print("\n Після обробки A:")
print(transformed_matrix)
