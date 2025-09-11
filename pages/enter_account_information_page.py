from locators.enter_account_information_page_locators import EnterAccountInformationPageLocators
from pages.base_page import BasePage


class EnterAccountInformationPage(BasePage):

    def is_enter_account_information_text_visible(self):
        return self.page.locator(EnterAccountInformationPageLocators.ENTER_ACCOUNT_INFORMATION_TEXT).is_visible()

    def enter_account_information(self, title, password):
        title = title.lower().rstrip(".")
        if title == "mr":
            self.page.locator(EnterAccountInformationPageLocators.FIRST_TITLE_RADIO_BUTTON).check()
        elif title == "mrs":
            self.page.locator(EnterAccountInformationPageLocators.SECOND_TITLE_RADIO_BUTTON).check()
        else:
            raise ValueError("Title must be 'Mr' or 'Mrs'")

        self.page.locator(EnterAccountInformationPageLocators.PASSWORD_INPUT).fill(password)

    def enter_date_of_birth(self, day, month, year):
        self.page.locator(EnterAccountInformationPageLocators.DATE_OF_BIRTH_DAY).select_option(str(day))
        self.page.locator(EnterAccountInformationPageLocators.DATE_OF_BIRTH_MONTH).select_option(str(month))
        self.page.locator(EnterAccountInformationPageLocators.DATE_OF_BIRTH_YEAR).select_option(str(year))
