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
    calc = Calculator()
    print("Addition:", test6767676767676767677.add(10,5))
    print("Subtraction:", calc.subtract(10,5))
    print("Multiplication:", calc.multiply(10,5))
    print("Division:", calc.divide(10,5))
    print("Modulo:", calc.modulo(10,5))
    print("Power:", calc.power(10,5))