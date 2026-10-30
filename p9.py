stock = {
    "idli": 50,
    "dosa": 40,
    "meals": 30
}

price = {
    "idli": 20,
    "dosa": 40,
    "meals": 60
}

total_sales = 0

n = int(input("Enter number of orders: "))

for i in range(n):
    item = input("Enter food item: ").lower()
    quantity = int(input("Enter quantity: "))

    if item in stock and quantity > 0:
        if quantity <= stock[item]:
            bill = price[item] * quantity
            stock[item] -= quantity
            total_sales += bill

            print("Order successful")
            print("Bill:", bill)
        else:
            print("Insufficient stock")

    else:
        print("Invalid item or quantity")

print("\nTotal Sales:", total_sales)
print("Remaining Stock:")

for item, quantity in stock.items():
    print(item, ":", quantity)
