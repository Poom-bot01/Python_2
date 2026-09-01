submit = float(input("How many hours do you submit late? "))
print()
score = float(input("What is your estimated score? "))

if submit <= 0:
    deduction = 0
elif submit <= 24:
    deduction = 20
elif submit <= 48:
    deduction = 50
else:
    deduction = 100

expected_score = score * (1 - deduction / 100)

if expected_score == 0:
    print(f"Your expected score is {int(expected_score)}")
else:
    print(f"Your expected score is {expected_score:.1f}")

#Finished