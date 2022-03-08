
bank_accounts = []
balances = []
run = True

print("Enter the name and balances of bank accounts (type: 'quit' when done)")

while run:
    add_account = str(input("What is the name of this account? "))
    if add_account != "quit":
        bank_accounts.append(add_account)
        add_balance = int(input("What is the balance? "))
        balances.append(add_balance)
    elif add_account == "quit":
        run = False

print("Account information")
