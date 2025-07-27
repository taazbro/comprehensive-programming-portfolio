
import re
import sqlite3

# Now we gonna set URLs 
dhaka_url = "https://www.accuweather.com/en/bd/dhaka/28143/weather-forecast/28143"
chittagong_url = "https://www.accuweather.com/en/bd/chittagong/27822/weather-forecast/27822"

# We gonna include the live data from the webpages manually
text_block = f"""
Source URL: {dhaka_url}
City: Dhaka
Temperature: 99°F
Condition: Partly sunny and very warm
Air Quality: Poor
Warning: Danger of dehydration and heat stroke if outside for extended periods of time Saturday

Source URL: {chittagong_url}
City: Chittagong
Temperature: 99°F
Condition: Sunny much of the time and very hot
Air Quality: Fair
Warning: Danger of dehydration and heatstroke if outside for extended periods of time
"""

# Now we gonna use regex  here to get info
pattern = r"Source URL: (.*?)\nCity: (.*?)\nTemperature: (.*?)\nCondition: (.*?)\nAir Quality: (.*?)\nWarning: (.*?)\n"
matches = re.findall(pattern, text_block)

# Here we gonna save the data into a dictionary and also write to text file
city_info = []
with open("bangladesh_weather.txt", "w") as file:
    file.write("Weather Report for Dhaka and Chittagong (AccuWeather)\n")
    file.write("------------------------------------------------------\n")
    for match in matches:
        record = {
            "url": match[0],
            "city": match[1],
            "temp": match[2],
            "condition": match[3],
            "air": match[4],
            "warning": match[5]
        }
        city_info.append(record)
        file.write(f"City: {record['city']}\n")
        file.write(f"URL: {record['url']}\n")
        file.write(f"Temperature: {record['temp']}\n")
        file.write(f"Condition: {record['condition']}\n")
        file.write(f"Air Quality: {record['air']}\n")
        file.write(f"Warning: {record['warning']}\n\n")

# We gonna store this data in an SQLite database
conn = sqlite3.connect("bd_weather.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS weather (
    url TEXT,
    city TEXT,
    temperature TEXT,
    condition TEXT,
    air_quality TEXT,
    warning TEXT
)
""")

for r in city_info:
    cur.execute("""
        INSERT INTO weather (url, city, temperature, condition, air_quality, warning)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (r['url'], r['city'], r['temp'], r['condition'], r['air'], r['warning']))

conn.commit()
conn.close()

print(" Weather data saved successfully.")
