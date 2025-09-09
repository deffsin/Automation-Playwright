import pytest
from playwright.async_api import Page
from pages.home_page import HomePage
from pages.enter_account_information_page import EnterAccountInformationPage

@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 1080, 'width': 1920})
    yield page

@pytest.fixture()
def home(page):
    return HomePage(page)

@pytest.fixture()
def enter_account_information(page):
    return EnterAccountInformationPage(page)

# @pytest.fixture()
# def fill_form(page, selector, value):
#     field = page.locator(selector)
#     field.fill(value)
