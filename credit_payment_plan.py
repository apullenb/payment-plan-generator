def calculate_debt_payoff(debts, available_funds):
    total_debt = sum(debt['balance'] for debt in debts)
    monthly_payments = []

    while total_debt > 0:
        monthly_payment = 0
        for debt in debts:
            if debt['balance'] > 0:
                payment = min(debt['balance'], debt['minimum_payment'])
                monthly_payment += payment
                debt['balance'] -= payment
                total_debt -= payment

        if monthly_payment > available_funds:
            return False, monthly_payments, available_funds - monthly_payment

        monthly_payments.append(monthly_payment)

    return True, monthly_payments, 0


def main():
    print("Debt Snowball Payoff Plan\n")

    # Prompt for paycheck frequency
    paycheck_frequency = input("Enter your paycheck frequency (e.g., monthly, bi-weekly, weekly): ")

    # Prompt for interest rate consideration
    consider_interest = input("Do you want to consider interest rates? (yes/no): ")

    interest_rate = 0  # Default interest rate
    if consider_interest.lower() == "yes":
        custom_interest = input("Do you want to enter a custom interest rate for each account? (yes/no): ")
        if custom_interest.lower() == "yes":
            interest_rate = float(input("Enter the custom interest rate (as a decimal): "))

    # Prompt for debt details
    debts = []
    while True:
        account_name = input("Enter the account name (or 'done' to finish): ")
        if account_name.lower() == "done":
            break

        balance = float(input("Enter the total balance owed: "))
        minimum_payment = float(input("Enter the minimum payment amount: "))
        interest = interest_rate if consider_interest.lower() == "yes" else 0

        debt = {'account_name': account_name, 'balance': balance, 'minimum_payment': minimum_payment, 'interest': interest}
        debts.append(debt)

    # Prompt for available funds per paycheck
    available_funds = float(input("Enter the amount of funds available per paycheck: "))

    # Calculate debt payoff plan
    success, monthly_payments, deficit = calculate_debt_payoff(debts, available_funds)

    # Display debt payoff plan
    if success:
        print("\nDebt Payoff Plan:")
        for i, payment in enumerate(monthly_payments, start=1):
            print(f"Month {i}: Pay ${payment:.2f} towards each account")
    else:
        print(f"\nError: Insufficient funds! You are short of ${deficit:.2f} each month.")

    print("\nDebt has been fully paid off!")


if __name__ == "__main__":
    main()
