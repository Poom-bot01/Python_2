product, price = input("Enter product and price: ").split()
price = float(price)
if product[0].upper() == "T":
    price_without_tax = price / 1.07
    tax = price - price_without_tax
    print(f"{product} is taxable (7%).")
else:
    price_without_tax = price
    tax = 0
    print(f"{product} is not taxable.") 



print(f"Price without tax: {price_without_tax:.2f} Baht")
print(f"Tax (7%): {tax:.2f} Baht")