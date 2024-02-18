import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.carddb import CardDBHelper

log = logging.getLogger(__name__)


async def delete_card(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    if len(context.args) == 0:
        return await msg.reply_text("please input card id")

    card_id = int(context.args[0])
    card_db = CardDBHelper("cards.db")
    card = card_db.get_card(card_id)
    if card is None:
        return await msg.reply_text("card not found")

    card_db.delete_card(card_id)
    return await msg.reply_text("card deleted")
