import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

def search_wikipedia(query):
    search_box = browser.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

def list_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    print("Нажмите Enter для листания параграфов и Esc для прерывания.")
    should_stop = False

    def on_esc(e):
        nonlocal should_stop
        should_stop = True

    keyboard.on_press_key("esc", on_esc)

    for p in paragraphs:
        if should_stop:
            print("Листание параграфов прервано.")
            break

        print(p.text)
        print("\n---\n")
        while True:
            if keyboard.is_pressed("enter"):
                break
            elif keyboard.is_pressed("esc"):
                should_stop = True
                break
        time.sleep(0.1)  # Небольшая задержка для избежания слишком быстрой проверки клавиш
    keyboard.unhook_all()  # Убираем все хуки
    print("Конец статьи или листание прервано. Возвращение к меню.")
    time.sleep(2)

def navigate_links():
    links = browser.find_elements(By.XPATH, '//div[@id="mw-content-text"]//a[starts-with(@href, "/wiki/")]')
    if links:
        random_link = random.choice(links)
        link_text = random_link.text
        link_href = random_link.get_attribute("href")
        print(f"Переход по случайной ссылке: {link_text}")
        browser.get(link_href)
    else:
        print("Связанные страницы не найдены.")

# Инициализация браузера
browser = webdriver.Firefox()

try:
    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")

    initial_query = input("Введите начальный запрос: ")
    search_wikipedia(initial_query)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == "1":
            list_paragraphs()
        elif choice == "2":
            navigate_links()
        elif choice == "3":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор, попробуйте снова.")
finally:
    browser.quit()
