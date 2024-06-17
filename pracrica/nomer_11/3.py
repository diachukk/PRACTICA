def ects_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 82 and score <= 89:
        return "B"
    elif score >= 74 and score <= 81:
        return "C"
    elif score >= 64 and score <= 73:
        return "D"
    elif score >= 60 and score <= 63:
        return "E"
    elif score >= 35 and score <= 59:
        return "FX"
    elif score >= 0 and score <= 34:
        return "F"
    else:
        return "Неправильно введені дані"

score = int(input("Введіть суму балів, зароблених студентом: "))
result = ects_grade(score)
print(f"Оцінка за шкалою ECTS: {result}")
