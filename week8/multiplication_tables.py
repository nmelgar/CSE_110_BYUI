# numbers = int(
#     input("What number would you like to multiply? "))
# for number in range(1, numbers + 1):
#     print(numbers, "X", number, "=", number * numbers)

number = int(
    input("What number would you like to multiply? "))

for i in range(1, number +1):
    for j in range(1, number +1):
        print(i * j, end="\t")
    print("\n")
