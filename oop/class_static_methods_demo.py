# Define the Calculator class
class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method - does not access class or instance attributes
    @staticmethod
    def add(a, b):
        return a + b

    # Class method - can access class-level attributes via the 'cls' parameter
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
