import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.carddb import CardDBHelper

log = logging.getLogger(__name__)


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
    for result in res:
        res_msg += f'ID: {result[0]}, Vocabulary: {result[1]}, Example: {result[2]}, Voice: { "❌" if result[3]==None else "✅" }{ "❌" if result[4]==None else "✅" }{ "❌" if result[5]==None else "✅" } Image:{ "❌" if result[6]==None else "✅" }\n'
    return await msg.reply_text(res_msg)
