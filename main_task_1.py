import pickle
from typing import Dict

class AddressBook:
    def __init__(self):
        """Ініціалізує нову адресну книгу з порожнім словником контактів."""
        self.contacts: Dict[str, str] = {}

    def add_contact(self, name: str, address: str) -> None:
        """Додає новий контакт до адресної книги.
        
        Args:
            name (str): Ім'я контакту.
            address (str): Адреса контакту.
        """
        self.contacts[name] = address

    def get_contact(self, name: str) -> str:
        """Повертає адресу контакту за його ім'ям.
        
        Args:
            name (str): Ім'я контакту.
        
        Returns:
            str: Адреса контакту або повідомлення, що контакт не знайдено.
        """
        return self.contacts.get(name, "Contact not found")

def save_data(book: AddressBook, filename: str = "addressbook.pkl") -> None:
    """Зберігає адресну книгу у файл.
    
    Args:
        book (AddressBook): Адресна книга для збереження.
        filename (str, optional): Ім'я файлу для збереження. За замовчуванням "addressbook.pkl".
    """
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename: str = "addressbook.pkl") -> AddressBook:
    """Завантажує адресну книгу з файлу.
    
    Args:
        filename (str, optional): Ім'я файлу для завантаження. За замовчуванням "addressbook.pkl".
    
    Returns:
        AddressBook: Завантажена адресна книга або нова адресна книга, якщо файл не знайдено.
    """
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  

def main() -> None:
    """Головна функція програми, яка керує основним циклом."""
    print("Адресна книга.\n-Ви можете додавати нові контакти, отримувати адреси існуючих контактів та зберігати дані між сеансами.")
    
    book = load_data()


    while True:
        command = input("Enter command (add, get, exit - вийти): ").strip().lower()
        if command == "add":
            name = input("Enter name: ")
            address = input("Enter address: ")
            book.add_contact(name, address)
        elif command == "get":
            name = input("Enter name: ")
            print(book.get_contact(name))
        elif command == "exit":
            save_data(book)
            print("Address book saved. Exiting program.")
            break
        else:
            print("Available commands: add, get, exit")

if __name__ == "__main__":
    main()