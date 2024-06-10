# Task ID: Mbpp/638

# Description/Response:
"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""
def wind_chill(wind_velocity, temperature):
    wind_chill = 13.12 + 0.6215 * temperature - 11.37 * wind_velocity**0.16 + 0.396 * temperature**0.16 * wind_velocity**0.16
    return round(wind_chill)