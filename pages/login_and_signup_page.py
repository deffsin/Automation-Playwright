from locators.login_and_signup_page_locators import LoginAndSignupPageLocators
from pages.base_page import BasePage

class LoginAndSignupPage(BasePage):

    def is_new_user_signup_text_visible(self):
        return self.page.locator(LoginAndSignupPageLocators.NEW_USER_SIGNUP_TEXT)

    def fill_signup_form(self, name, email):
        name_input = self.page.locator(LoginAndSignupPageLocators.NAME_FIELD)
        email_input = self.page.locator(LoginAndSignupPageLocators.EMAIL_FIELD)

    def click_signup_button(self):
        return self.page.locator(LoginAndSignupPageLocators.SIGNUP_BUTTON)
