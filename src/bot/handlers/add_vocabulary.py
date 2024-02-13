import logging
from telegram import Update
from telegram.ext import ContextTypes
from util.gpt import get_card
import json
from util.carddb import CardDBHelper
from util.tts import generation_audio_file
import os
import tempfile

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
    # 将card json string转为object
    card_data = json.loads(card)
    vocabulary = card_data["Vocabulary"]
    pronunciation = card_data["Pronunciation"]
    definition = card_data["Definitions"][0]
    part_of_speech = definition.get("PartOfSpeech", "")
    forms = definition.get("Forms", "")
    meaning = definition.get("Meaning", "")
    example = definition.get("Example", "")
    chinese_example = definition.get("ChineseExample", "")

    # 将card插入数据库
    card_db = CardDBHelper("cards.db")
    insert_card = (vocabulary, pronunciation, part_of_speech,
                   forms, meaning, example, chinese_example)
    card_id = card_db.insert_card(insert_card)
    await msg.reply_text(f"""Vocabulary[{card_id}]:{vocabulary}
Pronunciation:{pronunciation}
Part of speech:{part_of_speech}
Forms:{forms}
Meaning:{meaning}
Example:{example}
Chinese example:{chinese_example}""")

    # 生成语音
    with tempfile.NamedTemporaryFile() as v_audio, \
            tempfile.NamedTemporaryFile() as m_audio, \
            tempfile.NamedTemporaryFile() as e_audio:
        await generation_audio_file(vocabulary, v_audio.name)
        await generation_audio_file(meaning, m_audio.name)
        await generation_audio_file(example, e_audio.name)

        await msg.reply_voice(v_audio)
        await msg.reply_voice(m_audio)
        await msg.reply_voice(e_audio)

    card_db.close()
