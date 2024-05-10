from collections import UserDict
from errors import SearchError


# AddressBook: Клас для зберігання та управління записами.
# книга контактів містить записи {'name': ['phone', 'phone']}
class AddressBook(UserDict):


# - Додавання записів - add_record, який додає запис до self.data.
    def add_record(self, record):
        self.data[record.name.value] = record # ----------- Handle Error if bad value!
    
    def search(self, name):
        if self.data.get(name) == None:
            raise SearchError(f'There is no user with name {name}')


# - Пошук записів за іменем - find, який знаходить запис за ім'ям
    def find(self, name):
        try:
            self.search(name)
            return self.data.get(name)
        except SearchError as e:
            print(f"Error! {e}")


# - Видалення записів за іменем - delete, який видаляє запис за ім'ям
    def delete(self, name):
        try:
            self.search(name)
            del self.data[name]
        except SearchError as e:
            print(f"Error! {e}")            
