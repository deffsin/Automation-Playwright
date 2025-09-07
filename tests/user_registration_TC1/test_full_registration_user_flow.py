from pages.home_page import HomePage
from others.logging_config import logger

class TestFullRegistrationUserFlow:

    def test_start(self, page):
        logger.info("Starting user registration process.")
        home = HomePage(page)

        logger.info("Opening the home page.")
        home.open()

        logger.info("Accepting cookies on the home page.")
        home.click_accept_cookies()

        assert home.is_home_page_visible(), "Home page is not visible"

        logger.info("Navigating to the login and signup page")
        home.click_login_and_signup_button()