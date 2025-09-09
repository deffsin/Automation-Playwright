from locators.login_and_signup_page_locators import LoginAndSignupPageLocators
from pages.base_page import BasePage

class LoginAndSignupPage(BasePage):

    def is_new_user_signup_text_visible(self):
        return self.page.locator(LoginAndSignupPageLocators.NEW_USER_SIGNUP_TEXT).is_visible()

    def fill_signup_form(self, name, email):
        self.page.locator(LoginAndSignupPageLocators.NAME_FIELD).fill(name)
        self.page.locator(LoginAndSignupPageLocators.EMAIL_FIELD).fill(email)

    def click_signup_button(self):
        self.page.locator(LoginAndSignupPageLocators.SIGNUP_BUTTON).click()
