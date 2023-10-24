import copy


# Define a prototype class
class Prototype:
    def __init__(self):
        self._data = {}

    def set_data(self, key, value):
        self._data[key] = value

    def get_data(self):
        return self._data

    def clone(self):
        # Use the copy module to perform a deep copy of the object
        return copy.deepcopy(self)


# Create an instance of the prototype
prototype = Prototype()
prototype.set_data("name", "John")
prototype.set_data("age", 30)

# Clone the prototype to create a new object
new_object = prototype.clone()
new_object.set_data("age", 35)

# Display the data in the original prototype and the new object
print("Original Prototype Data:", prototype.get_data())
print("New Object Data:", new_object.get_data())
