class EnterAccountInformationPageLocators:
    # ENTER ACCOUNT INFORMATION
    ENTER_ACCOUNT_INFORMATION_TEXT = ("//b[contains(text(), 'Enter Account Information')]")

    FIRST_TITLE_RADIO_BUTTON = "input#id_gender1" # Mr
    SECOND_TITLE_RADIO_BUTTON = "input#id_gender2" # Mrs
    PASSWORD_INPUT = "input#password"

    DATE_OF_BIRTH_DAY = "select#days"
    DATE_OF_BIRTH_MONTH = "select#months"
    DATE_OF_BIRTH_YEAR = "select#years"