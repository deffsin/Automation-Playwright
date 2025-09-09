from others.logging_config import logger
from pages.login_and_signup_page import LoginAndSignupPage

class TestFullRegistrationUserFlow:

    def test_start(self, home, page):
        name = "Chris"
        email = "helloworldik999@gmail.com"

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


    #     login_and_signup_page.click_signup_button()
    #
    # def complete_account_information(self):
    #     logger.info("Completing account information process.")
    #     add_account_information_page = AddAccountInformationPage(self.driver)
    #
    #     logger.info("Verifying the presence of 'ENTER ACCOUNT INFORMATION' text.")
    #     assert add_account_information_page.is_account_information_text_visible(), "'ENTER ACCOUNT INFORMATION' text is not visible"
    #
    #     logger.info("Filling in account information and address details.")
    #     add_account_information_page.fill_account_information(password="Wozor119")
    #     add_account_information_page.fill_address_information(
    #         first_name="Denis",
    #         last_name="Sss",
    #         company="HelloWorld",
    #         address_one="Hobujaama 2",
    #         address_two="Something",
    #         state="Harjumaa",
    #         city="Tallinn",
    #         zipcode="14512",
    #         mobile_number="+372555555"
    #     )
    #
    # def delete_user_account(self):
    #     logger.info("Starting account deletion process.")
    #     home_page = HomePage(self.driver)
    #     login_and_register_page = LoginAndRegisterPage(self.driver)
    #
    #     logger.info("Verifying 'ACCOUNT CREATED!' text is visible.")
    #     assert login_and_register_page.account_created_text_visible(), "'ACCOUNT CREATED!' text is not visible"
    #     logger.info("Clicking the 'Continue' button after account creation.")
    #     home_page.continue_button_click()
    #
    #     logger.info("Verifying user is logged in as their username.")
    #     assert home_page.logged_in_as_text_visible(), "'Logged in as username' text is not visible"
    #     logger.info("Clicking the 'Delete Account' button.")
    #     home_page.delete_account()
    #
    #     logger.info("Verifying 'ACCOUNT DELETED!' text is visible.")
    #     home_page.account_deleted_text_visible()
    #     logger.info("Clicking the 'Continue' button after account deletion.")
    #     home_page.continue_button_click()