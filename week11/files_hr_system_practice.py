#name id_number job_title salary
#single space between each field of data

with open("hr_system.txt") as hr_data:
    for line in hr_data:
        line = line.strip()
        columns = line.split(" ")
        
        name = columns[0]
        id_number = columns[1]
        job_title = columns[2]
        salary = int(columns[3])

        #salary paid twice a month
        salary = salary / 24

        #if it is an engineer add 1000 to salary
        if job_title == "Engineer":
            salary_with_bonus = salary + 1000
        else: 
            salary_with_bonus = salary

        print(f"{name} (ID: {id_number}), {job_title} - ${salary_with_bonus: .2f}")