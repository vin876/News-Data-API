import os
import sys
import django
import requests
from bs4 import BeautifulSoup

print("Script iniciado...")

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()

from noticias.models import Noticia

url = "https://news.ycombinator.com/"
print("Acessando site...")

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titulos = soup.select(".titleline a")

print(f"Noticias encontradas: {len(titulos)}")

for titulo in titulos:

    texto = titulo.text
    link = titulo["href"]

Noticia.objects.get_or_create(
    link=link,
    defaults={
        "titulo": titulo,
        "fonte": "Hacker News"
    }
)

print("Noticias salvas com sucesso!")
