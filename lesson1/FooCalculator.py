import calculator as c


class FooCalculator:

    # empty constructor
    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m, n)

    def divide(self, m, n):
        return c.divide(m, n)

    def multiply(self, m, n):
        return c.multiply(m, n)

    def sub(self, m, n):
        return c.sub(m, n)


calculator = FooCalculator()

print("10/5= ", calculator.divide(10, 5))
print("5+5", calculator.sum(5, 5))
print("10/3= ", calculator.divide(10, 3))
print("5+1", calculator.sum(5, 1))
print("3/1= ", calculator.divide(3, 1))
print("0+0", calculator.sum(0, 0))
print("10/5= ", calculator.divide(10, 5))
print("3+3", calculator.sum(3, 3))
print("-3+3", calculator.sum(-3, 3))
print("-3-3", calculator.sum(-3, -3))
print("-10/5= ", calculator.divide(-10, 5))
print("10/-5= ", calculator.divide(10, -5))
print("-3-3=", calculator.sum(-3, 3))
print("-3-(-3)=", calculator.sum(-3, -3))
print("3-3=", calculator.sum(3, -3))
print("10-3=", calculator.sum(10, -3))
print("3* -3=", calculator.multiply(3, -3))
print("-3 * -3=", calculator.multiply(-3, -3))
