from playwright.sync_api import Page
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage

class HomePage(BasePage):
    url = "https://automationexercise.com/"

    def click_accept_cookies(self):
        return self.page.locator(HomePageLocators.ACCEPT_COOKIES_BUTTON).click()

    # If I see "home" icon, then page is visible
    def is_home_page_visible(self):
        return self.page.locator(HomePageLocators.HOME_ICN).is_visible()

    def click_login_and_signup_button(self):
        return self.page.locator(HomePageLocators.LOGIN_AND_SIGNUP_BUTTON).click()