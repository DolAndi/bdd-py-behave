# language: pt

Funcionalidade: Verificação de manchete de notícias esportivas
  Como um usuário do UOL Esportes
  Eu quero clicar em uma notícia
  Para que eu possa ver a página da notícia com a mesma manchete

  Esquema do Cenário: Usuário clica em uma notícia e é redirecionado para a página da notícia com a manchete correspondente
    Dado que o usuário esteja na página principal de esportes do UOL
    Quando o usuário clica na notícia com a manchete "<manchete>"
    Então o usuário é redirecionado para a página da notícia
    E a manchete "<manchete>" é exibida na página da notícia

    Exemplos:
    | manchete                                                                    |
    | Enfim, reconhecimento: Argentina se rende a Cano após sucesso no Fluminense |
