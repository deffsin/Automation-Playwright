class HomePageLocators:
    ACCEPT_COOKIES_BUTTON = ("//button[@class='fc-button fc-cta-consent fc-primary-button']")
    HOME_ICN = ("//i[@class='fa fa-home']")
    LOGIN_AND_SIGNUP_BUTTON = ("//a[@href='/login']")

    # If account is created, user can see these locators
    LOGGED_IN_AS_TEXT = ("//a[contains(., 'Logged in as')]")
    DELETE_ACCOUNT_BUTTON = ("//a[@href='/delete_account']")
    LOGOUT_BUTTON = ("//a[@href='/logout']")

    # After account deletion, user can see this locator
    ACCOUNT_DELETED_TEXT = ("//b[contains(text(), 'Account Deleted!')]")