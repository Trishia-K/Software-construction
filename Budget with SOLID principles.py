class Transaction:
    #For a just one expense entry
    def __init__(self, description: str, amount: float, category: str):
        self.description = description
        self.amount = amount
        self.category = category


class BudgetTracker:
    #Handles all budget logic and tracks spending totals.

    def __init__(self, budget_limit: float):
        self.limit = budget_limit
        self.transactions = []
        self.total_spent = 0.0
        self.category_totals = {}  # { "Food": 5000, "Transport": 2000 }

    def add_transaction(self, description: str, amount: float, category: str):
        """Records a new expense and updates both global and category totals."""
        new_transaction = Transaction(description, amount, category)
        self.transactions.append(new_transaction)
        self.total_spent += amount

        # Creates the category key and then adds the amount
        self.category_totals[category] = self.category_totals.get(category, 0) + amount

    def is_over_budget(self) -> bool:
        return self.total_spent > self.limit

    def get_remaining_balance(self) -> float:
        return self.limit - self.total_spent


class BudgetUI:
    #Handles all user interactions

    @staticmethod
    def get_valid_float(prompt: str) -> float:
        #This keeps prompting until the user enters a valid positive number.
        while True:
            try:
                value = float(input(prompt))
                if value < 0:
                    print("Value cannot be negative.")
                    continue
                return value
            except ValueError:
                print("Please enter a valid number.")

    def run(self):
        print("--- Weekly Budget Tracker ---")

        budget_limit = self.get_valid_float("Enter your budget for the week: ")
        tracker = BudgetTracker(budget_limit)

        print("\nEnter at least 5 transactions. Type 'done' in description to finish.\n")

        while True:
            desc = input("Describe your expense (or 'done'): ")
            if desc.lower() == "done":
                # Enforces the 5-transaction minimum before allowing exit
                if len(tracker.transactions) < 5:
                    print(f"Minimum 5 required. (You have: {len(tracker.transactions)})")
                    continue
                break

            category = input("Enter category (e.g., Food, Rent, Fun): ").capitalize()
            amount = self.get_valid_float("How much was it?: ")

            tracker.add_transaction(desc, amount, category)

            if tracker.is_over_budget():
                print("Warning: You have exceeded your budget!")

            print(f"Current total spent: UGX {tracker.total_spent}\n")

        self.display_summary(tracker)

    def display_summary(self, tracker: BudgetTracker):
        #Prints a detailed breakdown of the week's finances.
        print("\n" + "=" * 40)
        print("FINAL FINANCIAL SUMMARY")
        print("=" * 40)
        print(f"Initial Budget:  UGX {tracker.limit}")
        print(f"Total Spent:     UGX {tracker.total_spent}")

        balance = tracker.get_remaining_balance()
        if balance >= 0:
            print(f"Balance Left:    UGX {balance}")
        else:
            print(f"Total Deficit:   UGX {abs(balance)}")

        print("\n--- Spending by Category ---")
        for category, total in tracker.category_totals.items():
            print(f"* {category}: UGX {total}")

        print("\n--- Detailed Transaction Log ---")
        for t in tracker.transactions:
            print(f"[{t.category}] {t.description}: UGX {t.amount}")


if __name__ == "__main__":
    app = BudgetUI()
    app.run()