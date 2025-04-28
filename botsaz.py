from pyrogram import Client,filters
from pyrogram.types import ReplyKeyboardMarkup
import pyromod.listen
from attck import Bot
import tgcrypto

from keep_live import keep_alive
keep_alive()

ONWER = 2029106808
API_HASH = "8edc44bad592cbc7772df91460cce721"
API_ID = 17876846
app = Client(name="botsaz",bot_token="5892949239:AAFLC319sZ_t9INl6OV29wWooce5dl0TFz8",api_hash=API_HASH,api_id=API_ID)

@app.on_message(filters.command("start"))
@app.on_message(filters.regex("بازگشت"))
async def Start(client,message):
    if message.from_user.id == ONWER:
        reply = ReplyKeyboardMarkup(keyboard=[["ساخت ربات"]],resize_keyboard=True)
        await app.send_message(chat_id=message.chat.id,text="خوش آمدید، انتخاب کنید",reply_markup=reply)

@app.on_message(filters.regex("ساخت ربات"))
async def Create(client,message):
    if message.from_user.id == ONWER:
        reply = ReplyKeyboardMarkup(keyboard=[["بازگشت"]],resize_keyboard=True)
        token = await app.ask(chat_id=message.chat.id,text="توکن ربات را ارسال کنید",reply_markup=reply, filters=filters.user(message.from_user.id))
        if token.text == "بازگشت":
            await Start(client,token)
        else:
          for i in token.text.splitlines():
            await app.send_message(chat_id=message.chat.id,text="ربات فعال شد",reply_markup=ReplyKeyboardMarkup(keyboard=[["ساخت ربات"]],resize_keyboard=True))
            bot = Bot()
            await bot.attacker(name=i.split(":")[0],token=token.text)




app.run()
