min = 0
max = 100
numbers = [1, 3, 0.02,  5, 6, 8,-8,  34, 25, 89, 150, 0.0001, -3]

for number in numbers:
    if number <= min:
        min = number
    if number >= max:
        max = number
print(f"The min value is {min}")
print(f"The max value is {max}")
