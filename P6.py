product_price = input("Enter product and price: ").split()
product = product_price[0]
price = float(product_price[1])

is_taxable = product.startswith("T")  

if is_taxable:
    price_without_tax = price / 1.07
else:
    price_without_tax = price

tax = price - price_without_tax

print(f"Price without tax = {price_without_tax:.2f} Baht")
print(f"7% Tax = {tax:.2f} Baht")

#Finished