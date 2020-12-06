from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def adding_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        basket_button.click()

    def should_be_correct_name(self):
        assert self.browser.find_element(*ProductPageLocators.ADDED_NAME).text == self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def should_be_correct_price(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text == self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
