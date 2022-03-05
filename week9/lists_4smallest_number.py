smallest = 9999999
my_list = [1, 3, 7, 8, 9]
for value in my_list:
    if value < smallest:
        smallest = value

print(f"The smallest number is {smallest}")
