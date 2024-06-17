def product_between_zeros(arr):
    first_zero_index = -1
    second_zero_index = -1
    
  
    for i in range(len(arr)):
        if arr[i] == 0:
            if first_zero_index == -1:
                first_zero_index = i
            elif second_zero_index == -1:
                second_zero_index = i
                break
    
    if first_zero_index == -1 or second_zero_index == -1:
        print("У масиві менше двох нульових елементів.")
        return None
  
    product = 1
    for i in range(first_zero_index + 1, second_zero_index):
        product *= arr[i]
    
    return product

array = [2.5, 0, 3.2, 4.1, 0, 1.8, 2.0]
result = product_between_zeros(array)
if result is not None:
    print(f"Добуток елементів між першим і другим нульовими: {result}")
