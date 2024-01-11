import logging
import sys
import asyncio

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
log = logging.getLogger(__name__)


def main():
    from src.bot.application import application
    application.run_polling()


if __name__ == '__main__':
    main()
