balance = 5000
deposits = 0
withdrawals = 0

n = int(input("Enter number of transactions: "))

for i in range(n):
    choice = input("Enter deposit or withdraw: ").lower()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")

    elif choice == "deposit":
        balance += amount
        deposits += amount
        print("Deposit successful")

    elif choice == "withdraw":
        if amount <= balance:
            balance -= amount
            withdrawals += amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    else:
        print("Invalid transaction")

print("Final Balance:", balance)
print("Total Deposits:", deposits)
print("Total Withdrawals:", withdrawals)
