
import traceback
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from ChampuXString.generate import generate_session, ask_ques, buttons_ques, buttons_tools, ask_tools

ERROR_MESSAGE = "ᴡᴛғ ! sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ. \n\n**ᴇʀʀᴏʀ** : {} " \
            "\n\n**ᴩʟᴇᴀsᴇ ғᴏʀᴡᴀʀᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴛᴏ @itsMeShivanshu**, ɪғ ᴛʜɪs ᴍᴇssᴀɢᴇ " \
            "ᴅᴏᴇsɴ'ᴛ ᴄᴏɴᴛᴀɪɴ ᴀɴʏ sᴇɴsɪᴛɪᴠᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ " \
            "ʙᴇᴄᴀᴜsᴇ ᴛʜɪs ᴇʀʀᴏʀ ɪs **ɴᴏᴛ ʟᴏɢɢᴇᴅ ʙʏ ᴛʜᴇ ʙᴏᴛ** !"

ask_bot = "**<blockquote><b>❖ ʜᴇʀᴇ ɪs ᴛʜᴇ ʙᴏᴛ ᴍᴇᴛʜᴏᴅ.</b></blockquote>\n\n» ᴘʟᴇᴀsᴇ ᴄʜᴏᴏsᴇ ᴛʜᴇ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.: :**"

@Client.on_callback_query(filters.regex(pattern=r"^genbybot$"))
async def genbybot_callback(bot: Client, callback_query: CallbackQuery):
    # Acknowledge the callback query
    await callback_query.answer()

    # Edit the current message to show the bot generation menu
    await callback_query.message.edit_text(
        ask_bot,
        reply_markup=InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ", callback_data="pyrogram1"),
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ ᴠ2", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ ʙᴏᴛ", callback_data="pyrogram_bot"),
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ ʙᴏᴛ", callback_data="telethon_bot"),
    ],
    [
        InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="back"),
    ]
        ])
    )

@Client.on_callback_query(filters.regex(pattern=r"^genbytools$"))
async def genbytools_callback(bot: Client, callback_query: CallbackQuery):
    # Acknowledge the callback query
    await callback_query.answer()

    # Edit the current message to show the bot generation menu
    await callback_query.message.edit_text(
        ask_tools,
        reply_markup=InlineKeyboardMarkup(buttons_tools)
    )

@Client.on_callback_query(filters.regex(pattern=r"^back$"))
async def back_callback(bot: Client, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))

@Client.on_callback_query(filters.regex(pattern=r"^(generate|pyrogram|pyrogram_bot|telethon_bot|telethon)$"))
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    query = callback_query.matches[0].group(1)
    try:
        if query == "generate":
            await callback_query.answer()
            await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
        elif query == "genbybot":
            await callback_query.answer()
            await callback_query.message.reply(ask_bot, reply_markup=InlineKeyboardMarkup(buttons_bot))
        elif query == "genbytools":
            await callback_query.answer()
            await callback_query.message.reply(ask_tools, reply_markup=InlineKeyboardMarkup(buttons_tools))
        elif query == "pyrogram":
            await callback_query.answer()
            await generate_session(bot, callback_query.message)
        elif query == "pyrogram_bot":
            await callback_query.answer("» ᴛʜᴇ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴡɪʟʟ ʙᴇ ᴏғ ᴩʏʀᴏɢʀᴀᴍ ᴠ2.", show_alert=True)
            await generate_session(bot, callback_query.message, is_bot=True)
        elif query == "telethon_bot":
            await callback_query.answer()
            await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
        elif query == "telethon":
            await callback_query.answer()
            await generate_session(bot, callback_query.message, telethon=True)
    except Exception as e:
        print(traceback.format_exc())
        print(e)
        await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
