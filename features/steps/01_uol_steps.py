from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('que eu estou na página inicial do site "{url}"')
def step_open_browser(context, url):
    context.driver = webdriver.Chrome()  # Certifique-se de que o ChromeDriver esteja instalado e no PATH.
    context.driver.get(url)

@when('eu clico em uma notícia')
def step_click_news(context):
    # Substitua 'noticia_xpath' pelo seletor real da notícia no site.
    noticia_xpath = "//a[contains(@class, 'noticia')]"
    context.driver.find_element(By.XPATH, noticia_xpath).click()

@then('eu sou direcionado para uma página com a mesma manchete')
def step_verify_redirect(context):
    # Substitua 'manchete_xpath' pelo seletor real da manchete na página de destino.
    manchete_xpath = "//h1[contains(@class, 'manchete')]"
    manchete_inicial = context.driver.find_element(By.XPATH, manchete_xpath).text

    context.driver.back()  # Voltar para a página inicial.
    
    # Clique em outra notícia e verifique a manchete na página de destino.
    context.driver.find_element(By.XPATH, noticia_xpath).click()
    manchete_atual = context.driver.find_element(By.XPATH, manchete_xpath).text
    
    assert manchete_inicial == manchete_atual

    # Feche o navegador após o teste.
    context.driver.quit()
