column_count = 0
min_age = 25
max_age = 50
min_selected_country = ""
max_selected_country = ""
min_selected_year = ""
max_selected_year = ""
year_input = int(input("Enter the year o interest: "))

with open("life-expectancy.csv") as data_source:
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

            elif life_expectancy >= max_age:
                max_age = life_expectancy
                max_selected_country = country
                max_selected_year = year
        
        #will get the average, max, min of specific year
        #if line instead of column_count TRY
        if column_count != 1:
            if year_input == year:
                print(f"The year is {year_input}")

    print(
        f"\nThe overall max life expectancty is: {max_age} from {max_selected_country} in {max_selected_year}")
    print(
        f"The overall min life expectancty is: {min_age} from {min_selected_country} in {min_selected_year}")
