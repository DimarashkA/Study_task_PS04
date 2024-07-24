##Часть первая

#from selenium import webdriver
#import time

#browser= webdriver.Firefox()
#browser.get('https://ru.wikipedia.org/wiki/Document_Object_Model')
#browser.save_screenshot("dom.png") #скриншот страницы
#time.sleep(3)
#browser.get('https://ru.wikipedia.org/wiki/Selenium')
#browser.save_screenshot("selenium.png") #скриншот страницы
#time.sleep(3)
#browser.refresh() #перезагрузка страницы
#browser.quit()

##Часть вторая

#from selenium import webdriver
#from selenium.webdriver import Keys
#from selenium.webdriver.common.by import By
#import time

#browser = webdriver.Firefox()
#browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

#assert "Википедия" in browser.title
#time.sleep(5)
#search_box = browser.find_element(By.ID, "searchInput")
#search_box.send_keys("Солнечная система")
#search_box.send_keys(Keys.RETURN)

#time.sleep(5)
#a = browser.find_element(By.LINK_TEXT, "Солнечная система")
#a.click()

##Часть третья

#from selenium import webdriver
#from selenium.webdriver import Keys
#from selenium.webdriver.common.by import By
#import time

#browser = webdriver.Firefox()
#browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

#paragraphs = browser.find_elements(By.TAG_NAME, "p")
#for paragraph in paragraphs:
#    print(paragraph.text)
#    time.sleep(2)
#    input()

#Часть четвертая

from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

# Инициализация веб-драйвера
browser = webdriver.Firefox()

try:
    # Открытие страницы Википедии
    browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

    # Поиск элементов с определенным классом
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)

    if not hatnotes:
        print("Нет элементов с классом 'hatnote navigation-not-searchable'")
    else:
        print(f"Найдено {len(hatnotes)} элементов с классом 'hatnote navigation-not-searchable'")

        # Выбор случайного элемента
        hatnote = random.choice(hatnotes)
        link_element = hatnote.find_element(By.TAG_NAME, "a")

        if link_element:
            link = link_element.get_attribute("href")
            print(f"Переход по ссылке: {link}")

            # Переход по найденной ссылке
            browser.get(link)
        else:
            print("В выбранном элементе нет ссылок")
finally:
    # Закрытие браузера через некоторое время для возможности увидеть результат
    time.sleep(5)  # Увеличьте время, если хотите дольше наблюдать результат
    browser.quit()

