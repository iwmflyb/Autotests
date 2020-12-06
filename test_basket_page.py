import pytest
from .pages.basket_page import BasketPage


@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com", marks=pytest.mark.xfail)])
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.basket_should_be_empty()
    page.basket_empty_message_is_displayed()
