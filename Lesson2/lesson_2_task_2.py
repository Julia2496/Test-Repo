def is_year_leap(year):
    return year % 4 == 0  

year = 2024
print(f"год {year}: {is_year_leap(year)}")

year = 2023
print(f"год {year}: {is_year_leap(year)}")