import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019", marks=pytest.mark.xfail)])
@pytest.mark.skip(reason="Not in the scope")
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name()
    page.should_be_correct_price()


@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019", marks=pytest.mark.xfail)])
@pytest.mark.skip(reason="Not in the scope")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019", marks=pytest.mark.xfail)])
@pytest.mark.skip(reason="Not in the scope")
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019", marks=pytest.mark.xfail)])
@pytest.mark.skip(reason="Not in the scope")
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.solve_quiz_and_get_code()
    page.should_dissapear_of_success_message()


@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/", marks=pytest.mark.xfail)])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/", marks=pytest.mark.xfail)])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
