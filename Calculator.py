class Calculator:
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b
    
if __name__=="__main__":
    calc = Calculator()
    print("Multiplication: ", calc.multiply(10,5))
    print("Division: ", calc.divide(10,5))