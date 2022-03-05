from cgitb import small


print("Enter a list of numbers, type 0 when finished")

new_number = ""
numbers = []
while new_number != 0:
    new_number = int(input("Enter a number: "))
    if new_number != 0:
        numbers.append(new_number)

sum_total = 0

for number in numbers:
    #sum
    sum_total += number
    #average
    average = sum_total / len(numbers)
    #largest number
    largest_number = max(numbers)
    #smallest number
    # if number > 0:
    #     smallest_number = min(numbers)
    #     print(f"The smallest number is: {smallest_number}")

print(f"The sum is {sum_total:.2f}")
print(f"The average is: {average}")
print(f"The largest number is: {largest_number}")


#sorted list
print("The sorted list is:")
for sorted in numbers:
    sorted_list = numbers.sort()
    print(sorted)
