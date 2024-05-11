from fields import Name, Phone
from errors import ValidationError


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
        try:
            new_phone.validate()
            self.phones.append(new_phone)
        except ValidationError as e:
            print(f"Error! {e}")
        else:
            print(f"{phone} has 10 digits and is added to {self.name}'s phones list")


    def wrong_phone_alert(self, phone):
        print(f'User {self.name} has no phone {phone}.\nPlease, choose one of the existing phone numbers:\n{chr(10).join(p.value for p in self.phones)}')


# - Пошук телефону (об'єкту Phone) - find_phone
    def find_phone(self, searched_phone):
        try:
            found_phone = list(filter(lambda phone: phone.value == searched_phone, self.phones))[0]
            return found_phone
        except IndexError:
            return self.wrong_phone_alert(searched_phone)


# - Редагування телефонів edit_phone
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        return self.wrong_phone_alert(old_phone)


# - Видалення телефонів remove_phone
    def remove_phone(self, old_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
                return
        return self.wrong_phone_alert(old_phone)


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
