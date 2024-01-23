import os
from environs import Env
from src.util.doppler import get_doppler_env

env = Env()
env.read_env(f"{os.getcwd()}/local.env")
get_doppler_env()

conf = {
    'anki_connect_base_url': env.str("ANKI_URL", "http://localhost:8765")
}
