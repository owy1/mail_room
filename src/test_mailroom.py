"""This module tests mailroom.py."""
import pytest
import mailroom.py

PARAMS_TABLE = [
        (1, True),
        (2, True),
        (3, True),
        (4, True)
]


def send_thank_you():
    """Dummy var for 
    return True


def donor_report():
    return True

def  usr_input():
    return True

def test_create_donor_list_0_0():
    """Create donor list in dictionary."""
    from mailroom import create_donor_list
    assert len(create_donor_list()) == 20

def test_create_donor_list_0_1():
    """First entry is two words."""
    from mailroom import create_donor_list
    assert len(create_donor_list().items()[0][0].split(" ")) == 2

@pytest.mark.parametrize("m, result")
def test_usr_input()_0_0:
    """Test user input behavior."""
    from mailroom import test_usr_input

def test_send_thank_you():
    """Print donor report."""
    from mailroom import send_thank_you

def test_donor_report():
    """Print donor report."""
    from mailroom import donor_report