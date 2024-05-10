from collections import UserDict


# Field: Базовий клас для полів запису.
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# Name: Клас для зберігання імені контакту. Обов'язкове поле.
class Name(Field):
    # реалізація класу - обов'язкове поле
	pass


# Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
class Phone(Field):
    # реалізація класу - формат телефона 10 цифр
    def __init__(self, phone):
        super().__init__(phone)
    
    # ------------------------------------------------------ Handle wrong length Error!
    def validate(self):
        if len(self.value) == 10:
            return self.value
        else:
            print(f'{self.value} does not have 10 digits')


# Record: Клас для зберігання інформації про контакт. Кожен запис містить набір полів, включаючи ім'я та список телефонів.
class Record:
    def __init__(self, name):
# - зберігання об'єкта Name в окремому атрибуті
        self.name = Name(name)
# - зберігання списку об'єктів Phone в окремому атрибуті
        self.phones = []


# - Додавання телефонів add_phone
    def add_phone(self, phone):
        new_phone = Phone(phone)
        is_valid = new_phone.validate()
        if is_valid:
            self.phones.append(new_phone)


# - Пошук телефону (об'єкту Phone) - find_phone
    # ----------------------------------------- Handle IndexError if searched_phone is not found! or add if any()
    def find_phone(self, searched_phone):
        return list(filter(lambda phone: phone.value == searched_phone, self.phones))[0]


# - Редагування телефонів edit_phone
    # -------------------------------- reuse find function in edit function instead of repeating! 
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        print('There is no such phone')


# - Видалення телефонів remove_phone
    def remove_phone(self, old_phone):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones.remove(self.phones[index])
                return
        print('There is no such phone')


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


# AddressBook: Клас для зберігання та управління записами.
# книга контактів містить записи {'name': ['phone', 'phone']}
class AddressBook(UserDict):


# - Додавання записів - add_record, який додає запис до self.data.
    def add_record(self, record):
        self.data[record.name.value] = record # ----------- Handle Error if bad value!
    

# - Пошук записів за іменем - find, який знаходить запис за ім'ям
    def find(self, name):
        return self.data.get(name) # ---------------------- Handle Error if not found!


# - Видалення записів за іменем - delete, який видаляє запис за ім'ям
    def delete(self, name):
        if self.data.get(name):
            del self.data[name]
        else:
            print('There is no such name') # ---------------------- Nicer handle Error if not found!


# ---------------------    TESTS    ---------------------------- 

if __name__ == '__main__':

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # # Видалення запису Jane
    book.delete("Jane")

    # # Видалення 1 з телефонів запису John
    john_record.remove_phone('5555555555')

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)