import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = telebot.TeleBot("8908913545:AAFqVtBWMZNTrJQKGJxDPyi3wsSHC9iv77Y")

text = "Приветствую тебя друг, ты попал в моего крипто бота ⌚, бот полностью верифицирован компанией @send, и не относится к ск@м схемам, все платежи покупки и продажи полностью безопасны в этом кругу. Удачного пользования"

@bot.message_handler(commands=['start'])
def start(msg):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text="Открыть кошелек 🚀", web_app=WebAppInfo(url="https://onrender.com")))
    bot.send_message(msg.chat.id, text, reply_markup=kb)

bot.infinity_polling()
