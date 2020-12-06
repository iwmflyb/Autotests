from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_URL_NAME = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    BUTTON_ADD_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.TAG_NAME, "h1")
    ADDED_NAME = (By.XPATH, '//div[1]/div[@class="alertinner "]/strong')
    ITEM_PRICE = (By.XPATH, '//div[@id="content_inner"]/article/div/div/p[@class="price_color"]')
    BASKET_PRICE = (By.XPATH, '//div/div[@class="alertinner "]/p/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//div[1]/div[@class="alertinner "]/strong')
