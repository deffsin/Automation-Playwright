import pytest
from playwright.async_api import Page
from pages.home_page import HomePage

@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 1080, 'width': 1920})
    yield page

@pytest.fixture()
def home(page):
    return HomePage(page)