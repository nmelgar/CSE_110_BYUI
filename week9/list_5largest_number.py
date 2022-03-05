largest = 0
my_list = [1 , 3, 7, 8, 9]
for value in my_list:
    if value > largest:
        largest = value

print(f"The largest is {largest}")