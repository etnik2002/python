from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import requests

website = 'https://phones.mk/'
path = "C:/Users/etnik/PycharmProjects/getHTML/venv/Lib/site-packages/chromedriver_binary/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(website)

namesArray = []


products_name = driver.find_elements(By.CLASS_NAME, 'product-name')
# for names in products_name:
#     namesss=names.text
#     print(namesss)

products_price = driver.find_elements(By.CLASS_NAME, 'product-price')
for price in products_price:
    print(price.text)
 
products_image = driver.find_elements(By.CLASS_NAME, 'product-image')
for image in products_image:
    print(image.get_attribute("src"))

for names in products_name:
    json_names = json.dumps(names.text)
    namesJSONarr = []
    name = names.text
    namesJSONarr.append(names.text)
    print(namesJSONarr)

    f = open("data.json", "a")
    f.write(str(name.split(",")))
    f.close()

f = open("data.json", "r")
names_json = f.read()
name = json.dumps(names_json)
data = requests.post('http://localhost:5116/postdata', json={"names": name}) 


driver.quit()
