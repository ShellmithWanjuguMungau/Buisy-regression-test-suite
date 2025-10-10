from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from behave import given, when, then

@given("User opens buisy login page")
def user_opens_buisy_login_page(context):
    context.driver.get("https://dev.burnmfgsystems.com/")
#     https://training.burnmfgsystems.com/

@when("enter correct email")
def enter_correct_email(context):
    context.driver.find_element(By.CSS_SELECTOR, '[name*="username"]').send_keys("qa.software@burnmfg.com")

@when("enter correct password")
def enter_correct_password(context):
    context.driver.find_element(By.CSS_SELECTOR, '[name*="password"]').send_keys("123@Team")

@when('click login button')
def click_login(context):
    context.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    # sleep(3)


@when("navigate to main login url")
def navigate_to_main_page(context):
    # to bypass authentication
    context.driver.wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[class="widget-main"]'))
    )
    context.driver.get("https://dev.burnmfgsystems.com/")
    # sleep(3)

@when("enter incorrect email")
def enter_incorrect_email(context):
    context.driver.find_element(By.CSS_SELECTOR, '[name*="username"]').send_keys("qaaa.software@burnmfg.com")


@when("enter incorrect password")
def enter_correct_password(context):
    context.driver.find_element(By.CSS_SELECTOR, '[name*="password"]').send_keys("1233@Team")


@when("Click from the dropdown {language}")
def click_language(context,language):
    dropdown=context.driver.find_element(By.ID, "slang")
    select=Select(dropdown)
    select.select_by_value(language)

@when("click the stock and cash app tracker card")
def click_the_stock_and_cash_app(context):
    context.driver.wait.until(
        EC.invisibility_of_element((By.ID, "loader"))
    )
    context.driver.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[href*="stock"]'))
    ).click()


@then("confirm welcome is displayed")
def confirm_welcome_message(context):
    actual_text=context.driver.wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Welcome')]"))
    ).text
    print(actual_text)

    expected_text='Welcome'
    print(expected_text)
    assert expected_text in actual_text, f'error message: Expected tex:  {expected_text} not found in {actual_text}'
    # assert expected_text in actual_text, f'Expected text {expected_text} not found in {actual_text}'

@then("Invalid credentials error message is displayed")
def invalid_credentials_message(context):
    actual_text=context.driver.wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Invalid credentials')]"))
    ).text
    print(actual_text)
    expected_text='Invalid credentials'
    assert expected_text in actual_text, f'error message: Expected text {expected_text} not found in {actual_text}'


@then ("confirm {welcome_message} is displayed")
def confirm_welcome_message(context, welcome_message):
    actual_text=context.driver.wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h4"))
    ).text
    expected_text=welcome_message
    assert expected_text in actual_text, f'expected text {expected_text} not found in {actual_text}'

@then("Confirm that 9 cards are displayed")
def confirm_9_cards_displayed(context):
    dashboard_cards=context.driver.wait.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '[class*="dashboard_tab"]'))
    )
    print(len(dashboard_cards))
    assert len(dashboard_cards) == 9 , 'Excpected 9 cards displayed but got {}'.format(len(dashboard_cards))




