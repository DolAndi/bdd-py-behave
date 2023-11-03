from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que estou na página inicial do Magazine Luiza')
def open_page(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://www.magazineluiza.com.br/')

@when('eu pesquiso por "{produto}" na barra de busca')
def search_product(context, produto):
    wait = WebDriverWait(context.browser, 10)
    search_bar = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@placeholder, 'Busca no Magalu')]")))
    search_bar.send_keys(produto)
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Buscar produto']")))
    search_button.click()

@then('eu vejo resultados de busca relacionados ao "{produto}"')
def validation_result(context, produto):
    assert produto in context.browser.page_source