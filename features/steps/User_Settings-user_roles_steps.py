from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from behave import *
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@when("click user settings")
def click_user_settings(context):
    context.driver.wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[href="#UserSettings"]'))
    ).click()

@when("click user roles")
def click_user_roles(context):
    context.driver.wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[href="#UserRoles"]'))
    ).click()


@Then("verify {title} is displayed")
def verify_user_settings(context, title):
    actual_text=context.driver.wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h1"))
    ).text
    print(actual_text)
    title="User roles"
    assert actual_text in title,f'{actual_text} is not found in {title}'

@then("verify 13 records are displayed by footer info")
def verify_user_roles(context):
    # sleep(5)
    context.driver.wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="dataTables_wrapper no-footer"]'))
    )

    actual_text=context.driver.wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="dataTables_info"]'))
    ).text
    Expected_text="Showing 1 to 13 "
    assert Expected_text in actual_text,f'{actual_text} is not found in {Expected_text}'