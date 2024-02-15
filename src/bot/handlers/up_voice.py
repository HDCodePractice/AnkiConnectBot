import logging
from telegram import Update
from telegram.ext import ContextTypes
from util.tts import generation_audio_file
from util.carddb import CardDBHelper
import tempfile

log = logging.getLogger(__name__)


async def up_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    if len(context.args) == 0:
        return await msg.reply_text("please input card id")

    card_id = int(context.args[0])
    card_db = CardDBHelper("cards.db")
    card = card_db.get_card(card_id)
    if card is None:
        return await msg.reply_text("card id not found")
    vocabulary, pronunciation, part_of_speech, forms, meaning, chinese_meaning, example, chinese_example = card

    # 生成语音
    with tempfile.NamedTemporaryFile() as v_audio, \
            tempfile.NamedTemporaryFile() as m_audio, \
            tempfile.NamedTemporaryFile() as e_audio:
        await generation_audio_file(vocabulary, v_audio.name)
        await generation_audio_file(meaning, m_audio.name)
        await generation_audio_file(example, e_audio.name)

        card_db.update_sound_files_by_id(
            card_id, v_audio.name, m_audio.name, e_audio.name)

        await msg.reply_voice(v_audio)
        await msg.reply_voice(m_audio)
        await msg.reply_voice(e_audio)
