# ShadowFox - Task 02: Numbers and Real-World Calculations

# 1. Function using format() to convert number into octal
def format_number(value, fmt_type):
    formatted = format(value, fmt_type)
    print(f"Formatted representation of {value} using '{fmt_type}':", formatted)
    return formatted

# Call the function with 145 and 'o' (octal)
format_number(145, 'o')

print("\n---")

# 2. Area of a circular pond
radius = 84  # in meters
pi = 3.14

# Circle Area = π * r^2
pond_area = pi * (radius ** 2)
print("Area of the pond (in square meters):", pond_area)

# Bonus: Water in the pond
# 1.4 liters per square meter
water_per_sqm = 1.4
total_water_liters = pond_area * water_per_sqm

# Convert to int to remove decimal part
print("Total water in the pond (liters, no decimal):", int(total_water_liters))

print("\n---")

# 3. Calculate speed in meters per second
distance = 490  # in meters
time_minutes = 7
time_seconds = time_minutes * 60  # Convert minutes to seconds

speed_mps = distance / time_seconds

# Print as integer (no decimal)
print("Speed while crossing the street (m/s, no decimal):", int(speed_mps))



