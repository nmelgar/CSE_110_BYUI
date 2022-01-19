age = int(input("\nEnter your age: "))
age_next_birthday = age + 1
# print age next birthday
print(f"Your age next birthday will be: {age_next_birthday}\n")

user_eggs_cartons = int(input("Enter the egg cartons you have: "))
eggs_per_carton = 12
total_eggs = user_eggs_cartons * eggs_per_carton
# print the numbers of eggs
print(f"You have: {user_eggs_cartons}, each carton contains {eggs_per_carton}."
      f"\nSo, you have {total_eggs} eggs in total.\n")

number_cookies = int(input("How many cookies do you have?: "))
number_people = int(input("How many people are there?: "))
cookies_per_person = number_cookies / number_people 
print(f"Each person will have {cookies_per_person} cookies")
