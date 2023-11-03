from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que estou na página inicial do GauchaZH')
def open_page(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get("https://gauchazh.clicrbs.com.br/esportes/ultimas-noticias/")

@when('eu clico na seção "{secao}"')
def click_section(context, secao):
    wait = WebDriverWait(context.driver, 10) 
    news_article = wait.until(EC.visibility_of_element_located((By.XPATH, f"//span[contains(text(), '{secao}')]")))
    news_article.click()

@then('eu devo ser redirecionado para a página de Futebol Feminino')
def validation_result(context):
    assert context.driver.current_url == "https://gauchazh.clicrbs.com.br/esportes/futebol-feminino/ultimas-noticias/"
