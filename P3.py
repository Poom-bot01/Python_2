import math

x1, y1, x2, y2 = map(float, input("Enter x1, y1, x2, y2: ").split())

print("Please choose your distance:")
print("        1 Euclidean distance")
print("        2 Manhattan distance")
choice = int(input("Your choice: "))
if choice == 1:
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"Euclidean distance = {distance:.5f}")
else:  # choice == 2
    distance = abs(x2 - x1) + abs(y2 - y1)
    print(f"Manhattan distance = {distance:.5f}")

#Finished