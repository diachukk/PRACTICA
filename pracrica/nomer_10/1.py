
class Book:
    def __init__(self, author_lastname, title, year):
        self.author_lastname = author_lastname
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.author_lastname}, {self.title}, {self.year}"



def input_book_data():
    author_lastname = input("Введіть прізвище автора: ")
    title = input("Введіть назву книги: ")
    year = input("Введіть рік видання: ")
    return author_lastname, title, year



def write_to_file(data):
    with open('books.txt', 'a', encoding='utf-8') as file:
        file.write(data + '\n')



def main():
    author_lastname, title, year = input_book_data()
    
    book = Book(author_lastname, title, year)

    print("Введені дані:")
    print(book)

    
    write_to_file(str(book))
    print("Дані записано у файл 'books.txt'")

if __name__ == "__main__":
    main()
