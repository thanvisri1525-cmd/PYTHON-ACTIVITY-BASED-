print("ATM TRANSACTION SYSTEM")

balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Available balance: Rs.", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful.")
            print("Balance:", balance)
        else:
            print("Enter a positive amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a positive amount.")
        elif amount <= balance:
            balance -= amount
            print("Withdrawal successful.")
            print("Balance:", balance)
        else:
            print("Insufficient balance.")

    elif choice == "4":
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice.")
