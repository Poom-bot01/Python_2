product1, price1 = input("Enter product and price: ").split()
product2, price2 = input("Enter product and price: ").split()
product3, price3 = input("Enter product and price: ").split()
price1 = float(price1)
price2 = float(price2)
price3 = float(price3)

total = price1 + price2 + price3
price_without_tax = 0
tax = 0

print("------ Receipt ------")
print(f"{'Item':<24}{'Price':<10}")
if product1[0].upper() == "T":
    p1_no_tax = price1 / 1.07
    tax += price1 - p1_no_tax
    price_without_tax += p1_no_tax
    print(f"{product1:<24}{price1:<8.2f} *T")
else:
    price_without_tax += price1
    print(f"{product1:<24}{price1:<8.2f}")

if product2[0].upper() == "T":
    p2_no_tax = price2 / 1.07
    tax += price2 - p2_no_tax
    price_without_tax += p2_no_tax
    print(f"{product2:<24}{price2:<8.2f} *T")
else:
    price_without_tax += price2
    print(f"{product2:<24}{price2:<8.2f}")

if product3[0].upper() == "T":
    p3_no_tax = price3 / 1.07
    tax += price3 - p3_no_tax
    price_without_tax += p3_no_tax
    print(f"{product3:<24}{price3:<8.2f} *T")
else:
    price_without_tax += price3
    print(f"{product3:<24}{price3:<8.2f}")

print(f"Total = {total:.2f}")
print(f"Price with no tax = {price_without_tax:.2f}")
print(f"Total tax = {tax:.2f}")