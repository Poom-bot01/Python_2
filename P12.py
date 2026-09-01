import math
a, b, c = map(float, input("Enter coefficients a, b, c: ").split())

if a == 0:
    print("This equation is not quadratic.")
else:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("This equation has complex roots.")
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The 1st root = {x1:.2f}")
        print(f"The 2nd root = {x2:.2f}")

#Finished