with open("life-expectancy.csv") as data_source:
    for line in data_source:
        line = line.strip()
        parts = line.split(",")
        
        country = parts[0]
        country_initials = parts[1]
        year = parts[2]
        life_expectancy = parts[3]
        life_expectancy = float(life_expectancy)

        # choose_year = int(input("Enter the year of interest: "))

        max_life_expectancy =  0
        min_life_expectancy =  0 

        
        
        # if max_life_expectancy < life_expectancy:
        #     life_expectancy = max_life_expectancy
        # print(max_life_expectancy)

print(type(life_expectancy))