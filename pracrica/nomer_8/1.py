def count_letter_o(full_name):

    parts = full_name.split()

    
    if len(parts) != 3:
        print("Введено не вірний формат повного імені.")
        return -1

    first_name = parts[1]

   
    count_o = first_name.count('о')

    return count_o


full_name = input("Введіть прізвище, ім’я та по-батькові: ")


count_o_in_name = count_letter_o(full_name)

if count_o_in_name != -1:
    print(f"Кількість букв 'о' в імені: {count_o_in_name}")
