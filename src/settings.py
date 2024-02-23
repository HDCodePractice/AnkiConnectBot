from io import StringIO
import os
from environs import Env
from utils import doppler


def get_doppler_env():
    doppler_token = env.str('DOPPLER_TOKEN', default='')

    if len(doppler_token) > 0:
        response = doppler.get_doppler_env(doppler_token)
        if len(response) > 0:
            config = StringIO(response)
            env.read_file(config)


env = Env()
env.read_env(f"{os.getcwd()}/local.env")
get_doppler_env()


class settings:
    DEBUG = env.bool('DEBUG', default=False)
    BOT_TOKEN = env.str('BOT_TOKEN', default='')
    WEBAPP_URL = env.str(
        'WEBAPP_URL', default='https://127.0.0.1:4443/web/')
    OPENAI_API_KEY = env.str('OPENAI_API_KEY', default='')
    OPENAI_API_URL = env.str(
        'OPENAI_API_URL', default='https://api.openai.com/v1')
    OPENAI_MODEL = env.str('OPENAI_MODEL', default='gpt-3.5-turbo')
