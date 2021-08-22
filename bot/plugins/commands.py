#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = f"{file_name} /n ♻️ 𝙁𝙊𝙍 𝙉𝙀𝙒 𝙈𝙊𝙑𝙄𝙀𝙎 ♻️
          @D_W_T_1  

♻️ 𝙊𝙐𝙍 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ♻️
 
❤𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻❤ https://t.me/joinchat/4epcwX6e3_JmYjE1

♻𝙁𝙊𝙍 𝙊𝙇𝘿 𝘼𝙉𝘿 𝙉𝙀𝙒 𝙈𝙊𝙑𝙄𝙀♻️

❤𝙔𝙊𝙐 𝘾𝘼𝙉 𝙏𝙔𝙋𝙀 𝘼𝙉𝘿 𝙁𝙄𝙉𝘿 𝙔𝙊𝙐𝙍 𝙈𝙊𝙑𝙄𝙀𝙎 𝙄𝙉 𝙏𝙃𝙄𝙎 𝙂𝙍𝙊𝙐𝙋❤

❤𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿❤  https://t.me/joinchat/BhYlk3vvhG5hMmZl

🚫𝙿𝙻𝙴𝙰𝚂𝙴 𝙹𝙾𝙸𝙽 𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙱𝙴𝙵𝙾𝚁𝙴 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 🚫

♻️𝙅𝙊𝙄𝙉♻️𝙎𝙃𝘼𝙍𝙀♻️𝙎𝙐𝙋𝙋𝙊𝙍𝙏♻️", 
 
,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '♻️ OUR GROUP ♻️', url="https://t.me/joinchat/BhYlk3vvhG5hMmZl"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('Developers', url='https://t.me/D_W_T_1'),
        InlineKeyboardButton('Source Code 🧾', url ='https://t.me/D_W_T_1')
    ],[
        InlineKeyboardButton('Support 🛠', url='https://t.me/D_W_T_1')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
