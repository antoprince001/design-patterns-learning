class Person:
    def __init__(self, name, age, address, email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"


class PersonBuilder:
    def __init__(self):
        self.name = None
        self.age = None
        self.address = None
        self.email = None

    def with_name(self, name):
        self.name = name
        return self

    def with_age(self, age):
        self.age = age
        return self

    def with_address(self, address):
        self.address = address
        return self

    def with_email(self, email):
        self.email = email
        return self

    def build(self):
        if self.name is None:
            raise ValueError("Name is required")
        if self.age is None:
            raise ValueError("Age is required")
        if self.address is None:
            raise ValueError("Address is required")
        if self.email is None:
            raise ValueError("Email is required")
        return Person(self.name, self.age, self.address, self.email)


builder = PersonBuilder()
person = builder.with_name("John").with_age(30).with_address("123 Main St").with_email("john@example.com").build()

print(person)
