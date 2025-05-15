def convert_cel_to_far(C):
    in_Fahrenheit = C * 9 / 5 + 32
    return "%.2f" % in_Fahrenheit


def convert_far_to_cel(F):
    in_Celsius = (F - 32) * 5 / 9
    return "%.2f" % in_Celsius

F = float(input("Enter a temperature in degrees F: "))
print(f"{int(F)} degrees F = {convert_far_to_cel(F)} degrees C")


C = float(input("Enter a temperature in degrees C: "))
print(f"{int(C)} degrees C = {convert_cel_to_far(C)} degrees F")
