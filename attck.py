from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import os,json,random,asyncio
import tgcrypto
ONWER = 2029106808
channel = None # دست نزن
API_HASH = "8edc44bad592cbc7772df91460cce721"
API_ID = 17876846

if not os.path.exists("fosh.json"):
    with open(file="fosh.json",mode="w",encoding="utf-8") as f:
        json.dump(obj=[],fp=f)

# MichelleJohnston
class Bot:
    def __init__(self) -> None:
        pass
    async def attacker(self,name:str,token:str):
        self.name = name
        self.token = token
        self.admin = []
        self.gofl = []
        self.enmy = []
        self.usechannel = False
        app = Client(name=self.name,bot_token=self.token,api_hash=API_HASH,api_id=API_ID)
        @app.on_message(filters.regex("قفل"))
        async def on(client,message):
            if message.from_user.id == ONWER or message.from_user.id in self.admin:
              if not message.text == "قفل":
                with open(file="fosh.json",encoding="utf-8") as f:
                    fosh = json.load(fp=f)
                    if not fosh or self.usechannel == True:
                        if channel:
                            ff = await app.get_messages(chat_id=channel,message_ids=[i for i in range(-200,0)][::-1])
                            fosh = [msg.text for msg in ff]
                        else:
                            await app.send_message(chat_id=message.chat.id,text="هیچ فحشی در ربات تنظیم نشده است",reply_to_message_id=message.text)
                            return()
                txt = message.text.split()
                self.gofl.append(txt[3].strip())
                username = txt[3].strip() if not txt[3].strip().isdigit() else f"[{(await app.get_users(txt[3].strip())).first_name}](tg://user?id={txt[3].strip()})"
                for i in range(int(txt[1].strip())):
                  if txt[3].strip() in self.gofl:
                    await app.send_message(chat_id=message.chat.id,text=random.choice(fosh)+"\n"+username )
                    await asyncio.sleep(float(txt[2].strip()))
                  else:
                      await app.send_message(chat_id=message.chat.id,text="قفل غیرفعال شد")
                      return()
              else:
                  await app.send_message(chat_id=message.chat.id,text="مقادیر را تنظیم کنید\nمثال : قفل <تعداد> <زمان> <یوزرنیم>",reply_to_message_id=message.id)
        @app.on_message(filters.regex("قطع"))
        async def stop_on(client,message):
            if message.from_user.id == ONWER or message.from_user.id in self.admin:
              if not message.text == "قطع":
                  txt = message.text.split()
                  if txt[1].strip() in self.gofl:
                      self.gofl.remove(txt[1].strip())
                  else:
                      await app.send_message(chat_id=message.chat.id,text="این فرد قفل نشده است")
              else:
                  await app.send_message(chat_id=message.chat.id,text="مقادیر را تنظیم کنید\nمثال : قطع <یوزرنیم>",reply_to_message_id=message.id)
        @app.on_message(filters.regex("addfosh"))
        async def AddFosh(client,message):
            if message.from_user.id == ONWER or message.from_user.id in self.admin:
                if not message.text == "addfosh":
                    txt = message.text.split("addfosh")
                    with open(file="fosh.json",encoding="utf-8") as f:
                        fosh = json.load(fp=f)
                    fosh.append(txt[1])
                    with open(file="fosh.json",mode="w",encoding="utf-8") as f:
                        json.dump(obj=fosh,fp=f)
                    await app.send_message(chat_id=message.chat.id,text="اضافه شد",reply_to_message_id=message.id)
                else:
                    await app.send_message(chat_id=message.chat.id,text="مقادیر را تنظیم کنید\nمثال : addfosh <فحش>",reply_to_message_id=message.id)
        @app.on_message(filters.regex("delfosh"))
        async def deletefosh(client,message):
            if message.from_user.id == ONWER or message.from_user.id in self.admin:
                if not message.text == "addfosh":
                    txt = message.text.split("delfosh")
                    with open(file="fosh.json",encoding="utf-8") as f:
                        fosh = json.load(fp=f)
                    if txt[1] in fosh:
                        fosh.remove(txt[1])
                        with open(file="fosh.json",mode="w",encoding="utf-8") as f:
                            json.dump(obj=fosh,fp=f)
                        await app.send_message(chat_id=message.chat.id,text="حذف شد",reply_to_message_id=message.id)
                    else:
                        await app.send_message(chat_id=message.chat.id,text="این فحش در ربات ثبت نشده است",reply_to_message_id=message.id)
                else:
                    await app.send_message(chat_id=message.chat.id,text="مقادیر را تنظیم کنید\nمثال : delfosh <فحش>",reply_to_message_id=message.id)
        @app.on_message(filters.regex("addadmin"))
        async def Addadmin(client,message):
            if message.from_user.id == ONWER:
                if not message.text == "addadmin" or message.reply_to_message:
                    txt = message.text.split()
                    self.admin.append(int(txt[1].strip()) if not message.text == "addadmin" else message.reply_to_message.from_user.id)
                    await app.send_message(chat_id=message.chat.id,text="اضافه شد",reply_to_message_id=message.id)
                else:
                    await app.send_message(chat_id=message.from_user.id,text="مقادیر را تنظیم کنید\nمثال : addadmin <آیدی عددی>",reply_to_message_id=message.id)
        @app.on_message(filters.regex("deleteadmin"))
        async def Deleteadmin(client,message):
            if message.from_user.id == ONWER:
                if not message.text == "deleteadmin" or message.reply_to_message:
                    txt = message.text.split()
                    if int(txt[1].strip()) in self.admin:
                        self.admin.remove(int(txt[1].strip()) if not message.text == "deleteadmin" else message.reply_to_message.from_user.id)
                        await app.send_message(chat_id=message.chat.id,text="حذف شد",reply_to_message_id=message.id)
                    else:
                        await app.send_message(chat_id=message.chat.id,text="این فرد در لیست ادمین ها وجود ندارد",reply_to_message_id=message.id)
                else:
                    await app.send_message(chat_id=message.from_user.id,text="مقادیر را تنظیم کنید\nمثال : deleteadmin <آیدی عددی>",reply_to_message_id=message.id)
        @app.on_message(filters.regex("setenemy"))
        async def SetEnemy(client,message):
            if message.from_user.id == ONWER or message.from_user.id in self.admin:
                if not message.text == "setenemy" or message.reply_to_message:
                    user = int(message.text.split()[1].strip()) if not message.text == "setenemy" else message.reply_to_message.from_user.id
                    self.enmy.append(user)
                    await app.send_message(chat_id=message.chat.id,text="کاربر موردنظر به لیست انمی اضافه شد",reply_to_message_id=message.id)
                else:
                    await app.send_message(chat_id=message.chat.id,text="لطفا روی کاربر ریپلی بزنید یا مقادیر را تنظیم کنید\nمثال : setenemy <آیدی عددی>",reply_to_message_id=message.id)
        @app.on_message(filters.regex("delenemy"))
        async def DeleteEnemy(client,message):
            if message.from_user.id == ONWER or message.from_user.id in self.admin:
                if not message.text == "delenemy" or message.reply_to_message:
                    user = int(message.text.split()[1].strip()) if not message.text == "delenemy" else message.reply_to_message.from_user.id
                    if user in self.enmy:
                        self.enmy.remove(user)
                    else:
                        await app.send_message(chat_id=message.chat.id,text="این کاربر در لیست انمی وجود ندارد",reply_to_message_id=message.id)
                        return()
                    await app.send_message(chat_id=message.chat.id,text="کاربر موردنظر از لیست انمی حذف شد",reply_to_message_id=message.id)
                else:
                    await app.send_message(chat_id=message.chat.id,text="لطفا روی کاربر ریپلی بزنید یا مقادیر را تنظیم کنید\nمثال : deleteenemy <آیدی عددی>",reply_to_message_id=message.id)
        @app.on_message(filters.regex("addchannel"))
        async def AddChannel(client,message):
            global channel
            if message.from_user.id == ONWER:
                if not message.text == "addchannel":
                    txt = message.text.split()
                    channel = txt[1]
                    await app.send_message(chat_id=message.chat.id,text="چنل با موفقیت تنظیم شد")
                else:
                    await app.send_message(chat_id=message.chat.id,text="لطفا مقادیر را تنظیم کنید\nمثال : addchannel <یوزرنیم یا آیدی چنل>",reply_to_message_id=message.id)
        @app.on_message(filters.regex("channel"))
        async def Channel(client,message):
            if message.from_user.id == ONWER or message.from_user.id in self.admin:
                if message.text == "channel":
                    rply = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="✔️",callback_data="on_channel"),InlineKeyboardButton(text="❌",callback_data="off_channel")]])
                    await app.send_message(chat_id=message.chat.id,text="انتخاب کنید",reply_markup=rply)
        @app.on_callback_query()
        async def Setting(client,CallbackQuery):
            # if CallbackQuery.from_user.id == ONWER or CallbackQuery.from_user.id in self.admin:
            if CallbackQuery.data == "on_channel":
                if CallbackQuery.from_user.id == ONWER or CallbackQuery.from_user.id in self.admin:
                    await CallbackQuery.message.delete()
                    self.usechannel = True
            elif CallbackQuery.data == "off_channel":
                if CallbackQuery.from_user.id == ONWER or CallbackQuery.from_user.id in self.admin:
                    await CallbackQuery.message.delete()
                    self.usechannel = False

        @app.on_message(filters.regex("offbot"))
        async def OffBot(client,message):
            if message.from_user.id == ONWER and message.text == "offbot":
                await app.send_message(chat_id=message.chat.id,text="ربات با موفقیت غیرفعال شد",reply_to_message_id=message.id)
                await app.stop()
        @app.on_message(filters.regex("ping"))
        async def ping(client,message):
            if message.from_user.id == ONWER or message.from_user.id in self.admin:
                await app.send_message(chat_id=message.chat.id,text="𝙿𝙾𝙽𝙶!",reply_to_message_id=message.id)
        @app.on_message()
        async def enemy(client,message):
            global channel
            if message.from_user.id in self.enmy:
                with open(file="fosh.json",encoding="utf-8") as f:
                    fosh = json.load(fp=f)
                    if not fosh or self.usechannel == True:
                        if channel:
                            ff = await app.get_messages(chat_id=channel,message_ids=random.randint(-200,0))
                            fosh = [msg.text for msg in ff]
                        else:return()
                    await app.send_message(chat_id=message.chat.id,text=random.choice(fosh),reply_to_message_id=message.id)
        
        await app.start()