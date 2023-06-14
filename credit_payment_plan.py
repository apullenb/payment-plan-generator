class CreditAccount:
    def __init__(self, name, balance, min_payment):
        self.name = name
        self.balance = balance
        self.min_payment = min_payment


def create_payment_plan(accounts, paychecks, funds_per_paycheck):
    payment_plans = []
    
    for index, paycheck in enumerate(paychecks):
        payment_plan = {
            'date': paycheck['date'],
            'funds_available': paycheck['amount'],
            'payments': []
        }
        
        for account in accounts:
            if account.balance > 0:
                payment_amount = min(account.min_payment, payment_plan['funds_available'])
                payment_amount = min(payment_amount, account.balance)
                new_balance = max(account.balance - payment_amount, 0)
                
                payment_plan['payments'].append({
                    'account_name': account.name,
                    'payment_amount': payment_amount,
                    'new_balance': new_balance
                })
                
                payment_plan['funds_available'] -= payment_amount
                account.balance = new_balance
        
        payment_plans.append(payment_plan)
    
    return payment_plans


def main():
    # Get user inputs
    accounts = []
    paychecks = []
    
    num_paychecks = int(input("Enter the number of paychecks per month: "))
    for i in range(num_paychecks):
        paycheck_date = input("Enter the date of paycheck {}: ".format(i + 1))
        paycheck_amount = float(input("Enter the available funds for paycheck {}: $".format(i + 1)))
        
        paycheck = {
            'date': paycheck_date,
            'amount': paycheck_amount
        }
        paychecks.append(paycheck)
    
    while True:
        account_name = input("Enter the account name (or 'done' to finish): ")
        
        if account_name.lower() == 'done':
            break
        
        balance = float(input("Enter the balance owed for {}: $".format(account_name)))
        min_payment = float(input("Enter the minimum payment required for {}: $".format(account_name)))
        
        account = CreditAccount(account_name, balance, min_payment)
        accounts.append(account)
    
    # Generate payment plans
    payment_plans = create_payment_plan(accounts, paychecks, num_paychecks)
    
    # Print payment plans
    for index, plan in enumerate(payment_plans):
        print("\nPayment Plan for Month {}".format(index + 1))
        print("-" * 50)
        print("{}/ 15th |  (${:.2f})".format(plan['date'], plan['funds_available']))
        print("   Accounts to Pay    |   Payment Amount:")
        
        for payment in plan['payments']:
            print("       *{:<15} ${:.2f}".format(payment['account_name'], payment['payment_amount']))
        
        print("\n{}/ 30th  |  (${:.2f})".format(plan['date'], plan['funds_available']))
        print("   Accounts to Pay    |   Payment Amount:")
        
        for payment in plan['payments']:
            print("       *{:<15} ${:.2f}   |   New Balance: ${:.2f}".format(payment['account_name'], 
                                                                            payment['payment_amount'], 
                                                                            payment['new_balance']))


if __name__ == "__main__":
    main()
