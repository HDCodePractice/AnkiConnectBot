import logging
from telegram import Update
from telegram.ext import ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
log = logging.getLogger(__name__)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /help:
    return this help
    """
    from .index import index
    text = '<b>HELP:</b>\n'
    for k, v in index().items():
        text += v.__doc__
    await update.message.reply_text(text, parse_mode='HTML')
