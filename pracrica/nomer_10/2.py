class RejectionReason:
    def __init__(self, code, month, amount, hours):
        self.code = code  # Шифр причини відхилення
        self.month = month  # Місяць
        self.amount = amount  # Сума
        self.hours = hours  # Нормогодини

def read_input_data(filename):
    data = []
    with open(filename, 'r') as infile:
        for line in infile:
            parts = line.split()
            code = parts[0]
            month = parts[1]
            amount = float(parts[2])
            hours = float(parts[3])
            rejection_reason = RejectionReason(code, month, amount, hours)
            data.append(rejection_reason)
    return data

def print_data_to_screen(data):
    print("Шифр причини відхилення\tМісяць\tСума\tНормогодини")
    for reason in data:
        print(f"{reason.code}\t\t{reason.month}\t{reason.amount}\t{reason.hours}")

def print_data_to_file(data, filename):
    with open(filename, 'w') as outfile:
        outfile.write("Шифр причини відхилення\tМісяць\tСума\tНормогодини\n")
        for reason in data:
            outfile.write(f"{reason.code}\t\t{reason.month}\t{reason.amount}\t{reason.hours}\n")

def main():
    input_filename = "input.txt"
    output_filename = "output.txt"

    data = read_input_data(input_filename)
    print_data_to_screen(data)
    print_data_to_file(data, output_filename)

if __name__ == "__main__":
    main()
