from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd
import matplotlib.pyplot as plt


# Инициализация драйвера
driver = webdriver.Firefox()
driver.get('https://www.divan.ru/category/divany-i-kresla')

# Ожидание загрузки элементов с ценами
wait = WebDriverWait(driver, 10)
prices = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@data-testid='price']")))

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        # Проверяем класс элемента
        if 'KIkOH' in price.get_attribute('class'):
            # Получаем весь текст элемента, включая вложенные элементы
            price_text = price.get_attribute('textContent').replace('руб.', '').replace(' ', '').strip()
            print(price_text)  # Отладочный вывод
            if price_text:  # Проверяем, что текст не пустой
                try:
                    # Преобразуем строку к числу и обратно к строке для удаления любых нежелательных символов
                    price_numeric = str(int(price_text))
                    writer.writerow([price_numeric])
                except ValueError:
                    print(f"Cannot convert {price_text} to integer.")  # Сообщение об ошибке, если не удалось преобразовать

# Закрытие драйвера
driver.quit()

df = pd.read_csv('prices.csv')
# Вычисление средней цены
average_price = df['Price'].mean()
print(f"Средняя цена: {average_price}")

# Загрузка данных из CSV-файла
file_path = 'prices.csv'
data = pd.read_csv(file_path)

# Предположим, что столбец с ценами называется 'price'
prices = data['Price']

# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Показать гистограмму
plt.show()
