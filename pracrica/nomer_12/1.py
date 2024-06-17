class ScheduleRecord:
    def __init__(self, pair_number, subject, teacher_surname, lesson_format):
        self.pair_number = pair_number
        self.subject = subject
        self.teacher_surname = teacher_surname
        self.lesson_format = lesson_format

    def __str__(self):
        return f"Пара {self.pair_number}: {self.subject} ({self.lesson_format}) - {self.teacher_surname}"


class ScheduleDatabase:
    def __init__(self):
        self.schedule_records = []

    def add_record(self, pair_number, subject, teacher_surname, lesson_format):
        """
        Додати запис до розкладу пар.
        """
        record = ScheduleRecord(pair_number, subject, teacher_surname, lesson_format)
        self.schedule_records.append(record)

    def get_records_by_pair_number(self, pair_number):
        """
        Отримати всі записи з розкладу для заданого номера пари.
        """
        return [record for record in self.schedule_records if record.pair_number == pair_number]

    def get_records_by_subject(self, subject):
        """
        Отримати всі записи з розкладу для заданого предмету.
        """
        return [record for record in self.schedule_records if record.subject == subject]

    def get_records_by_teacher_surname(self, teacher_surname):
        """
        Отримати всі записи з розкладу для заданого прізвища викладача.
        """
        return [record for record in self.schedule_records if record.teacher_surname == teacher_surname]

    def get_records_by_lesson_format(self, lesson_format):
        """
        Отримати всі записи з розкладу для заданої форми заняття.
        """
        return [record for record in self.schedule_records if record.lesson_format == lesson_format]

    def display_schedule(self):
        """
        Вивести весь розклад пар.
        """
        for record in self.schedule_records:
            print(record)


#Друга частина завдання

schedule_db = ScheduleDatabase()

schedule_db.add_record(1, "Математика", "Дзюба", "Лекція")
schedule_db.add_record(2, "Фізика", "Дячук", "Лабораторна робота")
schedule_db.add_record(1, "Історія", "Шкатуляк", "Практика")


print("Весь розклад:")
schedule_db.display_schedule()


print("\nРозклад для пари 1:")
for record in schedule_db.get_records_by_pair_number(1):
    print(record)

print("\nРозклад для предмету Математика:")
for record in schedule_db.get_records_by_subject("Математика"):
    print(record)
    
class SpecializedScheduleRecord(ScheduleRecord):
    def __init__(self, pair_number, subject, teacher_surname, lesson_format, classroom, duration):
        super().__init__(pair_number, subject, teacher_surname, lesson_format)
        self.classroom = classroom
        self.duration = duration

    def __str__(self):
        return f"Пара {self.pair_number}: {self.subject} ({self.lesson_format}) - {self.teacher_surname}. Аудиторія: {self.classroom}, тривалість: {self.duration} хв."

    def set_classroom(self, classroom):
        """
        Встановлює аудиторію для запису розкладу.
        """
        self.classroom = classroom

    def set_duration(self, duration):
        """
        Встановлює тривалість заняття для запису розкладу.
        """
        self.duration = duration



special_record = SpecializedScheduleRecord(3, "Англійська мова", "Сміт", "Лекція", "Ауд. 301", 90)

print(special_record)


special_record.set_classroom("Ауд. 302")
special_record.set_duration(120)


print("Оновлений запис розкладу:")
print(special_record)

