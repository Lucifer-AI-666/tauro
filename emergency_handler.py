
import telebot
import os

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

def handle_emergency(chat_id, error_msg):
    alert = f"🚨 ERRORE: {error_msg}"
    bot.send_message(chat_id, alert)
