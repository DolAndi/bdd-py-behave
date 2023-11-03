from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que estou na página de teste de clique')
def open_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://testpages.eviltester.com/styled/key-click-display-test.html")

@when('eu dou um duplo clique no botão Click Me')
def double_click_button(context):
    wait = WebDriverWait(context.driver, 10) 
    click_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'styled-click-button')]")))
    actions = ActionChains(context.driver)
    actions.double_click(click_field).perform()

@then('o texto "{texto}" deve ser exibido')
def validation_result(context, texto):
    wait = WebDriverWait(context.driver, 10) 
    click_validation = wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[contains(@id, 'event1') and contains(text(), '{texto}')]")))
    actual_text = click_validation.text 
    assert texto == actual_text 