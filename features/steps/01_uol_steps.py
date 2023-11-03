from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

@given('que o usuário esteja na página principal de esportes do UOL')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://www.uol.com.br/esporte/")

@when('o usuário clica na notícia com a manchete "{headline}"')
def step_impl(context, headline):
    try:
        news_article = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(),'{headline}')]"))
        )
        news_article.click()
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Erro: {e}")
        context.browser.quit()
        assert False, "Elemento não encontrado ou não é clicável"

@then('o usuário é redirecionado para a página da notícia')
def step_impl(context):
    assert context.browser.current_url != "https://www.uol.com.br/esporte/"

@then('a manchete "{headline}" é exibida na página da notícia')
def step_impl(context, headline):
    assert headline in context.browser.page_source
    context.browser.quit()
