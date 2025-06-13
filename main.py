# main.py
import requests
import time
import datetime
from configparser import ConfigParser
import telegram

def get_news():
    url = "https://newsdata.io/api/1/news?apikey=pub_37701c8d4cfddfbf6b6df2e86bd58703f8a8e&q=geopolitics,economy,crypto,forex,stock&language=id"
    res = requests.get(url)
    data = res.json()

    news_items = data.get("results", [])
    message = "📰 *Rangkuman Berita Global Hari Ini:*\n\n"
    for item in news_items[:5]:
        title = item.get("title", "-")
        link = item.get("link", "-")
        source = item.get("source_id", "unknown")
        message += f"• *{title}*\nSumber: `{source}`\n[Klik di sini]({link})\n\n"
    return message

def send_telegram_news(token, chat_id, message):
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)

def main():
    config = ConfigParser()
    config.read("config/settings.ini")
    token = config["telegram"]["bot_token"]
    chat_id = config["telegram"]["chat_id"]

    while True:
        now = datetime.datetime.now()
        if now.hour == 7 and now.minute == 0:
            print("⏰ Kirim berita jam 7...")
            news = get_news()
            send_telegram_news(token, chat_id, news)
            time.sleep(60)  # biar gak spam
        time.sleep(10)

if __name__ == "__main__":
    main()
