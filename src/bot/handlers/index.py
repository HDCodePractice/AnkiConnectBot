"""
index.py
---------
index all function handlers
"""


# imports here -----------------------
from .start import start
from .help import help_command
from .whoami import whoami
from .add_vocabulary import add_vocabulary
from .update_voice import update_voice
from .update_image import update_image
from .search_cards import search_cards
from .information import information
from .delete_card import delete_card
from .gen_deck import gen_deck

command_map = {
    'start': start,
    'whoami': whoami,
    'help': help_command,
    'a': add_vocabulary,
    'uv': update_voice,
    'ui': update_image,
    's': search_cards,
    'i': information,
    'd': delete_card,
    'g': gen_deck
}

# --------------------------------------


def index():
    """

    """
    return command_map
