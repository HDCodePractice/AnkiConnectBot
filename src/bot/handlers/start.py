async def start(update, context):
    """
    /start: 
    a start function that replies some simple word
    """
    await update.message.reply_text(
        "I'm a bot that can help you create and manage your vocabulary flash cards.")
