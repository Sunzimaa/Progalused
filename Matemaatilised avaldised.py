"""Set of different math expression exercises."""
import math

num_a = 5
num_b = 2

# 1. Sum and difference
sum = num_a + num_b
print(f"{num_a} + {num_b} = {sum}")
print("--------------------------")

difference = num_a - num_b
print(f"{num_a} - {num_b} = {difference}")
print("--------------------------")

# 2. Float division
division = num_a / num_b
print(f"{num_a} / {num_b} = {division}")
print("--------------------------")

# 3. Integer division
division = num_a // num_b
print(f"{num_a} // {num_b} = {division}")
print("--------------------------")

# 4. Powerful operations
multiply_numbers = num_a * num_b
print(f"{num_a} * {num_b} = {multiply_numbers}")
print("--------------------------")

power = num_a ** num_b
print(f"{num_a} ** {num_b} = {power}")
print("--------------------------")

remainder = num_a % num_b
print(f"{num_a} % {num_b} = {remainder}")
print("--------------------------")

# 5. Find average
average = (num_a + num_b) / 2
print(f"({num_a} + {num_b}) / {2} = {average}")
print("--------------------------")

# 6. Area of a circle

radius = 3.5
circle_area = math.pi * radius * radius
print(f"{math.pi} * {radius} * {radius} = {circle_area}")
circle_area = (round(circle_area, 2))
print(circle_area)
print("--------------------------")

# 7. Area of an equilateral triangle

side_length = 5
triangle_area = (math.sqrt(3) / 4) * side_length ** 2
print(triangle_area)
triangle_area = round(triangle_area)
print(triangle_area)
print(f"Triangle area is {triangle_area} if side length is {side_length}")
print("--------------------------")

# 8. Calculate discriminant

a = 1
b = 5
c = 6
discriminant = b ** 2 - 4 * a * c
print(discriminant)
print(f"Numbers {a} and {b} and {c} discriminant is {discriminant}")
print("--------------------------")

# 9. Calculate hypotenuse length

a = 3
b = 4
c = math.sqrt(a ** 2 + b ** 2)
print(c)
print(f" Numbers {a} and {b} hypetenus is {c}")
print("--------------------------")

# 10. Calculate cathetus length

a = 6
c = 3
b = math.sqrt(a ** 2 - c ** 2)
print(b)
print(f" Numbers {a} and {c} cathetus is {b}")
print("--------------------------")

# 11. Time converter

seconds = 9325
print(f"Seconds {seconds}")
minutes = seconds // 60
print(f"Minutes {minutes}")
print(f"Minutes residue is {seconds % 60} seconds")
hours = minutes // 60
print(f"Hours {hours}")
print(f"Hours residue is {minutes % 60} minutes and {seconds % 60} seconds")
print("--------------------------")

# 12. Student helper

angle = 35
sine = math.sin(angle)
cosine = math.cos(angle)

sine = round(sine, 1)
cosine = round(cosine, 1)

print(sine)
print(cosine)

print(f"Angle {angle} sine is {sine}")
print(f"Angle {angle} cosine is {cosine}")
print("--------------------------")

# 13. Greetings

n = 4
lots_of_heys = "hey " * n
print(lots_of_heys)
print("--------------------------")

# 14. Adding numbers

num_a = "1"
num_b = "2"
string_numbers = num_a + num_b
print(string_numbers)
print("--------------------------")


