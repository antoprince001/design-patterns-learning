# Old System with an incompatible interface
class OldSystem:
    def operation(self):
        return "Old System Operation"


# New System with a different interface
class NewSystem:
    def new_operation(self):
        return "New System Operation"


# Adapter class that adapts OldSystem to the NewSystem interface
class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def new_operation(self):
        return self.old_system.operation()


# Client code that uses the NewSystem interface
def client_code(system):
    return system.new_operation()


# Using the Adapter to make OldSystem work with the NewSystem interface
old_system = OldSystem()
adapter = Adapter(old_system)
result = client_code(adapter)

print("Client: Using OldSystem via the Adapter")
print(result)
