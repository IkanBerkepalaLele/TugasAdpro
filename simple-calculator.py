class Calculator:
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b
    
if __name__=="__main__":
    multiplyDivide = Calculator()
    print("Multiplication: ", multiplyDivide.multiply(10,5))
    print("Division: ", multiplyDivide.divide(10,5))

    