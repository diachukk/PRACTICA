def find_max_index(arr):
    if not arr:
        return None
    
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i
    
    return max_index


array = [3.5, 1.2, 6.7, 2.1, 4.8]
max_index = find_max_index(array)
if max_index is not None:
    print(f"Номер максимального елемента масиву: {max_index}")
else:
    print("Масив порожній.")
