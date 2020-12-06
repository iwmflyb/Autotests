from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')


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


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p[1]')

