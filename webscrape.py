import time
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import sqlite3


options = webdriver.FirefoxOptions()
options.add_argument("-headless")
options.add_argument("--disable-gpu")
driver = webdriver.Firefox(options=options)

driver.get("https://www.timeanddate.com/weather/")
time.sleep(2)
table_body = driver.find_element(By.CLASS_NAME, 'zebra.fw.tb-theme')
cities = table_body.find_elements(By.CSS_SELECTOR, 'a')
temperature = table_body.find_elements(By.CLASS_NAME, 'rbi')
weather_details = table_body.find_elements(By.CLASS_NAME, 'r')
weaether_description = []
for details in weather_details:
    try:
        image = details.find_element(By.TAG_NAME, 'img')
        image_details = image.get_attribute('title')
        weaether_description.append(image_details)
    except Exception:
        continue


# print(weaether_description)
# print(len(weaether_description))
time_details = [time.text for time in weather_details if time.text != ""]
# print(len(time_details))
temp_list = []
for temp in temperature:
    temp_list.append(temp.text)
# print(len(temp_list))
city_list = []
for city in cities:
    city_list.append(city.text)
# print(len(city_list))
# for detail in time_details:
#     print(detail)

weather_dict = {}
column_headers = [
    'City',
    'Temperature',
    'Time'
]
weather_df = pd.DataFrame(zip(city_list, temp_list, time_details), columns=column_headers)
# for city,temp, time in zip(city_list, temp_list, time_details):
#     print(f'the weather in {city} was {temp} at {time}')
print(weather_df.head())
weather_df.to_csv('new_weather_data.csv')
with sqlite3.connect("weather.db") as conn:
    weather_df.to_sql("weather", conn, if_exists="replace", index=False)




