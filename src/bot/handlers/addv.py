import logging
from telegram import Update
from telegram.ext import ContextTypes
from util.gpt import get_card

# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.DEBUG
# )
log = logging.getLogger(__name__)


async def add_vocabulary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    input = msg.text.split(" ")[1:]
    if len(input) == 0:
        await msg.reply_text("/addv vocabulary@example sentence")
        return
    input = " ".join(input)
    vocabulary = input.split("@")[0]
    example = input.split("@")[1]
    log.info(f"vocabulary: {vocabulary}, example: {example}")
    card = await get_card(vocabulary, example)
    await msg.reply_text(card)
