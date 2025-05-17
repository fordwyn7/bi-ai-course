def check(function):
    def wrapper(a, b):
        try:
            result = function(a, b)
        except ZeroDivisionError:
            result = "Denominator can't be zero"
        return result
    return wrapper

@check
def div(a, b):
    return a / b

try:
    a, b = map(int, input("Enter two numbers separated by space: ").split())
    print(div(a, b))
except ValueError:
    print("Invalid input. Please enter two integers.")