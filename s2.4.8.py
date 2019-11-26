from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pyperclip

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 15 секунд, пока цена не станет 100
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element_by_id("book")
    button.click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    browser.execute_script('return arguments[0].scrollIntoView(true);', input1)
    input1.send_keys(y)

    button = browser.find_element_by_id("solve")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

    pyperclip.copy(browser.switch_to.alert.text.split(': ')[-1])

    print("Тест успешно завершен. 5 сек на закрытие браузера...")


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

#не забываем пустую строку

