column_count = 0
min_age = 25
max_age = 50
selected_country = ""
selected_year = ""

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
            life_expectancy = float(life_expectancy)

            if life_expectancy <= min_age:
                min_age = life_expectancy
                selected_country = country
                
            elif life_expectancy >= max_age:
                max_age = life_expectancy
                selected_country = country
                
    print(f"The overall max life expectancty is: {max_age} from {selected_country} in {selected_year}")
    print(f"The overall min life expectancty is: {min_age} from {selected_country} in {selected_year}")
