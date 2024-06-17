def process_array(numbers):
    if len(numbers) == 0:
        print("Масив порожній.")
        return
    
    if len(numbers) % 2 != 0: 
        sorted_numbers = sorted(numbers)
        print("Відсортований масив:", sorted_numbers)
    else:  
        max_num = max(numbers)
        min_num = min(numbers)
        print(f"Максимум: {max_num}, Мінімум: {min_num}")


numbers = [3, 1, 4, 1, 5, 9]  
process_array(numbers)
