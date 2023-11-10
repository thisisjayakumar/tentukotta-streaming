# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup    

CMD = ["/", "."]
            
@StreamBot.on_message((filters.command("start") | filters.regex('start⚡️')) & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__𝓢𝓞𝓡𝓡𝓨, 𝓨𝓞𝓤 𝓐𝓡𝓔 𝓐𝓡𝓔 𝓑𝓐𝓝𝓝𝓔𝓓 𝓕𝓡𝓞𝓜 𝓤𝓢𝓘𝓝𝓖 𝓜𝓔. 𝓒ᴏɴᴛᴀᴄᴛ ᴛʜᴇ 𝓓ᴇᴠᴇʟᴏᴘᴇʀ__\n\n  **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo = Var.PIC,
                caption="<i>𝙹𝙾𝙸𝙽 CHANNEL 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴🔐</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<i>𝓢𝓸𝓶𝓮𝓽𝓱𝓲𝓷𝓰 𝔀𝓮𝓷𝓽 𝔀𝓻𝓸𝓷𝓰</i> <b> <a href='https://github.com/adarsh-goel'>CLICK HERE FOR SUPPORT </a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo=Var.PIC,
        caption =f'<b>ʜᴇʟʟᴏ {m.from_user.mention(style="md")} 🦋\n\nɪ ᴀᴍ ᴘᴏᴡᴇʀғᴜʟ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ , sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ ᴀɴᴅ ɪ ᴡɪʟʟ sᴇɴᴅ ᴛʜᴇ ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ᴀɴᴅ sᴛʀᴇᴀᴍ ʟɪɴᴋ! ɪ ᴀᴍ ᴀʟsᴏ ᴀ ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ᴄᴀᴘᴛɪᴏɴ ᴀᴅᴅᴇʀ ʙᴏᴛ 🥂!!</b>',
        reply_markup = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('〆 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ 〆', url=f'http://t.me/{Var.BOT_USERNAME}?startchannel=true')
            ],[
            InlineKeyboardButton('👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ​', callback_data='owner_info'),
            InlineKeyboardButton('🌿 sᴜᴘᴘᴏʀᴛ', callback_data='support')
            ],[      
            InlineKeyboardButton('🎭 ʜᴇʟᴘ 🎭', callback_data='help'),
            InlineKeyboardButton('♻️ ᴀʙᴏᴜᴛ ♻️', callback_data='about')
        ]]
        ))



@StreamBot.on_callback_query()
async def cb_handler(client: StreamBot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>‣ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/{Var.BOT_USERNAME}><b>{Var.BOT_NAME}</b></a>\n\n‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/NovaxTG><b>ɴᴏᴠᴀ</b></a>\n\n‣ ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org><b>ᴘʏᴛʜᴏɴ</b></a>\n\n‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a>\n\n‣ ʜᴏsᴛᴇᴅ ᴏɴ : <a href=heroku.com><b>ʜᴇʀᴏᴋᴜ</b></a>\n\n‣ sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Nova_Botz><b>ɴᴏᴠᴀ ʙᴏᴛᴢ ™</b></a>\n</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('♙ ʜᴏᴍᴇ', callback_data='home'),
                        InlineKeyboardButton('ᴄʟᴏsᴇ ⊝', callback_data='close_data')
                    ]
                ]
            )
        )
    elif data == "owner_info":
        await query.message.edit_text(
            text = f"<b>↞⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟↠</b>\n\n<b>• ꜰᴜʟʟ ɴᴀᴍᴇ :</b> | ɴᴏᴠᴀ ☣ |\n<b>• ᴜꜱᴇʀɴᴀᴍᴇ : @NovaxTG</b>\n<b>• ɴᴀᴛɪᴠᴇ : ʀᴏsᴀʀɪᴏ, ᴀʀɢᴇɴᴛɪɴᴀ </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('♙ ʜᴏᴍᴇ', callback_data='home'),
                        InlineKeyboardButton('ᴄʟᴏsᴇ ⊝', callback_data='close_data')
                    ]
                ]
            )
        )
    elif data == "support":
        await query.message.edit_text(
            text = f"<b>ᴜᴘᴅᴀᴛᴇs ᴀɴᴅ ᴄᴏɴᴛᴀᴄᴛ ᴍᴏᴅᴜʟᴇ 🌿</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [[
            InlineKeyboardButton('ʏᴛᴜʙᴇ', url='https://www.youtube.com/@Nova_Botz'),
            InlineKeyboardButton('​ᴘᴀɪᴅ ᴅᴇᴠ', url='t.me/NovaxTG'),
            InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇs​', url='t.me/Nova_Botz')
            ],[
            InlineKeyboardButton('✇ ʜᴏᴍᴇ ✇', callback_data="home")
                ]]
            ))
    elif data == "connect":
        await query.message.edit_text(
            text = f"<b>❉ Hᴏᴡ Tᴏ Cᴏɴɴᴇᴄᴛ Yᴏᴜʀ Oᴡɴ Sʜᴏʀᴛɴᴇʀ\n\n➥ Iғ Yᴏᴜ Wᴀɴᴛ Tᴏ Cᴏɴɴᴇᴄᴛ Yᴏᴜʀ Oᴡɴ Sʜᴏʀᴛɴᴇʀ Tʜᴇɴ Jᴜsᴛ Sᴇɴᴅ Tʜᴇ Gɪᴠᴇɴ Dᴇᴛᴀɪʟs Iɴ Cᴏʀʀᴇᴄᴛ Fᴏʀᴍᴀᴛ.\n\n➥ ғᴏʀᴍᴀᴛ ↓↓↓\n<code>/shortlink sʜᴏʀᴛɴᴇʀsɪᴛᴇ sʜᴏʀᴛɴᴇʀᴀᴘɪ</code>\n\n➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓\n<code>/set_shortner tnshort.net b6aace46d40c605fff8e0cafbcd8fbe416851f4d</code>\n\nɪғ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ᴀᴄᴄᴏᴜɴᴛ, ᴍʏ ᴏᴘᴛɪᴏɴ <a href=https://tnshort.net/ref/Bharathraj><b>ᴛɴsʜᴏʀᴛ.ɴᴇᴛ</b></a> ʙᴇᴄᴀᴜsᴇ ɪᴛs CPM ᴡᴀs 7+</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('♙ ʜᴏᴍᴇ', callback_data='home'),
                        InlineKeyboardButton('ᴄʟᴏsᴇ ⊝', callback_data='close_data')
                    ]
                ]
            )
        )
    elif data == "help":
        await query.message.edit_text(
            text = f"<b>⊹ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ⊹\n\n⇒ sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ (ᴏʀ) ᴍᴇᴅɪᴀ ғʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ\n\n⇒ ᴛʜɪs ʙᴏᴛ ᴡɪʟʟ sᴇɴᴅ ʏᴏᴜ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴀɴᴅ sᴛʀᴇᴀᴍ ʟɪɴᴋ\n\n⇒ ғᴏʀ sᴛʀᴇᴀᴍɪɴɢ ᴊᴜsᴛ ᴄᴏᴘʏ ᴛʜᴇ ᴍᴏɴᴏ ʟɪɴᴋ ᴀɴᴅ ᴘᴀsᴛᴇ ɪᴛ ɪɴ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴛᴏ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ\n\n⇒ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟsᴏ sᴜᴘᴘᴏʀᴛᴇᴅ ɪɴ ᴄʜᴀɴɴᴇʟs. ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ᴡᴏʀᴋᴀʙʟᴇ...!\n\n⇒ ᴊᴜsᴛ sᴇɴᴅ ᴀ ғɪʟᴇ, ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴄᴀᴘᴛɪᴏɴ\n\n⇒ ғᴏʀ ᴘᴀɪᴅ ᴅᴇᴠᴇʟᴏᴘɪɴɢ : <a href=https://t.me/NovaxTG><b>ɴᴏᴠᴀ</b></a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('♙ ʜᴏᴍᴇ', callback_data='home'),
                        InlineKeyboardButton('ᴄʟᴏsᴇ ⊝', callback_data='close_data')
                    ]
                ]
            )
        )
    elif data == "home":
        await query.message.edit_text(
            text = f"<b>ɪ ᴀᴍ ᴘᴏᴡᴇʀғᴜʟ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ . sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ ᴀɴᴅ ɪ ᴡɪʟʟ sᴇɴᴅ ᴛʜᴇ ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ᴀɴᴅ sᴛʀᴇᴀᴍ ʟɪɴᴋ! ɪ ᴀᴍ ᴀʟsᴏ ᴀ ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ᴄᴀᴘᴛɪᴏɴ ᴀᴅᴅᴇʀ ʙᴏᴛ 🥂\n\nғᴏʀ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ /tutorial !!</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [[
            InlineKeyboardButton('〆 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ 〆', url=f'http://t.me/{Var.BOT_USERNAME}?startchannel=true')
            ],[
            InlineKeyboardButton('👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ​', callback_data='owner_info'),
            InlineKeyboardButton('🌿 sᴜᴘᴘᴏʀᴛ', callback_data='support')
            ],[      
            InlineKeyboardButton('🎭 ʜᴇʟᴘ 🎭', callback_data='help'),
            InlineKeyboardButton('♻️ ᴀʙᴏᴜᴛ ♻️', callback_data='about')
            ]]
            ))
    elif query.data == "close_data":
        await query.message.delete()

@StreamBot.on_message((filters.command("help") | filters.regex('help📚')) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ FROM USING ᴍᴇ. Cᴏɴᴛᴀᴄᴛ ᴛʜᴇ Dᴇᴠᴇʟᴏᴘᴇʀ</i>",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/ca10e459bc6f48a4ad0f7.jpg",
                Caption="**𝙹𝙾𝙸𝙽 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿 𝚃𝙾 𝚄𝚂𝙴 ᴛʜɪs Bᴏᴛ!**\n\n__Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍᴇ__ [ADARSH GOEL](https://github.com/adarsh-goel/-pro/issues).",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b> Send me any file or video i will give you streamable link and download link.</b>\n
<b> I also support Channels, add me to you Channel and send any media files and see miracle✨ also send /list to know all commands""",
        
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("💁‍♂️ DEV", url="https://github.com/adarsh-goel")],
                [InlineKeyboardButton("💥 Source Code", url="https://github.com/adarsh-goel/-pro/")]
            ]
        )
    )

@StreamBot.on_message(filters.command("tutorial", CMD))
async def tutorial(_, message):
    video=(Var.TUTORIAL_VIDEO)

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("⊝ Close ⊝", callback_data='close_data')]
        ]
    )
    await message.reply_video(video=Var.TUTORIAL_VIDEO, reply_markup=keyboard)  

