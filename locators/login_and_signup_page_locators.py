class LoginAndSignupPageLocators:
    # Login
    LOGIN_TO_YOUR_ACCOUNT_TEXT = ("//h2[contains(text(), 'Login to your account')]")
    LOGIN_EMAIL_FIELD = ("input[data-qa='login-email']")
    LOGIN_PASSWORD_FIELD = ("input[data-qa='login-password']")
    LOGIN_ERROR_MESSAGE_TEXT = ("//p[contains(text(), 'Your email or password is incorrect!')]")
    LOGIN_BUTTON = ("button[data-qa='login-button']")

    # Register
    NEW_USER_SIGNUP_TEXT = ("//h2[contains(text(), 'New User Signup!')]")
    NAME_FIELD = ("input[data-qa='signup-name']")
    EMAIL_FIELD = ("input[data-qa='signup-email']")
    SIGNUP_BUTTON = ("button[data-qa='signup-button']")

    # After successful registration user can see this text
    ACCOUNT_CREATED_TEXT = ("//b[contains(text(), 'Account Created')]")