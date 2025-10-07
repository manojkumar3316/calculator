# calculator.py

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b == 0:
            return "Error! Division by zero."
        return self.a / self.b

    def floordiv(self):
        if self.b == 0:
            return "Error! Division by zero."
        return self.a // self.b

    def mod(self):
        if self.b == 0:
            return "Error! Modulus by zero."
        return self.a % self.b


if __name__ == "__main__":
    val1 = int(input("Enter the first number: "))
    val2 = int(input("Enter the second number: "))
    calc = Calculator(val1, val2)

    print("Choose the operation: +  -  *  /  //  %")
    symbol = input("Enter operator: ")

    if symbol == "+":
        print("Result:", calc.add())
    elif symbol == "-":
        print("Result:", calc.sub())
    elif symbol == "*":
        print("Result:", calc.mul())
    elif symbol == "/":
        print("Result:", calc.div())
    elif symbol == "//":
        print("Result:", calc.floordiv())
    elif symbol == "%":
        print("Result:", calc.mod())
    else:
        print("Invalid operator!")
