#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from tabulate import tabulate
import calendar
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://myabb.in/')
user_name = driver.find_element_by_xpath('//*[@id="DUser"]')
user_name.send_keys(os.environ.get("username"))
password = driver.find_element_by_xpath('//*[@id="Pwd"]')
password.send_keys(os.environ.get("password"))
login_button = driver.find_element_by_xpath('//*[@id="button"]')
login_button.click()

delay = 30
try:
    usage_button = WebDriverWait(driver, delay)\
        .until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="freeze"]/header/div/div[2]/ul/li[11]/a')
            )
        )
except TimeoutException:
    print("Loading took too much time!")

usage_button.click()

try:
    alloted = WebDriverWait(driver, delay).\
        until(EC.presence_of_element_located((By.XPATH, '//*[@id="totalOc"]')))
except TimeoutException:
    print("Loading took too much time!")

used = driver.find_element_by_xpath('//*[@id="totalOctet"]')
remaining = driver.find_element_by_xpath('//*[@id="totalOctets"]')

alloted_GB = round(float(alloted.text)/1000, 2)
used_GB = round(float(used.text)/1000, 2)
remaining_GB = round(float(remaining.text)/1000, 2)

now = datetime.datetime.now()
days_of_month = calendar.monthrange(now.year, now.month)[1]
remaining_days = days_of_month - now.day
remainming_per_day_GB = round(remaining_GB/remaining_days, 2)

table_data = [[alloted_GB, used_GB, remaining_GB, remainming_per_day_GB]]

headers = ['alloted GB', 'used GB', 'remaining GB', 'remaining per day GB']
table = tabulate(table_data, headers=headers, tablefmt='orgtbl')
print(table)

driver.quit()
