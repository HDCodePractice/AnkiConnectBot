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
from .up_voice import up_voice

command_map = {
    'start': start,
    # ....
    # one-to-one correspondence mapping
    # map command to function here
    # ....
    'whoami': whoami,
    'help': help_command,
    'a': add_vocabulary,
    'uv': up_voice
}

# --------------------------------------


def index():
    """

    """
    return command_map
