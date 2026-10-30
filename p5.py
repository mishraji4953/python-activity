transactions = [
    ("T101", 500),
    ("T102", 1000),
    ("T101", 500),
    ("T103", 6000),
    ("T104", 300)
]

seen = []
threshold = 5000

for transaction_id, amount in transactions:

    if transaction_id in seen:
        print("Duplicate transaction:", transaction_id)
    else:
        seen.append(transaction_id)

    if amount > threshold:
        print("High value transaction:", transaction_id)
