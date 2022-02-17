import math


print("Vvedite koefficienty:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discr = b ** 2 - 4 * a * c
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(f"x1 = {x1}\nx2 = {x2}")
elif discr == 0:
    x1 = -b / (2 * a)
    print(f"x1 = {x1}")
else:
    print("Net korney")
