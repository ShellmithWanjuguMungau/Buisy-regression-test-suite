from selenium.webdriver.common.by import By
from behave import given, when, then

@given("User opens buisy login page")
def user_opens_buisy_login_page(context):
    context.driver.get("https://dev.burnmfgsystems.com/")

@when("enter correct email")
def enter_correct_email(context):
    context.driver.find_element(By.CSS_SELECTOR, '[name*="username"]').send_keys("qa.software@burnmfg.com")

@when("enter correct password")
def enter_correct_password(context):
    context.driver.find_element(By.CSS_SELECTOR, '[name*="password"]').send_keys("123@Team")

@when("navigate to main login url")
def navigate_to_main_page(context):
    # to bypass authentication
    context.driver.get("https://dev.burnmfgsystems.com/")


@then("confirm welcome is displayed")
def confirm_welcome_message(context):
    actual_text=context.driver.find_element(By.XPATH, "//a[contains(text(),'Welcome')]").text
    print(actual_text)

    expected_text='welcomllle'
    assert expected_text in actual_text, f'error message: Expected text{expected_text} not found in {actual_text}'



