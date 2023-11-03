from behave import given, when
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('que o usuário esteja na página principal de esportes do UOL')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://www.uol.com.br/esporte/")

@when('o usuário clica na notícia com a manchete "{headline}"')
def step_impl(context, headline):
    news_article = context.browser.find_element(By.XPATH, f"//*[contains(text(),'{headline}')]")
    news_article.click()

@then('o usuário é redirecionado para a página da notícia')
def step_impl(context):
    assert context.browser.current_url != "https://www.uol.com.br/esporte/"

@then('a manchete "{headline}" é exibida na página da notícia')
def step_impl(context, headline):
    assert headline in context.browser.page_source
    context.browser.quit()
