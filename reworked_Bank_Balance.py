customer_name = input('What is your name? ')
starting_balance = float(5000.25)

deposit = float(input(f'Hello, {customer_name}. Your current balance is ${starting_balance}. How much of your paycheck, in USD, would you like to deposit? '))
expenditure_item = input('What have you spent money on? ')
expenses_Withdrawn = float(input('How much will it cost in USD? '))

def check_balance(user_name, balance, deposits, expense_item, expense_amount):
    ending_balance = balance + deposits - expense_amount
    print(f'Your new balance is ${ending_balance}') 
check_balance(customer_name, starting_balance, deposit, expenditure_item, expenses_Withdrawn)