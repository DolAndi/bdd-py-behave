# Arquivo: uol_esporte.feature

Funcionalidade: Verificar redirecionamento de notícia no site UOL Esporte

  Cenário: Verificar redirecionamento de notícia
    Dado que estou na página inicial do site "https://www.uol.com.br/esporte/"
    Quando eu clico em uma notícia
    Então eu deveria ser redirecionado para uma página que mostra a mesma manchete
