# Exercise 8-6: City Names
# Write a function called city_country() that takes a city and country name.
# Return a formatted string like: "Santiago, Chile"
# Call it with at least three city-country pairs and print each result.

# TODO: Define city_country(city, country) that returns "City, Country"
def city_country(city, country):
    return f"{city}, {country}"


# TODO: Call at least three times and print the returned strings
print(city_country(city='Beijing', country='China'))
print(city_country(city='New York', country='USA'))
print(city_country(city='London', country='UK'))
print(city_country(city='Tokyo', country='Japan'))
print(city_country(city='Paris', country='France'))
print(city_country(city='Berlin', country='Germany'))
