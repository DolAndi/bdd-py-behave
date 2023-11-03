# language: pt

Funcionalidade: Teste de Login no SauceDemo
    Como um usuário do SauceDemo
    Eu quero realizar o login
    Para que eu possa acessar a página do catálogo de produtos  
    
  Cenário: Login com sucesso
    Dado que estou na página de login do SauceDemo
    Quando eu insiro meu nome de usuário "standard_user"
    E eu insiro minha senha "secret_sauce"
    E eu clico no botão de login
    Então eu devo ser redirecionado para a página do catálogo de produtos
