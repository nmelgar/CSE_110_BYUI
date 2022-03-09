bank_accounts = []
balances = []
run = True

print("Enter the names and balances of bank accounts: (type 'quit' when done)")
add_account = ""

while add_account != "quit":
    add_account = str(input("What is the name of this account? "))
    if add_account != "quit":
        add_balance = float(input("What is the balance "))
        bank_accounts.append(add_account)
        balances.append(add_balance)
    else:
        run = False

print("")
print("Account Information")
total = 0
for index in range(len(bank_accounts)):
    add_account = bank_accounts[index]
    add_balance = balances[index]
    print(f"{add_account} - ${add_balance}")
    
    total += balances[index]
    average = total / len(balances)

print("")
print(f"Total: ${total}")
print(f"Average: ${average: .2f}")
