# fahrenheit to celsius
#formula (f - 32) * (5/9)
fahrenheit_degrees = input("What is the temperature in fahrenheit?: ")
fahrenheit_formula = (float(fahrenheit_degrees) - 32) * (5/9)
# result to one decimal place of precision
result = f"The temperature in Celsius is: {fahrenheit_formula:.1f} degrees"
print(result)
