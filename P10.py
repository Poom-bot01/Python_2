usage = float(input("usage amount (unit) this month: "))
avg = float(input("avg usage amount (unit) in the past 3 months: "))

if avg <= 150:
    service_fee = 8.19
    cost = 0
    if usage > 0:
        cost += (min(usage, 5) - 0) * 0
    if usage > 5:
        cost += (min(usage, 15) - 5) * 1.3576
    if usage > 15:
        cost += (min(usage, 25) - 15) * 1.5445
    if usage > 25:
        cost += (min(usage, 35) - 25) * 1.7968
    if usage > 35:
        cost += (min(usage, 100) - 35) * 2.1800
    if usage > 100:
        cost += (min(usage, 150) - 100) * 2.2734
    if usage > 150:
        cost += (min(usage, 400) - 150) * 2.7781
    if usage > 400:
        cost += (usage - 400) * 2.9780
else:
    service_fee = 40.90
    cost = 0
    if usage > 0:
        cost += min(usage, 150) * 1.8047
    if usage > 150:
        cost += (min(usage, 400) - 150) * 2.7781
    if usage > 400:
        cost += (usage - 400) * 2.9780

total_cost = cost + service_fee

usage_display = f"{usage:.0f}" if usage == int(usage) else f"{usage:g}"

print(f"Your electricity usage is {usage_display} unit(s).")
print(f"The electricity cost is {total_cost:.2f} Baht.")

#Finished