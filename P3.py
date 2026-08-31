import math

x1, y1, x2, y2 = map(float, input("Enter x1, y1, x2, y2: ").split())

choice = int(input("Choose distance type (1 = Euclidean, 2 = Manhattan): "))

if choice == 1:
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"Euclidean distance is {distance:.5f}")
else:  # choice == 2
    distance = abs(x2 - x1) + abs(y2 - y1)
    print(f"Manhattan distance is {distance:.5f}")