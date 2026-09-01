height = float(input("Your height (cm): "))
if (height >= 120):
    print("Yes! You can play.")
elif(height < 120 ):
    height_needed = 120 - height
    print(f"Sorry, you need {height_needed:.2f} more cm to play.")


#Finished