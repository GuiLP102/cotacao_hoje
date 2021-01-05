import time
from extract_and_post.Tweets import Tweet
import schedule
from datetime import datetime


print("online")

def tweetar():
    Tweet().fazer_tweet()
    hora = datetime.now().strftime("%H")
    minutos = datetime.now().strftime("%M:%S")
    print(f"Tweet enviado as {int(hora)-3}:{minutos}")


schedule.every().day.at("01:00").do(tweetar)
schedule.every().day.at("04:00").do(tweetar)
schedule.every().day.at("07:00").do(tweetar)
schedule.every().day.at("10:00").do(tweetar)
schedule.every().day.at("13:00").do(tweetar)
schedule.every().day.at("16:00").do(tweetar)
schedule.every().day.at("19:00").do(tweetar)
schedule.every().day.at("22:00").do(tweetar)


while True:
    schedule.run_pending()
    time.sleep(5)
