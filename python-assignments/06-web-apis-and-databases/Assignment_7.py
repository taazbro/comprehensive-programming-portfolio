# Assignment 7
# Name: Tanjim Ahmed Al Zabeer

import urllib.request
import json
import re

# Here i gonna set URL to get data about Bangladesh. This country is the most beautiful in the world.
url = "https://restcountries.com/v3.1/all"

# Now i gonna open and read from the URL easily.
response = urllib.request.urlopen(url)
data = response.read().decode()

# In this step i gonna analyz JSON data.
countries = json.loads(data)

# Now i will access my country's details. Cool huh.
bangladesh_info_raw = None
for country in countries:
    if "Bangladesh" == country['name']['common']:
        bangladesh_info_raw = country
        break

# So in here i will create a simple text block to apply regex, see magic.
info_text = f"""
Name: {bangladesh_info_raw['name']['common']}
Official Name: {bangladesh_info_raw['name']['official']}
Capital: {bangladesh_info_raw['capital'][0]}
Region: {bangladesh_info_raw['region']}
Subregion: {bangladesh_info_raw['subregion']}
Area: {bangladesh_info_raw['area']} sq km
Population: {bangladesh_info_raw['population']}
Currency: {list(bangladesh_info_raw['currencies'].keys())[0]}
Language: {list(bangladesh_info_raw['languages'].values())[0]}
"""

# Here i will use regex to extract every piece of information that i want.
name = re.findall(r"Name: (.+)", info_text)
official_name = re.findall(r"Official Name: (.+)", info_text)
capital = re.findall(r"Capital: (.+)", info_text)
region = re.findall(r"Region: (.+)", info_text)
subregion = re.findall(r"Subregion: (.+)", info_text)
area = re.findall(r"Area: ([\d.]+)", info_text)
population = re.findall(r"Population: (\d+)", info_text)
currency = re.findall(r"Currency: (.+)", info_text)
language = re.findall(r"Language: (.+)", info_text)

# Now i will save the information i collected in a dictionary.
bangladesh_details = {
    "Country Name": name[0] if name else "N/A",
    "Official Name": official_name[0] if official_name else "N/A",
    "Capital City": capital[0] if capital else "N/A",
    "Region": region[0] if region else "N/A",
    "Subregion": subregion[0] if subregion else "N/A",
    "Area (sq km)": area[0] if area else "N/A",
    "Population": population[0] if population else "N/A",
    "Currency": currency[0] if currency else "N/A",
    "Language": language[0] if language else "N/A"
}

# We are at the end. Now we will write the data into a text file.
with open("bangladesh_details.txt", "w") as file:
    file.write("Field\t\t\tValue\n")
    file.write("--------------------------------------------\n")
    for key, value in bangladesh_details.items():
        file.write(f"{key}\t{value}\n")

print("Beautiful Bangladesh information will be saved into 'bangladesh_details.txt'.")
