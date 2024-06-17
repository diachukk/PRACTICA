def calculate_statistics(numbers):
    if len(numbers) == 0:
        print("Масив порожній.")
        return
    
    positive_sum = sum(num for num in numbers if num > 0)
    positive_count = sum(1 for num in numbers if num > 0)
    negative_product = 1
    negative_count = 0
    
    for num in numbers:
        if num < 0:
            negative_product *= num
            negative_count += 1
    
    if negative_count > 0:
        average_negative = negative_product / negative_count
    else:
        average_negative = 0
    
    print(f"Сума додатніх елементів: {positive_sum}")
    print(f"Кількість додатніх елементів: {positive_count}")
    print(f"Добуток від'ємних елементів: {negative_product}")
    print(f"Кількість від'ємних елементів: {negative_count}")
    print(f"Середнє арифметичне від'ємних елементів: {average_negative}")


numbers = [3, -1, 4, -1, 5, 9]  
calculate_statistics(numbers)
