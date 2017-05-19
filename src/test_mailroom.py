"""This module tests mailroom.py."""
import pytest


def test_create_donor_list_0_0():
    """Create donor list in dictionary."""
    from mailroom import create_donor_list
    assert len(create_donor_list()) == 20


def test_create_donor_list_0_1():
    """First entry is two words."""
    from mailroom import create_donor_list
    assert len(list(create_donor_list().keys())[0].split(" ")) == 2


@pytest.mark.parametrize("fake_choice", [1, 2, 3, 4, "exit"])
def test_usr_input(monkeypatch, fake_choice):
    """Test user input behavior.
        Using monkeypatch to put in input."""
    from mailroom import usr_input
    monkeypatch.setitem(__builtins__, 'input', lambda choice: fake_choice)
    assert usr_input() == fake_choice


def test_send_thank_you():
    """Print donor report."""
    from mailroom import send_thank_you
    pass


def test_donor_report():
    """Print donor report."""
    from mailroom import donor_report
    pass
