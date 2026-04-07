# 📰 News Data API

API ainda sendo desenvolvida em Python para coleta automática de notícias através de Web Scraping e disponibilização dos dados via API REST.
O projeto realiza a extração de notícias, armazena as informações em banco de dados e disponibiliza os dados em formato JSON para consumo por aplicações, dashboards ou sistemas externos.

---

##  Funcionalidades:

- Coleta automática de notícias via Web Scraping
- Armazenamento das notícias em banco de dados
- API REST para consulta dos dados
- Endpoint de estatísticas das notícias
- Retorno de dados em formato JSON
- Sistema de prevenção de duplicidade de notícias

---

##  Arquitetura do Projeto


Web Scraping

Banco de Dados (SQLite)

API REST (Django + Django REST Framework)

JSON para consumo de aplicações




##  Endpoints da API

## Listar notícias

## GET /api/noticias


Exemplo de retorno:

```json
[
 {
   "id": 1,
   "titulo": "Example News Title",
   "link": "https://news-link.com",
   "fonte": "Hacker News",
   "data": "2026-03-10"
 }
]


Estatísticas da API:
GET /api/stats


Exemplo de retorno:
{
 "total_noticias": 59,
 "fontes": [
   {
     "fonte": "Hacker News",
     "total": 59
   }
 ],
 "ultima_noticia": "Example news title"
}


 Tecnologias utilizadas:

1- Python
2- Django
3- Django REST Framework
4- BeautifulSoup
5- SQLite


Objetivo do projeto
#Este projeto foi desenvolvido com o objetivo de praticar:
1- Engenharia de dados
2- Web Scraping
3- Desenvolvimento de APIs REST
4- Manipulação e disponibilização de dados
5- Colocar em prática conhecimentos que estão sendo obtidos no curso = Python backend Coursera
