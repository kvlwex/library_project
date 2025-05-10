# Entry point for the client application
from prompt_toolkit import prompt
import requests

BASE_URL = "http://127.0.0.1:5000"

def show_menu():
    print("\n📚 Library Management")
    print("1. Показать список книг")
    print("2. Взять книгу")
    print("3. Вернуть книгу")
    print("0. Выход")

def list_books():
    r = requests.get(f"{BASE_URL}/books")
    for book in r.json():
        print(f"{book['id']} - {book['title']} ({book['author']}) | Доступно: {book['available_copies']}")

def borrow_book():
    user_id = prompt("Введите ID пользователя: ")
    book_id = prompt("Введите ID книги: ")
    r = requests.post(f"{BASE_URL}/borrow", json={"user_id": int(user_id), "book_id": int(book_id)})
    print(r.json())

def return_book():
    user_id = prompt("Введите ID пользователя: ")
    book_id = prompt("Введите ID книги: ")
    r = requests.post(f"{BASE_URL}/return", json={"user_id": int(user_id), "book_id": int(book_id)})
    print(r.json())

def main():
    while True:
        show_menu()
        choice = prompt("Выберите действие: ")
        if choice == "1":
            list_books()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
