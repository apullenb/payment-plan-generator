def calculate_debt_payoff(debts, available_funds):
    total_debt = sum(debt['balance'] for debt in debts)
    monthly_payments = []

    while total_debt > 0:
        minimum_payment_sum = sum(debt['minimum_payment'] for debt in debts if debt['balance'] > 0)
        extra_payment = available_funds - minimum_payment_sum
        if extra_payment < 0:
            return False, monthly_payments, abs(extra_payment)

        debts_sorted = sorted(debts, key=lambda x: x['balance'])
        monthly_payment = 0
        deficit = 0

        for debt in debts_sorted:
            if debt['balance'] > 0:
                payment = min(debt['balance'], debt['minimum_payment'] + extra_payment)
                debt['balance'] -= payment
                total_debt -= payment
                monthly_payment += payment

                if payment > debt['minimum_payment']:
                    deficit = payment - debt['minimum_payment']

                print(f"{debt['account_name']}: Pay ${payment:.2f}, New Balance: ${debt['balance']:.2f}")

        if deficit > 0:
            print(f"Deficit: ${deficit:.2f}")

        monthly_payments.append(monthly_payment)

    return True, monthly_payments, 0


def display_debt_details(debts):
    print("Current Debts:")
    for debt in debts:
        print(f"{debt['account_name']}: ${debt['balance']:.2f}")


def edit_account(debts):
    account_name = input("Enter the name of the account you want to edit: ")
    for debt in debts:
        if debt['account_name'] == account_name:
            new_balance = float(input("Enter the new balance: "))
            new_minimum_payment = float(input("Enter the new minimum payment: "))
            debt['balance'] = new_balance
            debt['minimum_payment'] = new_minimum_payment
            print("Account updated successfully.")
            return

    print("Account not found.")


def edit_paycheck_amount(available_funds):
    new_amount = float(input("Enter the new amount of funds available per paycheck: "))
    return new_amount


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
        display_debt_details(debts)

        while True:
            print("\nOptions:")
            print("1. Edit an account")
            print("2. Edit paycheck amount")
            print("3. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                edit_account(debts)
                success, monthly_payments, deficit = calculate_debt_payoff(debts, available_funds)
                display_debt_details(debts)
            elif choice == "2":
                available_funds = edit_paycheck_amount(available_funds)
                success, monthly_payments, deficit = calculate_debt_payoff(debts, available_funds)
                display_debt_details(debts)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

        print("\nDebt has been fully paid off.")

    else:
        print("\nError: Not enough available funds.")
        print(f"Deficit: ${deficit:.2f} per paycheck.")


if __name__ == '__main__':
    main()