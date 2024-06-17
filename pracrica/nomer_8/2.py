def find_parentheses_positions(s):
    n = len(s)
    open_positions = []
    close_positions = []

    for i in range(n):
        if s[i] == '(':
            open_positions.append(i + 1) 
        elif s[i] == ')':
            close_positions.append(i + 1) 

    if len(open_positions) == 0 and len(close_positions) == 0:
        print("Дужок у рядку немає")
    else:
        if len(open_positions) > 0:
            print(f"Відкриті дужки на позиціях: {', '.join(map(str, open_positions))}")
        else:
            print("Відкритих дужок немає")

        if len(close_positions) > 0:
            print(f"Закриті дужки на позиціях: {', '.join(map(str, close_positions))}")
        else:
            print("Закритих дужок немає")

# Приклад використання:
input_string = "(abc(def)ghi)"
find_parentheses_positions(input_string)
