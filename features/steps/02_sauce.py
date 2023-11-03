from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que estou na página de login do SauceDemo')
def open_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

@when('eu insiro meu nome de usuário "{username}"')
def step_when_enter_username(context, username):
    wait = WebDriverWait(context.driver, 10) 
    username_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@placeholder, 'Username')]")))
    username_field.send_keys(username)

@when('eu insiro minha senha "{password}"')
def step_when_enter_password(context, password):
    wait = WebDriverWait(context.driver, 10) 
    password_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@placeholder, 'Password')]")))
    password_field.send_keys(password)

@when('eu clico no botão de login')
def step_when_click_login_button(context):
    wait = WebDriverWait(context.driver, 10)  
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'submit-button btn_action')]")))
    search_button.click()

@then('eu devo ser redirecionado para a página do catálogo de produtos')
def validation_result(context):
    assert "inventory.html" in context.driver.current_url
