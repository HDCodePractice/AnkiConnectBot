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

command_map = {
    'start': start,
    # ....
    # one-to-one correspondence mapping
    # map command to function here
    # ....
    'whoami': whoami,
    'help': help_command,
    'a': add_vocabulary,
    'uv': update_voice,
    'ui': update_image,
    's': search_cards,
    'i': information
}

# --------------------------------------


def index():
    """

    """
    return command_map
