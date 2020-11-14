from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_page1(self):

            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector(".first_block .first")
            input1.send_keys("name")
            input2 = browser.find_element_by_css_selector(".first_block .second")
            input2.send_keys("surname")
            input3 = browser.find_element_by_css_selector(".first_block .third")
            input3.send_keys("email@email.com")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text1 = welcome_text_elt.text

            self.assertEqual(welcome_text1, "Congratulations! You have successfully registered!",
                             "Should be congratulation message")

            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_page2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("name")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("surname")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("email@email.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text2 = welcome_text_elt.text

        self.assertEqual(welcome_text2, "Congratulations! You have successfully registered!",
                         "Should be congratulation message")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()