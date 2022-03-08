
bank_accounts = []
balances = []
run = True

print("Enter the name and balances of bank accounts (type: 'quit' when done)")

while run:
    add_account = str(input("What is the name of this account? "))
    if add_account != "quit":
        bank_accounts.append(add_account)
        add_balance = float(input("What is the balance? "))
        balances.append(add_balance)
    elif add_account == "quit":
        run = False

print("Account information")
for index in range(len(bank_accounts)):
    add_account = bank_accounts[index]
    add_balance = balances[index]
    print(add_account, " - ", add_balance)
    total = add_balance + add_balance
    average = total / len(balances)
print(f"Total: ${total}")
print(f"Average: ${average}")
