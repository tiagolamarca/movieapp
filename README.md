# MoviesApp - Aplicação Web de Pesquisa de Filmes

Este projeto tem como objetivo desenvolver uma aplicação web onde o usuário poderá pesquisar por títulos de filmes, retornados pela API do [The Movie DB]. O usuário poderá marcar filmes como assistidos, favoritos ou que pretende assistir, com os dados sendo armazenados em um banco de dados MySQL. A aplicação também é conteinerizada usando Docker.

## Funcionalidades

- **Tela de Login e Registro**: O usuário pode criar uma conta e fazer login.
- **Pesquisa de Filmes**: O usuário pode buscar por títulos de filmes usando a API "The Movie DB" (ou outra API).
- **Marcar Filmes**: O usuário pode marcar os filmes com as seguintes opções:
  - **ASSISTIDO**
  - **FAVORITOS**
  - **PRETENDE ASSISTIR**
- **Persistência de Dados**: As informações de filmes marcados serão armazenadas em um banco de dados SQL (MySQL, PostgreSQL, SQLite, SQLServer, etc.).
- **Tela Inicial Personalizada**: A tela inicial do usuário exibe a lista de filmes incluídos nas categorias "Assistido", "Favoritos" e "Pretende Assistir", mostrando o título e a capa dos filmes.
- **Detalhes do Filme**: Ao clicar na capa do filme, serão exibidas informações básicas, como:
  - Nome
  - Diretor
  - Sinopse
  - Duração
  - Ano de lançamento
- **Conteinerização com Docker**: A aplicação é conteinerizada para facilitar o deploy e execução em qualquer ambiente.

## Tecnologias Utilizadas

- **Backend**: Python (Flask) 
- **Banco de Dados**: MySQL
- **API de Filmes**: [The Movie DB API]
- **Frontend**: HTML, CSS, JavaScript 
- **Docker**: Utilizado para conteinerização da aplicação.

## Como Executar o Projeto

Clone o repositório e execute a aplicação:
   ```bash
   git clone https://github.com/tiagolamarca/movieapp.git
   cd movieapp
   sudo docker-compose up --build

## Como Acessar a Aplicação

Acesse a aplicação no navegador no endereço: http://localhost:5000

## Contribuidores

Tiago Lamarca


