balance = 5000
transactions = []

while True:
    print("\n--- ATM MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction Summary")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            transactions.append("Deposit: " + str(amount))
            print("Deposit successful")
        else:
            print("Invalid amount")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            transactions.append("Withdrawal: " + str(amount))
            print("Withdrawal successful")
        else:
            print("Invalid amount or insufficient balance")

    elif choice == 3:
        print("Current Balance:", balance)

    elif choice == 4:
        for transaction in transactions:
            print(transaction)

    elif choice == 5:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
