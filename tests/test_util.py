"""Textgraph util tests."""

import unittest.mock
import subprocess
import textgraph


@unittest.mock.patch('subprocess.check_output')
def test_terminal_width(mock_subprocess_check_output):
    """Test terminal_width."""
    mock_subprocess_check_output.return_value = '1 20'
    assert textgraph.util.terminal_width() == 20


@unittest.mock.patch('subprocess.check_output')
def test_terminal_width_index_error(mock_subprocess_check_output):
    """Test terminal_width IndexError handling."""
    mock_subprocess_check_output.return_value = ''
    assert textgraph.util.terminal_width() == 79


@unittest.mock.patch('subprocess.check_output')
def test_terminal_width_subprocess_error(mock_subprocess_check_output):
    """Test terminal_width subprocess.CalledProcessError handling."""
    mock_subprocess_check_output.side_effect = subprocess.CalledProcessError(
        1,
        ['stty', 'size']
    )
    assert textgraph.util.terminal_width() == 79
