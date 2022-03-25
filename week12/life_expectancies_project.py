# VARIABLES FOR GENERAL INFORMATION
column_count = 0
min_age = 25
max_age = 50
min_selected_country = ""
max_selected_country = ""
min_selected_year = ""
max_selected_year = ""

# VARIABLES FOR A SPECIFIC YEAR
year_input = 0
year_min_age = 1000
year_max_age = 1
year_min_selected_country = ""
year_max_selected_country = ""
year_min_selected_year = ""
year_max_selected_year = ""
year_sum_counter = 0
year_sum_total = 0
average = 0

with open("life-expectancy.csv") as data_source:
    year_input = int(input("Enter the year o interest: "))
    for line in data_source:
        # clean line
        line = line.strip()
        # split in parts, the variable columns will contain the parts
        columns = line.split(",")

        country = columns[0]
        code = columns[1]
        year = columns[2]
        life_expectancy = columns[3]
        column_count += 1

        if column_count != 1:
            # GET GENERAL MAX and MIN LIFE EXPECTANCY
            life_expectancy = float(life_expectancy)

            if life_expectancy <= min_age:
                min_age = life_expectancy
                min_selected_country = country
                min_selected_year = year

            if life_expectancy >= max_age:
                max_age = life_expectancy
                max_selected_country = country
                max_selected_year = year

            # FOR A SPECIFIC YEAR
            if year_input == int(year):
                # print(str(year_input) + " " +  str(column_count) +  " " + str(life_expectancy))
                year_sum_counter += 1
                year_sum_total += life_expectancy
                average = year_sum_total / year_sum_counter

                if life_expectancy <= year_min_age:
                    year_min_age = life_expectancy
                    year_min_selected_country = country

                if life_expectancy >= year_max_age:
                    year_max_age = life_expectancy
                    year_max_selected_country = country

    print(
        f"\nThe overall max life expectancty is: {max_age} from {max_selected_country} in {max_selected_year}")
    print(
        f"The overall min life expectancty is: {min_age} from {min_selected_country} in {min_selected_year}")

    # FOR A SPECIFIC YEAR
    print(f"\nFor the year {year_input}:")
    print(
        f"The average life expectancy across al countries was {average: .2f}")
    print(
        f"The max age expectancy was in {year_max_selected_country} with {year_max_age}")
    print(
        f"The min age expectancy was in {year_min_selected_country} with {year_min_age}")
