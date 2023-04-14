from collections import UserDict
from functools import wraps


class Field:
    def __init__(self, value):
        self.value = value

    def __setitem__(self):
        pass

    def __getter__(self):
        pass

    def __str__(self):
        return str(self.value)


class Record(Field):
    def __init__(self, name, phone=None, date=None):
        self.name = name
        self.phone = phone
        self.phones = [phone] if phone else []
        self.days = date

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, name, phone):
        self.phones[name] = phone

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def days_to_birthday(self, date):
        pass


class Birthday:
    def __setitem__(self):
        pass


class Phone(Field):
    def __setitem__(self):
        pass


class Name(Field):
    pass


class AddressBook(UserDict):
    def add_record(self, record):
        name = record.name.value
        self.data[name] = record

    def iterator(self):
        pass


contacts = AddressBook()


def input_error(func):
    @wraps(func)
    def wrapper(*args):
        try:
            return func(*args)
        except (KeyError, ValueError, IndexError) as exc:
            result = f"An error occurred: {str(exc)}"
            return result
    return wrapper


def help(*args):
    return """"hello", відповідає у консоль "How can I help you?"
"add ...". За цією командою бот зберігає у пам'яті новий контакт.
"change ..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту.
"phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту.
"show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
"good bye", "close", "exit" по будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!"."""


def hello(*args):
    return 'Hello, how can I help you?'


@input_error
def add_func(*args):
    obj = args[0].split()
    name = Name(obj[0])
    phone = Phone(obj[1])
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return f'U add contact with name : {name} and his number is : {phone}'


@input_error
def change_contacts_dict(*args):
    obj = args[0].split()
    name = Name(obj[0])
    phone = Phone(obj[1])
    record = contacts[name.value]
    record.change_phone(0, phone)
    return f'You have changed the number to this one: {phone} in the contact with the name: {name}'


@input_error
def phone_func(*args):
    name = args[0]
    if name in contacts.data:
        for key in contacts.data.keys():
            record = contacts.data[key]
            if name == key:
                return f"{name}: {', '.join(str(phone) for phone in record.phones)}"
    raise KeyError


def show_all_func(*args):
    list = []
    if len(contacts.data) == 0:
        return "list of contacts is empty..."
    for key in contacts.data.keys():
        record = contacts.data[key]
        list.append(
            f"{key}: {', '.join(str(phone) for phone in record.phones)}")
    return "\n".join([f"{item}"for item in list])


def no_command(*args):
    return "Unknown command, try again."


OPERATION = {
    'hello': hello,
    'add': add_func,
    'change': change_contacts_dict,
    'phone': phone_func,
    'show': show_all_func,
    'help': help
}

END_WORDS = ['good bye', 'close', 'exit']


def handle_command(user_input):
    for word, command in OPERATION.items():
        if user_input.startswith(word):
            return command, user_input.replace(word, '').strip()
    return no_command, None


def main():
    print(help())
    while True:
        user_input = input("Write what u wont from bot >>> ").lower()
        if user_input in END_WORDS:
            print("Good bye!")
            break
        command, data = handle_command(user_input)
        print(command(data))


if __name__ == '__main__':
    main()
