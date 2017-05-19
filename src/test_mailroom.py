"""This module tests mailroom.py."""
# import pytest


def test_create_donor_list_0_0():
    """Create donor list in dictionary."""
    from mailroom import create_donor_list
    assert len(create_donor_list()) == 20


def test_create_donor_list_0_1():
    """First entry is two words."""
    from mailroom import create_donor_list
    assert len(list(create_donor_list().keys())[0].split(" ")) == 2


def test_donor_report():
    """Print donor report."""
    from mailroom import donor_report
    pass
