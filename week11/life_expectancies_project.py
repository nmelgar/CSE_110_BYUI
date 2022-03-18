column_count = 0
min_age = 1
max_age = 150

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
            print(f"{country}, {code}, {year}, {life_expectancy}, {column_count}")

            if life_expectancy >= min_age:
                min_age = life_expectancy
            if life_expectancy <= max_age:
                max_age = life_expectancy
    print(f"Max life expectancty is {max_age}")
    print(f"Max life expectancty is {min_age}")
