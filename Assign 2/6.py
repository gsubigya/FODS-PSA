# Function to search a country in a list
def search_country(countries, country):
    if country in countries:
        return countries.index(country)
    else:
        return "Not Found in List"

# Example list of countries
country_list = ["Nepal", "Japan", "China", "USA", "UK"]

# Test the function
print(search_country(country_list, "China"))  # Should return 2
print(search_country(country_list, "India"))  # Should return "Not Found in List"