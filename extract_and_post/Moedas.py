import requests
from bs4 import BeautifulSoup
import re


class Moeda:
    def __init__(self, url, tipo_moeda):  # recebe a url do site de cotação e o tipo da moeda
        self._url = url
        self._tipo_moeda = tipo_moeda

    def coletar_dados(self):  # coleta os dados no site e transforma em uma string
        url = requests.get(self._url)
        soup = BeautifulSoup(url.text, 'html.parser')
        dados_raw = soup.find(class_="style__Text-sc-15flwue-2 cSuXFv").text
        return dados_raw

    def formatar_dados(self):  # formata e retorna a string
        dados_default = "([0-9]{1,2})([,])([0-9]{2})"
        dados_format = re.search(dados_default, self.coletar_dados())
        return f"{dados_format.group(1)},{dados_format.group(3)}"
