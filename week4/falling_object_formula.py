import math
# formula -> v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
print("Welcome to the velocity calculator.")
print("Please enter the following:")
print("----------------------------------------------")
mass_kg = float(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time_in_seconds = float(input("Time (in seconds): "))
density = float(
    input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_sectional_area = float(input("Cross sectional area (in m^2): "))
drag_constant = float(
    input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# inner value c -> c = (1/2) * p * A * C (this upper C is the drag constant)
inner_c_formula = ((1/2) * (density * cross_sectional_area * drag_constant))
# mass * gravity * inner value c
mgc = mass_kg * gravity * inner_c_formula
formula_part_1 = math.sqrt((mass_kg * gravity)/inner_c_formula)
formula_part_2 = (1 - math.exp((-math.sqrt(mgc)/mass_kg) * time_in_seconds))
formula_final = formula_part_1 * formula_part_2
print("----------------------------------------------\n")

print(f"The inner value of c is: {inner_c_formula:.3f}")
print(f"The velocity after {time_in_seconds} is : {formula_final:.3f} m/s\n")

print("----------------------------------------------")
