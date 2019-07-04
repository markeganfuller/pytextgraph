"""Utilities for textgraph."""

import subprocess


def terminal_width():
    """
    Return width of current terminal.

    This allows autosizing of graphs.
    """
    try:
        # Rows is 0, columns is 1
        columns = int(subprocess.check_output(['stty', 'size']).split()[1])
    except (IndexError, subprocess.CalledProcessError):
        columns = 79
    return columns
