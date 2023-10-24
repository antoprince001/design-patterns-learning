class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.init_singleton()
        return cls._instance

    def init_singleton(self):
        # Initialize the singleton instance here
        self.value = 0

# Creating instances
singleton1 = Singleton()
singleton2 = Singleton()

# Both instances will refer to the same object
print(singleton1 is singleton2)  # Output: True

# Modifying the value in one instance affects the other
singleton1.value = 42
print(singleton2.value)  # Output: 42
