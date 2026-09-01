weight = float(input("Enter package weight: "))
if (weight < 0):
    print("Invalid weight. Bye.")
elif (weight <= 5):
    weight_total = weight * 20
    print(f"Total delivery cost is {weight_total:.2f} Baht")
elif (weight <= 10):
    weight_total = 5 * 20 + (weight - 5) * 30
    print(f"Total delivery cost is {weight_total:.2f} Baht")
elif (weight >= 11):
    weight_total = 5 * 20 + 5 * 30 + (weight - 10) * 40
    print(f"Total delivery cost is {weight_total:.2f} Baht")

#Finished