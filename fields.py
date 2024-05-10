from errors import ValidationError


# Field: Базовий клас для полів запису.
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# Name: Клас для зберігання імені контакту. Обов'язкове поле.
class Name(Field):
    # реалізація класу - обов'язкове поле
	def __init__(self, name):
         super().__init__(name)


# Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
class Phone(Field):
    # реалізація класу - формат телефона 10 цифр
    def __init__(self, phone):
        super().__init__(phone)
    
    def validate(self):
        if len(self.value) != 10:
            raise ValidationError(f'{self.value} does not have 10 digits. Please, provide a valid number')
        else:
            return self.value