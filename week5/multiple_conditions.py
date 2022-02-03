country = input("Enter the country you live: ")

if country.lower() == "canada":
    province = input("Enter the province you live: ")
    # if province.lower() in("alberta", "nunavut", "yukon"):
    if province.lower() == "alberta" or province.lower() == "nunavut":
        tax = 0.05
    elif province.lower() == "ontario":
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0
print(tax)
