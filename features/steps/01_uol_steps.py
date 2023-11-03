from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('que o usuário esteja na página principal de esportes do UOL')
def open_page(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://www.uol.com.br/esporte/")

@when('o usuário clica na manchete principal')
def user_action(context):
    news_article = context.browser.find_element(By.XPATH, f"//*[contains(@class, 'positioning-bottom')]")
    news_article.click()

@then('o usuário é redirecionado para a página da notícia')
def validation_resultUrl(context):
    assert context.browser.current_url != "https://www.uol.com.br/esporte/"

@then('a manchete "{headline}" é exibida na página da notícia')
def validation_result(context):
    news_article = context.browser.find_element(By.XPATH, f"//h1[contains(@class, 'title')]")
    assert news_article in context.browser.page_source
