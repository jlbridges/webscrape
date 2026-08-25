from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
options = webdriver.FirefoxOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)

driver.get("https://www.timeanddate.com/weather/")

table = driver.find_element(By.CSS_SELECTOR,'[id=zebra fw tb-theme]')