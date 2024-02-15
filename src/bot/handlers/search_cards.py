import logging
from telegram import Update
from telegram.ext import ContextTypes
from util.tts import generation_audio_file
from util.carddb import CardDBHelper
import tempfile

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
        res_msg += f'ID: {result[0]}, Vocabulary: {result[1]}, Example: {result[2]}\n'
    return await msg.reply_text(res_msg)
