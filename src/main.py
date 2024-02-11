import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
log = logging.getLogger(__name__)
logging.getLogger('httpx').setLevel(logging.WARNING)


def main():
    from bot.application import application
    application.run_polling()


if __name__ == '__main__':
    main()
