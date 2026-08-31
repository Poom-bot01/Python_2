submit = int(input("How many hours do you submit late? "))
score = int(input("What is your estimated score? "))
if submit <= 0:
    deduction = 0
elif submit <= 24:
    deduction = 20
elif submit <= 48:
    deduction = 50
else:
    deduction = 100



expected_score = score * (1 - deduction / 100)

print(f"Your final score is {expected_score:.1f}.")