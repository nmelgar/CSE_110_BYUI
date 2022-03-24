people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 1000
youngest_person = ""

oldest_age = 0
oldest_person = ""

for person in people:
    column = person.split(" ")

    name = column[0]
    age = int(column[1])

    if age < youngest_age:
        youngest_age = age
        youngest_person = name

    if age > oldest_age:
        oldest_age = age
        oldest_person = name

print(
    f"The youngest's person age is: {youngest_age}, and its name is: {youngest_person}")
print(
    f"The youngest's person age is: {oldest_age}, and its name is: {oldest_person}")
