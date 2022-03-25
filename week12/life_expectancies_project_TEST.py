column_count = 0

# for specific year
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
            if year_input == int(year):
                # print(str(year_input) + " " +  str(column_count) +  " " + str(life_expectancy))
                year_sum_counter += 1
                year_sum_total += life_expectancy
                average = year_sum_total / year_sum_counter
                print(f"{life_expectancy} + {year_sum_counter}")
    print(f"Total is = {year_sum_total}")
    print(f"The average is = {average: .2f}")