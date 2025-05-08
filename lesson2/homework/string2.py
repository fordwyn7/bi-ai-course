car_names = ["Lamborghini", "Maserati", "Bugatti"]

txt = "LMaasleitbtui"

for car in car_names:
    is_car = True
    for ch in car:
        if not ch in txt:
            is_car = False
    if is_car:
        print(car, sep=" ")
else:
    print("No car name found :(")