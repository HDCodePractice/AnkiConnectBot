import logging
from telegram import Update
from telegram.ext import ContextTypes
from util.carddb import CardDBHelper

log = logging.getLogger(__name__)


async def information(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    if len(context.args) == 0:
        return await msg.reply_text("please input card id")

    card_id = int(context.args[0])
    card_db = CardDBHelper("cards.db")
    card = card_db.get_card(card_id)
    if card is None:
        return await msg.reply_text("card not found")

    vid, vocabulary, pronunciation, part_of_speech, forms, meaning, chinese_meaning, example, chinese_example, v_vocabulary, v_meaning, v_example, image = card

    await msg.reply_text(f'''Vocabulary: {vocabulary}
Pronunciation: {pronunciation}
Part of speech: {part_of_speech}
Forms: {forms}
Meaning: {meaning}
Chinese meaning: {chinese_meaning}
Example: {example}
Chinese example: {chinese_example}
''')

    if v_vocabulary is not None and len(v_vocabulary) > 0:
        await msg.reply_voice(v_vocabulary)
    if v_meaning is not None and len(v_meaning) > 0:
        await msg.reply_voice(v_meaning)
    if v_example is not None and len(v_example) > 0:
        await msg.reply_voice(v_example)
    if image is not None and len(image) > 0:
        await msg.reply_photo(image)
