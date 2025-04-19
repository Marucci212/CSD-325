# city_functions.py

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

# Call the function three times
print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan"))
print(city_country("paris", "france"))

def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# Final calls:
print(city_country("santiago", "chile"))
print(city_country("cairo", "egypt", 9500000))
print(city_country("madrid", "spain", 6700000, "spanish"))
