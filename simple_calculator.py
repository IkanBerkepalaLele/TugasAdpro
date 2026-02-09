class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a/b
    def modulo(self, a, b):
        return a % b
    def power(self, a, b):
        return a ** b

if __name__ == "main":
    test = Calculator()
    print("Addition:", test.add(10,5))
    print("Subtraction:", test.subtract(10,5))
    print("Multiplication:", test.multiply(10,5))
    print("Division:", test.divide(10,5))
    print("Modulo:", test.modulo(10,5))
    print("Power:", test.power(10,5))