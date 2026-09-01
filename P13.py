x = float(input("Enter x [-10,10]): "))

if x < -10 or x > 10:
    print("Error, out of range.")
elif x <= -6 or x >= 6:
    y = 0
    print(f"(x, y) = ({x:.2f}, {y:.2f})")
elif -6 < x < -2:
    y = x + 6
    print(f"(x, y) = ({x:.2f}, {y:.2f})")
elif -2 <= x <= 2:
    y = 4
    print(f"(x, y) = ({x:.2f}, {y:.2f})")
else:  # 2 < x < 6
    y = -x + 6
    print(f"(x, y) = ({x:.2f}, {y:.2f})")

#Finished