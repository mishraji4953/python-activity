products = []
total = 0

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    products.append((name, amount))
    total += amount

print("\n----- BILL -----")

for name, amount in products:
    print(name, ":", amount)

if total >= 2000:
    discount = total * 0.10
elif total >= 1000:
    discount = total * 0.05
else:
    discount = 0

final_amount = total - discount
print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)+
