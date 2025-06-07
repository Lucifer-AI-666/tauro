
import os
import json
import openai
import telebot
import requests
from voice_output import speak
from emergency_handler import handle_emergency

# Load environment variables
from dotenv import load_dotenv
load_dotenv("config.env")

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))
openai.api_key = os.getenv("OPENAI_API_KEY")
voice_enabled = True

def load_memory(user_id):
    try:
        with open("user_memory.json", "r") as f:
            mem = json.load(f)
        return mem.get(str(user_id), "")
    except:
        return ""

def save_memory(user_id, content):
    try:
        with open("user_memory.json", "r") as f:
            mem = json.load(f)
    except:
        mem = {}
    mem[str(user_id)] = content
    with open("user_memory.json", "w") as f:
        json.dump(mem, f)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "🧠 Tauros attivo. Dimmi tutto.")

@bot.message_handler(commands=['mirror_on'])
def mirror(message):
    bot.reply_to(message, "🪞 Occhio attivo. Sto osservando.")

@bot.message_handler(commands=['reset'])
def reset_memory(message):
    save_memory(message.chat.id, "")
    bot.reply_to(message, "🔄 Memoria resettata.")

@bot.message_handler(func=lambda m: True)
def chat_handler(message):
    try:
        memory = load_memory(message.chat.id)
        prompt = f"{memory}
Utente: {message.text}
Tauros:"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        answer = response['choices'][0]['message']['content']
        save_memory(message.chat.id, prompt + answer)
        bot.send_message(message.chat.id, answer)
        if voice_enabled:
            speak(answer)
    except Exception as e:
        handle_emergency(message.chat.id, str(e))

bot.polling()
