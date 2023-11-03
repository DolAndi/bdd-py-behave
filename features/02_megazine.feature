# language: pt

Funcionalidade: Teste de busca por produto no Magazine Luiza
  Como um usuário do Magazine Luiza
  Eu quero buscar por um produto
  Para que eu possa encontrar resultados relacionados ao produto desejado

  Esquema do Cenário: Pesquisar por um produto
    Dado que estou na página inicial do Magazine Luiza
    Quando eu pesquiso por "<produto>" na barra de busca
    Então eu vejo resultados de busca relacionados ao "<produto>"

      Exemplos:
      | produto |
      | samsung |
