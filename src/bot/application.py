from telegram.ext import ApplicationBuilder, Application, CommandHandler
from bot.common.context import context_types
from settings import settings
from bot.handlers.index import index


async def on_startup(app: Application):
    pass


application: Application = (
    ApplicationBuilder()
    .token(settings.BOT_TOKEN)
    .context_types(context_types)
    # .arbitrary_callback_data(True)
    .post_init(on_startup)
    .build()
)

for k, v in index().items():
    application.add_handler(CommandHandler(k, v))
