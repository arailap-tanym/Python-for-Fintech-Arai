"""Example analysis using fictional fintech transaction data."""

transactions = [
    {"date": "2026-01-05", "category": "groceries", "amount": 42.75, "currency": "USD"},
    {"date": "2026-01-08", "category": "transport", "amount": 18.50, "currency": "USD"},
    {"date": "2026-01-12", "category": "subscription", "amount": 9.99, "currency": "USD"},
]


def main():
    total_spend = sum(transaction["amount"] for transaction in transactions)
    print(f"Dummy transactions: {len(transactions)}")
    print(f"Total spend: ${total_spend:.2f} {transactions[0]['currency']}")


if __name__ == "__main__":
    main()
