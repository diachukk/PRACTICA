import math

def calculate_Q(b, x):
    bx = b * x
    if bx < 1 and b == 1.5:
        return bx - math.log10(bx)
    elif bx == 1:
        return 1
    elif bx > 1:
        return bx + math.log10(bx)

# Задані значення b і x з варіанту
b = 1.5
x_values = [0.1, 0.5, 0.9, 1, 1.1, 1.5, 2]

# Вивід заголовка таблиці
print(f"{'b\\x':<8}", end="")
for x in x_values:
    print(f"{x:<10}", end="")
print()

# Вивід значень функції Q у вигляді таблиці
for x in x_values:
    print(f"{b:<8.1f}", end="")
    for x_val in x_values:
        result = calculate_Q(b, x_val)
        print(f"{result:<10.4f}", end="")
    print()
