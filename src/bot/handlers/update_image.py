import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.carddb import CardDBHelper
import tempfile

log = logging.getLogger(__name__)


async def update_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    if len(context.args) == 0:
        return await msg.reply_text("please input card id")

    with tempfile.NamedTemporaryFile() as image_file:
        image = await get_reply_image(image_file.name, update, context)
        if image is None:
            return await msg.reply_text("please reply to a photo message")

        card_id = int(context.args[0])
        card_db = CardDBHelper("cards.db")
        card = card_db.get_card(card_id)
        if card is None:
            return await msg.reply_text("card id not found")
        if card_db.update_image_by_id(card_id, image_file.name) is None:
            return await msg.reply_text("card image update failed")
        return await msg.reply_text("card image updated")


async def get_reply_image(image_path: str, update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 获取回复消息
    reply_message = update.message.reply_to_message
    if reply_message and reply_message.photo:
        # 获取回复消息的第一张图片
        photo_file_id = reply_message.photo[-1].file_id
        # 通过文件ID获取图片文件对象
        photo_file = await context.bot.get_file(photo_file_id)
        # 下载图片到本地
        await photo_file.download_to_drive(image_path)
        return image_path
    else:
        return
