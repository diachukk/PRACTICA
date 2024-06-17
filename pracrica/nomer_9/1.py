
class Appointment:
    def __init__(self, day, month, year, client_name):
        self.day = day
        self.month = month
        self.year = year
        self.client_name = client_name


def process_appointments(appointments):
   
    unique_dates = set((appointment.day, appointment.month, appointment.year) for appointment in appointments)

    if not unique_dates:
        print("Немає записів на прийом")
    else:
        print(f"Всього записано на {len(unique_dates)} різних дат:")
        for date in unique_dates:
            print(f"{date[0]}.{date[1]}.{date[2]}")


def main():
    appointments = [
        Appointment(12, 6, 2024, "Петров"),
        Appointment(15, 6, 2024, "Іванов"),
        Appointment(12, 6, 2024, "Сидоров"),
        Appointment(20, 6, 2024, "Петров"),
        Appointment(12, 6, 2024, "Коваленко"),
        Appointment(15, 6, 2024, "Петров"),
        Appointment(20, 6, 2024, "Іванов"),
    ]

    
    process_appointments(appointments)

if __name__ == "__main__":
    main()
