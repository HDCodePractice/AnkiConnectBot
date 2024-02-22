import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ContextTypes
from utils.carddb import CardDBHelper
from settings import settings
from urllib.parse import quote_plus

log = logging.getLogger(__name__)
web_app_url = settings.WEBAPP_URL


async def search_cards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    if len(context.args) == 0:
        return await msg.reply_text("please input sarch query")

    query = " ".join(context.args)

    card_db = CardDBHelper("cards.db")
    res = card_db.search_cards_by_vocabulary(query)

    if len(res) == 0:
        return await msg.reply_text("no result found")

    res_msg = ""
    keyboard = []

    for result in res:
        res_msg += f'ID: {result[0]}, Vocabulary: {result[1]}, Example: {result[2]}, Voice: { "❌" if result[3]==None else "✅" }{ "❌" if result[4]==None else "✅" }{ "❌" if result[5]==None else "✅" } Image:{ "❌" if result[6]==None else "✅" }\n'
        # id, vocabulary, example and means set to url params and encode to base64
        url = f"{web_app_url}/edit.html?id={result[0]}&vocabulary={result[1]}&example={result[2]}"
        web_app = WebAppInfo(url)
        keyboard.append([InlineKeyboardButton(
            f"[{result[0]}] {result[1]}", web_app=web_app)])

    reply_markup = InlineKeyboardMarkup(keyboard)
    return await msg.reply_text(res_msg, reply_markup=reply_markup)
