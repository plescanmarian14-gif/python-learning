def celsius_in_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_in_celsius(f):
    return (f - 32) * 5/9

def km_in_mile(km):
    return km * 0.621371

# Apelare funcții
temp_c = 25
print(f"{temp_c}°C = {celsius_in_fahrenheit(temp_c)}°F")

distanta_km = 10
print(f"{distanta_km} km = {km_in_mile(distanta_km)} mile")