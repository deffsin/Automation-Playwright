from others.logging_config import logger
from pages.login_and_signup_page import LoginAndSignupPage
import time

class TestFullRegistrationUserFlow:

    def test_start(self, home, enter_account_information,  page):
        name = "Chris"
        email = "helloworldik999@gmail.com"
        title = "Mr."
        password = "wozor119"

        logger.info("Starting user registration process.")

        logger.info("Opening the home page.")
        home.open()

        logger.info("Accepting cookies on the home page.")
        home.click_accept_cookies()

        assert home.is_home_page_visible(), "Home page is not visible"

        logger.info("Navigating to the login and signup page")
        home.click_login_and_signup_button()

        login_and_signup_page = LoginAndSignupPage(page)
        logger.info("Verifying the presence of 'New User Signup!' text.")
        assert login_and_signup_page.is_new_user_signup_text_visible(), "'New User Signup!' text is not visible"
        logger.info("Filling out the signup form")
        login_and_signup_page.fill_signup_form(name=name, email=email)
        logger.info(f"Clicking the signup button for user: {name} with email: {email}.")
        login_and_signup_page.click_signup_button()

        logger.info(f"Verifying the presence of 'Enter account information' text.'")
        assert enter_account_information.is_enter_account_information_text_visible(), "'Enter account information' text is not visible"
        enter_account_information.enter_account_information(title=title, password=password)

        enter_account_information.enter_date_of_birth(day=4, month=9, year=2000)

        time.sleep(3)