class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def calculate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'subtract':
            return self.a - self.b
        elif operation == 'multiply':
            return self.a * self.b
        elif operation == 'divide':
            if self.b == 0:
                return "Cannot divide by zero"
            return self.a / self.b
        else:
            return "Invalid operation"

# Example usage:
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (add/subtract/multiply/divide): ")

calc = Calculator(a, b)
print("Result:", calc.calculate(op))
