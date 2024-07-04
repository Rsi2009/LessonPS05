import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://divan.ru/category/svet")
time.sleep(5)

svets = driver.find_elements(By.CLASS_NAME, '_Ud0k')
print(f"Найдено элементов: {len(svets)}")

parsed_data = []

for svet in svets:
    try:
        name = svet.find_element(By.CSS_SELECTOR, 'div.wYUX2 span').text
        price = svet.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        link = svet.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        parsed_data.append([name, price, link])
        print(f"Название: {name}, Цена: {price}, Ссылка: {link}")
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

driver.quit()

with open("svet.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Название', 'цена', 'ссылка'])
    writer.writerows(parsed_data)


