from io import StringIO
from cli.cli import CLI
import sys
import unittest
from unittest import TestCase, mock

def input(*cmds):
    """Replace input."""
    visible_cmds = "\n".join([c for c in cmds if isinstance(c, str)])
    hidden_cmds = [c.get("hidden") for c in cmds if isinstance(c, dict)]
    with mock.patch("sys.stdin", StringIO(f"{visible_cmds}\n")), mock.patch("getpass.getpass", side_effect=hidden_cmds):
        yield

def test_cli_question():
    interface = CLI()
    with input("hello"):
        user_answer = interface.ask_user_input("type hello >")
        print("User answer:", user_answer)
        assert ('hello' == user_answer)
