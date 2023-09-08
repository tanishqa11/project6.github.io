from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import time
# Load the extracted data from local storage
with open(r'extracted_data.json', 'r') as f:
    extracted_data = json.load(f)
driver = webdriver.Chrome()
driver.get(r'C:\Users\Dell\Downloads\chromedriver-win32')
driver.get('https://tanishqa11.github.io/project6.github.io/form.html')
driver.find_element("id",'name').send_keys(extracted_data[0]['name'])
driver.find_element("id",'phone').send_keys(extracted_data[0]['phone'])
driver.find_element("id",'address').send_keys(extracted_data[0]['user_address'])
driver.find_element("id",'lname').send_keys(extracted_data[0]['test'])
driver.find_element("id",'code').send_keys(extracted_data[0]['source_type'])
driver.find_element("id",'mail').send_keys(extracted_data[0]['mail'])
driver.find_element("id",'password').send_keys(extracted_data[0]['collection_date'])
radio2 = driver.find_element("xpath",(f"//input[@name=\"gender\"][@value=\"{extracted_data[0]['gender']}\"]"))
radio2.click()
if int(extracted_data[0]["age"])<18:
    age="below 18"
elif int(extracted_data[0]["age"])>18 and int(extracted_data[0]["age"])<25:
    age="18-25"
if int(extracted_data[0]["age"])>25 and int(extracted_data[0]["age"])<40:
    age="25-40"
if int(extracted_data[0]["age"])>40:
    age="40+" 
age_select=driver.find_element("id","age")
select=Select(age_select)
select.select_by_value(age)
# Thread.sleep(2000)
driver.find_element("name",'submit').click()
# Close the WebDriver
time.sleep(100)
