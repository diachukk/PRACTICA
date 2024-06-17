
num1 = int(input("Введіть перше ціле число: "))
num2 = int(input("Введіть друге ціле число: "))
num3 = int(input("Введіть третє ціле число: "))

max_negative = max(num1, num2, num3, default=None) if any(x < 0 for x in (num1, num2, num3)) else None

if max_negative is not None:
    print(f"Найбільше від'ємне число: {max_negative}")
else:
    print("Всі введені числа є додатніми.")
