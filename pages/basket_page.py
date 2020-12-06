from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def basket_empty_message_is_displayed(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
