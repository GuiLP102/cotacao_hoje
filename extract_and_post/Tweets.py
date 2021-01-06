import tweepy
from auth import tokens
from extract_and_post.Moedas import Moeda
from datetime import datetime
import pytz


class Tweet:
    # passa o link e o tipo da moeda para a classe Moeda, e cria e retorna uma lista com as moedas formatadas
    @staticmethod
    def cambios():
        dolar = Moeda("https://www.remessaonline.com.br/cotacao/cotacao-dolar", "dolar")
        euro = Moeda("https://www.remessaonline.com.br/cotacao/cotacao-euro", "euro")
        libra = Moeda("https://www.remessaonline.com.br/cotacao/cotacao-libra-esterlina", "libra")
        iene = Moeda("https://www.remessaonline.com.br/cotacao/cotacao-iene-japones", "iene")
        moedas_formatadas = [dolar.formatar_dados(), euro.formatar_dados(), libra.formatar_dados(),
                             iene.formatar_dados()]
        return moedas_formatadas

    def fazer_tweet(self):  # loga na api do twitter faz o tweet todo formatado
        auth = tweepy.OAuthHandler(tokens.consumer_key, tokens.consumer_secret)
        auth.set_access_token(tokens.access_token, tokens.access_token_secret)
        api = tweepy.API(auth)
        time_zone = pytz.timezone('Brazil/East')
        hora = datetime.now(time_zone).strftime("%H")
        minutos = datetime.now(time_zone).strftime("%M")
        try:
            api.update_status(f"🌎 Cotação das {hora}h{minutos}min 🌎\n"
                              f"Dólar . . . . . . . . . . . . . . . . . . R$ {self.cambios()[0]}\n"
                              f"Euro . . . . . . . . . . . . . . . . . .  R$ {self.cambios()[1]}\n"
                              f"Libra . . . . . . . . . . . . . . . . . . R$ {self.cambios()[2]}\n"
                              f"Iene . . . . . . . . . . . . . . . . . .  R$ {self.cambios()[3]}\n")
        except tweepy.error.TweepError:
            print("******Tweet duplicado ou limite de caracteres antingido******")
