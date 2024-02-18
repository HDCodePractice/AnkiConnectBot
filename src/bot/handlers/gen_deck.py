from utils.package_deck import async_create_hd_deck
import logging
from telegram import Update
from telegram.ext import ContextTypes

log = logging.getLogger(__name__)


async def gen_deck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Generate a deck of vocabulary cards
    """
    log.info("Generating deck...")
    deck_path = await async_create_hd_deck()
    log.info(f"Deck generated: {deck_path}")
    await update.message.reply_document(document=open(deck_path, 'rb'))
    log.info("Deck sent.")
