column_count = 0

# for specific year
year_input = 0
year_min_age = 1000
year_max_age = 1
year_min_selected_country = ""
year_max_selected_country = ""
year_min_selected_year = ""
year_max_selected_year = ""

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
            if year_input == int(year):
                # print(str(year_input) + " " +  str(column_count) +  " " + str(life_expectancy))
                if life_expectancy <= year_min_age:
                    year_min_age = life_expectancy
                    year_max_selected_country = country
                if life_expectancy >= year_max_age:
                    year_max_age = life_expectancy
                    year_min_selected_country = country
    print(f"Min age expectancy was in {year_min_selected_country} with {year_min_age}")
    print(f"Min age expectancy was in {year_max_selected_country} with {year_max_age}")
                
