# wind chill formula(°F)
# 35.74 + 0.6215T - 35.75(V^0.16) + 0.4275T(V^0.16)
# where -> T = Air Temperature(°F) | V = Wind Speed(mph)

wind_speed = 5


def wind_chill(temperature):
    # return (35.74 + (0.6215 * temperature)) - (35.75(wind_speed**0.16) + (0.4275 * temperature)(wind_speed**0.16))
    return (35.74 + 0.6215 * temperature) - (35.75 * (wind_speed**0.16)) + ((0.4275 * temperature) * (wind_speed**0.16))


def convert_celsius_to_fahrenheit(temperature):
    return (temperature * 1.8) + 32


temperature = float(input("What is the temperature? "))
user_choice = str(input("Fahrenheit or Celsius (F/C)? "))
user_choice = user_choice.lower()

if user_choice == "f":
    while wind_speed <= 60:
        final_result = wind_chill(temperature)
        print(
            f"At temperature {temperature}F, and wind speed {wind_speed} mph, the windchill is: {final_result: .2f}F")
        wind_speed += 5

elif user_choice == "c":
    while wind_speed <= 60:
        celsius_degrees = convert_celsius_to_fahrenheit(temperature)
        final_result = wind_chill(celsius_degrees)
        print(
            f"At temperature {celsius_degrees}F, and wind speed {wind_speed} mph, the windchill is: {final_result: .2f}F")
        wind_speed += 5
