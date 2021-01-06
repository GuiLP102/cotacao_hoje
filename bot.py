import time
from extract_and_post.Tweets import Tweet
import schedule
from datetime import datetime
import pytz


print("online")

def tweetar():
    Tweet().fazer_tweet()
    time_zone = pytz.timezone('Brazil/East')
    hora = datetime.now(time_zone).strftime("%H:%M:%S")
    print(f"Tweet enviado as {hora}")


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
    time.sleep(1)
