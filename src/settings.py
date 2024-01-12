import os
from environs import Env
from src.util.doppler import get_doppler_env

env = Env()
env.read_env(f"{os.getcwd()}/local.env")
get_doppler_env()
