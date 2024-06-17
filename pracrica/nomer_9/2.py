class Book:
    def __init__(self, author_lastname, title, year):
        self.author_lastname = author_lastname
        self.title = title
        self.year = year

def find_book_by_title(books, title):
    for book in books:
        if book.title == title:
            return book
    return None


def main():
    
    books = [
        Book("Турчин", "Програмування", 2020),
        Book("Петров", "Історія комп'ютерів", 2018),
        Book("Іванов", "Інформатика", 2015),
        Book("Сидоренко", "Математика для інформатиків", 2017),
        Book("Сидоров", "Алгоритми", 2019),
        Book("Коваленко", "Інформатика", 2021),
    ]

   
    book_to_find = "Інформатика"
    found_book = find_book_by_title(books, book_to_find)

    if found_book:
        print(f"Книга '{book_to_find}' знайдена:")
        print(f"Автор: {found_book.author_lastname}")
        print(f"Рік видання: {found_book.year}")
    else:
        print(f"Книга '{book_to_find}' не знайдена")

if __name__ == "__main__":
    main()
