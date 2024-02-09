from collections import UserDict


class Field:
    def __init__(self, value):
        # Initialize the field with a value
        self.value = value

    def __str__(self):
        # Return the string representation of the field value
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) < 10:
            raise ValueError("Phone number has less than 10 digits")
        super().__init__(value)


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def find_phone(self, phone: str) -> Phone:
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError("Phone number not found")

    def __str__(self):
        # Return a string representation of the record
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    book = AddressBook()

    # Create a record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    # Create and add a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Print all records in the book
    for name, record in book.data.items():
        print(record)

    # Find and edit John's phone number
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)

    # Find a specific phone in John's record
    found_phone = john.find_phone("5555555555")
    print(f"{john.name.value}: {found_phone}")  # Output: 5555555555

    # Delete Jane's record
    book.delete("Jane")
