print("REPEATED TRANSACTION DETECTOR")

n = int(input("Enter number of transactions: "))

if n <= 0:
    print("Enter a positive number.")

else:
    transactions = []

    for i in range(n):
        transaction_id = input(
            f"Enter transaction ID {i + 1}: "
        )
        transactions.append(transaction_id)

    duplicates = []

    for transaction_id in transactions:
        if (transactions.count(transaction_id) > 1
                and transaction_id not in duplicates):
            duplicates.append(transaction_id)

    if duplicates:
        print("Repeated transaction IDs:")
        for transaction_id in duplicates:
            print(transaction_id)
    else:
        print("No repeated transactions found.")
